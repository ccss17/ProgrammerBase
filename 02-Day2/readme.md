# Day 2

GBC 첫번째 과정 **Programmer Base** 의 2일차 내용입니다.

---

# 리눅스 교재 

오늘 내용을 수월하게 이해하기 위해서는 교재의 **Chapter 04** 내용을 먼저 실습해보아야 합니다.

교재에서 다음 분량을 읽고 우분투 도커 컨테이너에서 실습해주세요. 사실 너무 열심히 읽지 않아도 됩니다. 즉, 막 외우려고 애쓰지 않아도 된다는 뜻입니다. 이런게 있구나 하면서 실습하면서 술술 넘기세요. 그리고 하다가 실습하기 힘든 부분이 있다면 그냥 너무 걱정하지 말고 넘겨도 됩니다. 

**(옵션)** 라고 되어있는 파트는 시간절약을 위해 아예 안봐도 됩니다.

## Chapter 04

- **186p ~ 203p 읽고 실습하기**

  - 셸의 기능과 종류, 셸 기본 사용법, 입출력 방향 바꾸기

- **206p ~ 217p 읽고 실습하기**

  - 배시 셸 환경 설정, 에일리어스와 히스토리

- **220p ~ 224p 읽고 실습하기**

  - **(옵션)** 프롬프트 설정

- **225p ~ 229p 읽고 실습하기**

  - 환경 설정 파일

---

**다음 내용을 학습하세요.**

# Stackoverflow Survey

