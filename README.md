# lms cralwer

lms를 쉽게 저장하기 위한 크롤러

lms는 앞으로 여러분의 인공지능 공부에 큰 도움이 될 것입니다. 여러분들이 수강을 완료하면, lms 서비스는 종료될 것이기 떄문에 내용을 저장할 필요가 있습니다!

이 레파지토리는 다음이 포함되어 있습니다.

```bash
.
├── README.md # 사용법이 적힌 파일
├── config.py # 유저 정보와 사이트 정보를 담은 파일
├── cralwer.py # 데이터 수집 관련 파일
├── driver.py # driver를 통한 웹 이동용 파일
├── main.py # 실행시킬 파일
├── save.py # 내용 저장 관련 파일
└── settings.py # Chrome 기반 driver 세팅 관련 파일

0 directories, 7 files
```

각 파일에 대한 간단한 설명과 실행법을 나열합니다.

## 목차

***

- [설치](#설치목차)
  - [chrome 설치](#chrome-설치목차)
  - [config 파일 수정](#config-파일-수정목차)
- [사용법](#사용법목차)

## [설치](#목차)

***

가장 먼저 설치할 컴퓨터에 git을 복제합니다.

```bash
git clone https://github.com/LBR56/lms_cralwer.git
```

이 프로젝트는 python 3.8.9 버전을 사용하였습니다. 또 필요한 라이브러리는 requirements.txt에 기제되어 있습니다.

그럼으로 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### [chrome 설치](#목차)

***

이 프로젝트는 여러 브라우저 중 크롬에 중점적으로 맞췄습니다. 그럼으로 chrome 브라우저가 설치되어 있어야 합니다.

[크롬 다운로드 링크](https://www.google.com/intl/ko_kr/chrome/)를 통해 설치해 주시길 바랍니다.

### [config 파일 수정](#목차)

***

기본적으로 config 파일은 다음의 모습을 가지고 있습니다.

```python
USER_INFO = {
  'id':'아이디', # 실제 lms 아이디
  'pw':'비민번호' # 실제 lms 비밀번호
}

SITE_URL = 'lms 사이트 url' # lms 사이트 링크
```

다음 각 요소를 변경해주지 않는다면, 원치 않는 사이트로 들어갈 위험이 있습니다.

## [사용법](#목차)

***

1. 먼저 저장하고 싶은 내용을 미리 lms에서 선택하여 환경을 연결해줍니다.
2. ```python main.py```를 실행합니다.

```bash
python main.py
```
