### Custom GPT Tutorial

#### 요약
- .py의 역활
  - calendar에 저장된 일정을 읽어와 json 형식으로 변환
  - 직접 본인의 calendar로 가서 '일정 확인','추가', '삭제'가 아닌 endpoint를 이용해 gpt와 calendar의 데이터 교환 가능
  -> gpt와의 상호작용을 통해 gpt상에서 calendar의 내용을 확인, 추가, 삭제할 수 있음

- 'explore gpts'사이트의 cutstom gpt 
  - 나만의 custom gpt 생성 가능
  - .py를 통해 만들어진 endpoint를 입력해 gpt에게 데이터(일정)을 주고받음
    -> custom gpt 사용자는 calendar로 직접 접근하지 않으면서 gpt상에서 일정을 확인할 수있음

========================================================================================
backend : .py  
frontend : gpt  
user : gpt와의 상호교환를 통한 calender와 그 외의 정보 획득

user의 이용 과정
1) 00대회에 나가기로 함
2) gpt를 통해 '00대회' 일정 추가 (추가적으로 세부설명, 장소, 사이트 링크 등을 저장할 수 있음)
3) 00대회에 대한 세부내용, 위치, 교통편 등의 정보가 부족함
4) gpt를 통해 00대회에 위치, 교통편등의 정보의 얻을 수 있음 

#### 선행 요건
- 본인 계정의 Calendar API 발급
    -  "Google Developers Console" 사이트를 통해 api 생성
    -  생성한 후 JSON 파일로 다운로드
    -  다운로드 한 파일의 이름을 credentials.json으로 변경후 프로젝트에 위치하기
    -  (만약 opensoure 프로젝트가 있다면, 프로젝트 안에 .json과 .pyp 가 같은 위치에 있어야 함)

#### 서버 실행


