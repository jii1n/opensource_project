
from quart import Quart, request, jsonify, abort
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
from dotenv import load_dotenv
import os

# Load environment variables from a .env file for better security and configuration management
load_dotenv()

# Initialize Quart app
app = Quart(__name__)

# Initialize Notion client with an authentication token from environment variables
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# Define the Google API scope needed for calendar access
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
    """Retrieve Google Calendar service object to interact with the API."""
    creds = None
    # Check if access token exists in 'token.json' for reuse
    if os.path.exists("token.json"):
        with open("token.json", "r") as token:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Refresh or obtain new credentials if necessary
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service

# calendar의 일정 읽어오기(-> html페이지(/read_events)에서 일정목록을 확인할 수 있음)
@app.route("/read_events", methods=["GET"])
async def read_events():
    """API endpoint to read events from a specified Google Calendar."""
    service = get_calendar_service()

    # Retrieve query parameters with defaults
    calendar_id = request.args.get("calendar_id", "primary")
    time_min = request.args.get(
        "time_min", datetime.datetime.utcnow().isoformat() + "Z"
    )
    time_max = request.args.get("time_max", None)

    try:
        # Call the Google Calendar API to list events
        events_result = (
            service.events()
            .list(
                calendarId=calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        # 일정의 추가설명, 날짜, 시간, 장소, 참여자(ex. 만나기로 한 사람)을 읽도록 설정함
        extracted_events = [
            {
                "id": event.get("id"),
                "summary": event.get("summary"),
                "description": event.get("description"),
                "start_date": event["start"].get("dateTime", event["start"].get("date")).split("T")[0],
                "start_time": event["start"].get("dateTime").split("T")[1] if "T" in event["start"].get("dateTime", "") else None,
                "end_date": event["end"].get("dateTime", event["end"].get("date")).split("T")[0],
                "end_time": event["end"].get("dateTime").split("T")[1] if "T" in event["end"].get("dateTime", "") else None,
                "location": event.get("location"),
                "attendees": [
                    attendee.get("email") for attendee in event.get("attendees", [])
                ]
            }
            for event in events
        ]

        return jsonify(extracted_events)
    except Exception as e:
        abort(500, description=str(e))


# gpt로 calendar에 일정 추가( ex. gpt에게 '00월 00일 누구와~~~ 일정추가해줘'라고 전달하면 calendar에 일정이 추가됨)
# 일정의 추가설명, 날짜, 시간, 장소, 참여자(ex. 함께하기로 한 사람)등이 calendar에 추가되도록 함.
@app.route("/create_event", methods=["POST"])
async def create_event():
    """API endpoint to create a new event in a specified Google Calendar."""
    service = get_calendar_service()
    data = await request.get_json()

    # Retrieve event details from request body
    calendar_id = data.get("calendar_id", "primary")
    summary = data.get("summary")
    description = data.get("description")
    start_time = data.get("start_time")  # Expected in RFC3339 format
    end_time = data.get("end_time")  # Expected in RFC3339 format
    location = data.get("location")
    attendees = data.get("attendees", [])  # List of attendee email addresses

    # Validate required fields
    if not all([summary, start_time, end_time]):
        abort(400, description="Missing required event fields.")

    # Prepare event data
    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_time} if "T" in start_time else {"date": start_time},
        "end": {"dateTime": end_time} if "T" in end_time else {"date": end_time},
        "location": location,
        "attendees": [{"email": attendee} for attendee in attendees],
    }

    try:
        # Call the Google Calendar API to create the event
        created_event = (
            service.events().insert(calendarId=calendar_id, body=event).execute()
        )
        return jsonify({
            "id": created_event.get("id"),
            "summary": created_event.get("summary"),
            "description": created_event.get("description"),
            "start_date": created_event["start"].get("dateTime", created_event["start"].get("date")).split("T")[0],
            "start_time": created_event["start"].get("dateTime").split("T")[1] if "T" in created_event["start"].get("dateTime", "") else None,
            "end_date": created_event["end"].get("dateTime", created_event["end"].get("date")).split("T")[0],
            "end_time": created_event["end"].get("dateTime").split("T")[1] if "T" in created_event["end"].get("dateTime", "") else None,
            "location": created_event.get("location"),
            "attendees": [
                attendee.get("email") for attendee in created_event.get("attendees", [])
            ]
        })
    except Exception as e:
        abort(500, description=str(e))


# gpt로 calendar에 저장된 일정 삭제
@app.route("/delete_event", methods=["DELETE"])
async def delete_event():
    """API endpoint to delete an event from a specified Google Calendar."""
    service = get_calendar_service()

    calendar_id = request.args.get("calendar_id", "primary")
    event_id = request.args.get("event_id")

    if not event_id:
        abort(400, description="Event ID is required.")

    try:
        # Call the Google Calendar API to delete the event
        service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        return jsonify({"status": "success", "message": "Event deleted successfully"})
    except Exception as e:
        abort(500, description=str(e))


if __name__ == "__main__":
    # Delete token.json file to force re-authentication
    if os.path.exists("token.json"):
        os.remove("token.json")

    app.run()



   