- [Stackoverflow Survey](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#stackoverflow-survey)

  - [개발자들이 가장 사랑하는 플랫폼](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%B4-%EA%B0%80%EC%9E%A5-%EC%82%AC%EB%9E%91%ED%95%98%EB%8A%94-%ED%94%8C%EB%9E%AB%ED%8F%BC)

  - [개발자들이 가장 사랑하는 개발환경](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%B4-%EA%B0%80%EC%9E%A5-%EC%82%AC%EB%9E%91%ED%95%98%EB%8A%94-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD)

위 내용을 학습하셨다면 전세계 개발자의 추세를 나름 볼 수 있었을 것입니다. 그러면 이 추세를 따라가봅시다! 리눅스와 도커는 계속 배우고 있으니까 **VSCode** 개발환경만 알아보면 되겠네요. 하지만 그러기 전에 **Git** 과 **Github** 을 가볍게 알아보겠습니다. 

# Git

- [Git](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-1)

  - [Git 설치](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EC%84%A4%EC%B9%98)

    - [Windows 설치](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#windows-%EC%84%A4%EC%B9%98)

    - [MacOS 설치](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#macos-%EC%84%A4%EC%B9%98)

    - [우분투 도커 컨테이너에서 git 초기 설정](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%9A%B0%EB%B6%84%ED%88%AC-%EB%8F%84%EC%BB%A4-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%97%90%EC%84%9C-git-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95)

  - [git 이 파일을 관리하는 상태](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EC%9D%B4-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94-%EC%83%81%ED%83%9C)

    - [git 레포지토리 생성하기 (untracked 상태)](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0-untracked-%EC%83%81%ED%83%9C)

    - [파일 생성하고 스테이징하기 (untracked 상태 &rarr; staged 상태)](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%ED%8C%8C%EC%9D%BC-%EC%83%9D%EC%84%B1%ED%95%98%EA%B3%A0-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%95%ED%95%98%EA%B8%B0-untracked-%EC%83%81%ED%83%9C--staged-%EC%83%81%ED%83%9C)

    - [커밋해서 하나의 버전으로 만들기 (staged 상태 &rarr; committed 상태)](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%BB%A4%EB%B0%8B%ED%95%B4%EC%84%9C-%ED%95%98%EB%82%98%EC%9D%98-%EB%B2%84%EC%A0%84%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-staged-%EC%83%81%ED%83%9C--committed-%EC%83%81%ED%83%9C)

    - [변경된 파일 커밋하기 (modified 상태 &rarr; staged 상태 &rarr; committed 상태)](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B3%80%EA%B2%BD%EB%90%9C-%ED%8C%8C%EC%9D%BC-%EC%BB%A4%EB%B0%8B%ED%95%98%EA%B8%B0-modified-%EC%83%81%ED%83%9C--staged-%EC%83%81%ED%83%9C--committed-%EC%83%81%ED%83%9C)

    - [커밋 기록 보기 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%BB%A4%EB%B0%8B-%EA%B8%B0%EB%A1%9D-%EB%B3%B4%EA%B8%B0)

# Github

- [Github](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github)

  - [Github 가입 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github-%EA%B0%80%EC%9E%85)

  - [Github 레포지토리 생성](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1)

  - [git 에서 레포지토리 공유](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EC%97%90%EC%84%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B3%B5%EC%9C%A0)

  - [원격 레포지토리 가져오고 수정하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B3%A0-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0)

  - [수정된 원격 레포지토리로부터 업데이트하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%88%98%EC%A0%95%EB%90%9C-%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%ED%95%98%EA%B8%B0)

# VSCode

- [VSCode](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-1)

  - [VSCode 설치](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-%EC%84%A4%EC%B9%98)

  - [VSCode 간단 사용법 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-%EA%B0%84%EB%8B%A8-%EC%82%AC%EC%9A%A9%EB%B2%95)

    - [로컬에서 레포지토리 만들기 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0)

    - [새 파일 만들고 저장하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%83%88-%ED%8C%8C%EC%9D%BC-%EB%A7%8C%EB%93%A4%EA%B3%A0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)

    - [변경된 파일 스테이징하고 커밋하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%B3%80%EA%B2%BD%EB%90%9C-%ED%8C%8C%EC%9D%BC-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%95%ED%95%98%EA%B3%A0-%EC%BB%A4%EB%B0%8B%ED%95%98%EA%B8%B0)

    - [원격 레포지토리 등록하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0)

    - [원격 레포지토리로 공유하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C-%EA%B3%B5%EC%9C%A0%ED%95%98%EA%B8%B0)

    - [원격 레포지토리 가져오고 수정하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B3%A0-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0)

    - [원격 레포지토리로부터 업데이트하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%ED%95%98%EA%B8%B0)

  - [더 빨라진 개발환경](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD)

    - [파일 열기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%8C%8C%EC%9D%BC-%EC%97%B4%EA%B8%B0)

    - [파일 닫기 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%8C%8C%EC%9D%BC-%EB%8B%AB%EA%B8%B0)

    - [열린 파일 포커싱 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%97%B4%EB%A6%B0-%ED%8C%8C%EC%9D%BC-%ED%8F%AC%EC%BB%A4%EC%8B%B1)

    - [화면 옮기기 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%99%94%EB%A9%B4-%EC%98%AE%EA%B8%B0%EA%B8%B0)

    - [분할된 화면 포커싱 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%B6%84%ED%95%A0%EB%90%9C-%ED%99%94%EB%A9%B4-%ED%8F%AC%EC%BB%A4%EC%8B%B1)

    - [화면 레이아웃 변경](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%99%94%EB%A9%B4-%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83-%EB%B3%80%EA%B2%BD)

    - [화면 복제](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%99%94%EB%A9%B4-%EB%B3%B5%EC%A0%9C)

# Markdown 

- [Markdown ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#markdown-1)

  - [**VSCode** 의 **Markdown** 미리보기](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#vscode-%EC%9D%98-markdown-%EB%AF%B8%EB%A6%AC%EB%B3%B4%EA%B8%B0)

  - [제목 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%A0%9C%EB%AA%A9)

  - [텍스트 포맷팅 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%8F%AC%EB%A7%B7%ED%8C%85)

  - [아이템과 순서](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%95%84%EC%9D%B4%ED%85%9C%EA%B3%BC-%EC%88%9C%EC%84%9C)

  - [링크와 사진](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EB%A7%81%ED%81%AC%EC%99%80-%EC%82%AC%EC%A7%84)

  - [코드 입력 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%BD%94%EB%93%9C-%EC%9E%85%EB%A0%A5)

  - [표 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%ED%91%9C)

  - [분할선 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EB%B6%84%ED%95%A0%EC%84%A0)

  - [README.md ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#readmemd)

---

# 과제 

- [hw2.md](hw2.md) 에 과제 가이드가 나와있으니 따라주시면 됩니다. 

- 과제를 발표를 하며 설명할 수 있어야 합니다. 
