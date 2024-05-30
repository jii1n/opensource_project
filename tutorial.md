### Custom GPT Tutorial
요약.
- .py의 역활:
  1) calendar에 저장된 일정을 읽어와 json 형식으로 변환
  2) 직접 본인의 calendar로 가서 '일정 확인','추가', '삭제'가 아닌 endpoint를 이용해 gpt와 calendar의 데이터 교환 가능
     -> 즉, gpt와의 상호작용을 통해 gpt상에서 calendar의 내용을 확인, 추가, 삭제할 수 있음 


https://chatgpt.com/gpts?oai-dm=1

#### 선행 요건
- 본인 계정의 Calendar API 발급
    -  "Google Developers Console" 사이트를 통해 api 생성
    -  생성한 후 JSON 파일로 다운로드
    -  다운로드 한 파일의 이름을 credentials.json으로 변경후 프로젝트에 위치하기
    -  (만약 opensoure 프로젝트가 있다면, 프로젝트 안에 .json과 .pyp 가 같은 위치에 있어야 함)

#### 서버 실행



