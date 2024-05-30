### Custom GPT Tutorial

#### 요약
- .py의 역활
  - calendar에 저장된 일정을 읽어와 json 형식으로 변환
  - 직접 본인의 calendar로 가서 **'일정 확인,추가,삭제'** 가 아닌 endpoint를 이용해 gpt와 calendar의 데이터 교환 가능
  -> gpt와의 상호작용을 통해 gpt상에서 calendar의 내용을 확인, 추가, 삭제할 수 있음

- explore gpts의 **"cutstom gpt"** 기능 
  - 나만의 custom gpt 생성 
  - .py를 통해 만들어진 endpoint를 입력해 gpt에게 데이터(일정)을 주고받음
    -> custom gpt 사용자는 calendar로 직접 접근하지 않으면서 gpt상에서 일정을 확인할 수있음

========================================================================================
backend : .py  
frontend : gpt  
user : gpt와의 상호교환를 통한 calender와 그 외의 정보 획득

user의 시나리오 
1) 00대회에 나가기로 함
2) gpt를 통해 '00대회' 일정 추가 (추가적으로 세부설명, 장소, 사이트 링크 등을 저장할 수 있음)
3) 00대회에 대한 세부내용, 위치, 교통편 등의 정보가 부족함
4) gpt를 통해 00대회에 위치, 교통편등의 정보의 얻을 수 있음
=========================================================================================

#### 선행 요건
- 본인 계정의 Calendar API 발급
    -  **"Google Developers Console"** 사이트를 통해 api 생성
    -  생성한 후 JSON 파일로 다운로드
    -  다운로드 한 파일의 이름을 **credentials.json** 으로 변경후 프로젝트에 위치하기
    -  (만약 opensoure 프로젝트가 있다면, 프로젝트 안에 .json과 .py 가 같은 위치에 있어야 함)

#### 서버 실행

1. pip install -r reguirements.txt
2. credential.json과 calendar.py 위치 확인
3. python calendar.py
4. it --port 5000 --subdomain **your-creative-proxy-address**
your-creative-proxy-address는 본인이 명명한 address주소로 설정

5. subdomain your-creative-poxy-address/read_events 로 calendar의 일정을 잘 읽어왔는지 확인
6. 'custom gpt 만들기'로 들어가서 이름, 설명, 지침등을 자유롭게 입력
7. 단, 지침(nstructions)에는 **instructions.md**를 입력
8. '새 작업 만들기'를 클릭해 스키마 입력
9. 스키마의 내용으로는 server. path, parameter등이 추가되어야 함
ex. 

10. 그 후 프롬프트를 통해 gpt에게 원하는 말투,형식을 지정할 수 있음 


#### 세부 이미지
- your-creative-proxy-address을 cal-api로 설정 
/read_events 를 통해 일정을 잘 읽어왔는지 확인(start date, end date, summary, location등등)
<img width="60%" src="https://github.com/jii1n/opensource_project/assets/170122957/0fc3c08f-5700-48e1-94e0-035ae20ac930"/>
![image](https://github.com/jii1n/opensource_project/assets/170122957/0fc3c08f-5700-48e1-94e0-035ae20ac930)

- custom gpt 스키마의 내용
ex)
![image](https://github.com/jii1n/opensource_project/assets/170122957/9215f340-cb3a-4112-ac5a-2dea174707f7)



### 캘린더 gpt 완성
- 관련된 이미지는 **result.md** 참고 
