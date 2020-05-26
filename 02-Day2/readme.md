# Day 2

GBC 첫번째 과정 **Programmer Base** 의 2일차 내용입니다.

---

# Table of Contents

- [리눅스 교재 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B5%90%EC%9E%AC)

- [Stackoverflow Survey](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#stackoverflow-survey)

  - [개발자들이 가장 사랑하는 플랫폼](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%B4-%EA%B0%80%EC%9E%A5-%EC%82%AC%EB%9E%91%ED%95%98%EB%8A%94-%ED%94%8C%EB%9E%AB%ED%8F%BC)

  - [개발자들이 가장 사랑하는 개발환경](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%9D%B4-%EA%B0%80%EC%9E%A5-%EC%82%AC%EB%9E%91%ED%95%98%EB%8A%94-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD)

- [Git](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#git)

  - [Git 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#git-%EC%84%A4%EC%B9%98)

    - [Windows 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#windows-%EC%84%A4%EC%B9%98)

    - [MacOS 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#macos-%EC%84%A4%EC%B9%98)

    - [우분투 도커 컨테이너에서 git 초기 설정](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9A%B0%EB%B6%84%ED%88%AC-%EB%8F%84%EC%BB%A4-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%97%90%EC%84%9C-git-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95)

  - [git 이 파일을 관리하는 상태](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#git-%EC%9D%B4-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EA%B4%80%EB%A6%AC%ED%95%98%EB%8A%94-%EC%83%81%ED%83%9C)

    - [git 레포지토리 생성하기 (untracked 상태)](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#git-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0-untracked-%EC%83%81%ED%83%9C)

    - [파일 생성하고 스테이징하기 (untracked 상태 &rarr; staged 상태)](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%8C%8C%EC%9D%BC-%EC%83%9D%EC%84%B1%ED%95%98%EA%B3%A0-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%95%ED%95%98%EA%B8%B0-untracked-%EC%83%81%ED%83%9C--staged-%EC%83%81%ED%83%9C)

    - [커밋해서 하나의 버전으로 만들기 (staged 상태 &rarr; committed 상태)](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%BB%A4%EB%B0%8B%ED%95%B4%EC%84%9C-%ED%95%98%EB%82%98%EC%9D%98-%EB%B2%84%EC%A0%84%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-staged-%EC%83%81%ED%83%9C--committed-%EC%83%81%ED%83%9C)

    - [변경된 파일 커밋하기 (modified 상태 &rarr; staged 상태 &rarr; committed 상태)](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%B3%80%EA%B2%BD%EB%90%9C-%ED%8C%8C%EC%9D%BC-%EC%BB%A4%EB%B0%8B%ED%95%98%EA%B8%B0-modified-%EC%83%81%ED%83%9C--staged-%EC%83%81%ED%83%9C--committed-%EC%83%81%ED%83%9C)

    - [커밋 기록 보기 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%BB%A4%EB%B0%8B-%EA%B8%B0%EB%A1%9D-%EB%B3%B4%EA%B8%B0)

- [Github](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#github)

  - [Github 가입 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#github-%EA%B0%80%EC%9E%85)

  - [Github 레포지토리 생성](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#github-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1)

  - [git 에서 레포지토리 공유](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#git-%EC%97%90%EC%84%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B3%B5%EC%9C%A0)

  - [원격 레포지토리 가져오고 수정하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B3%A0-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0)

  - [수정된 원격 레포지토리로부터 업데이트하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%88%98%EC%A0%95%EB%90%9C-%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%ED%95%98%EA%B8%B0)

- [VSCode](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#vscode)

  - [VSCode 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#vscode-%EC%84%A4%EC%B9%98)

    - [Windows 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#windows-%EC%84%A4%EC%B9%98-1)

    - [MacOS 설치](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#macos-%EC%84%A4%EC%B9%98-1)

  - [VSCode 간단 사용법 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#vscode-%EA%B0%84%EB%8B%A8-%EC%82%AC%EC%9A%A9%EB%B2%95)

    - [로컬에서 레포지토리 만들기 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0)

    - [새 파일 만들고 저장하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%83%88-%ED%8C%8C%EC%9D%BC-%EB%A7%8C%EB%93%A4%EA%B3%A0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)

    - [변경된 파일 스테이징하고 커밋하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%B3%80%EA%B2%BD%EB%90%9C-%ED%8C%8C%EC%9D%BC-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%95%ED%95%98%EA%B3%A0-%EC%BB%A4%EB%B0%8B%ED%95%98%EA%B8%B0)

    - [원격 레포지토리 등록하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0)

    - [원격 레포지토리로 공유하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C-%EA%B3%B5%EC%9C%A0%ED%95%98%EA%B8%B0)

    - [원격 레포지토리 가져오고 수정하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B3%A0-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0-1)

    - [원격 레포지토리로부터 업데이트하기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%ED%95%98%EA%B8%B0)

  - [더 빨라진 개발환경](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD)

    - [파일 열기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%8C%8C%EC%9D%BC-%EC%97%B4%EA%B8%B0)

    - [파일 닫기 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%8C%8C%EC%9D%BC-%EB%8B%AB%EA%B8%B0)

    - [열린 파일 포커싱 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%97%B4%EB%A6%B0-%ED%8C%8C%EC%9D%BC-%ED%8F%AC%EC%BB%A4%EC%8B%B1)

    - [화면 옮기기 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%99%94%EB%A9%B4-%EC%98%AE%EA%B8%B0%EA%B8%B0)

    - [분할된 화면 포커싱 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%B6%84%ED%95%A0%EB%90%9C-%ED%99%94%EB%A9%B4-%ED%8F%AC%EC%BB%A4%EC%8B%B1)

    - [화면 레이아웃 변경](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%99%94%EB%A9%B4-%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83-%EB%B3%80%EA%B2%BD)

    - [화면 복제](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%99%94%EB%A9%B4-%EB%B3%B5%EC%A0%9C)

- [Markdown ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#markdown)

  - [**VSCode** 의 **Markdown** 미리보기](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#vscode-%EC%9D%98-markdown-%EB%AF%B8%EB%A6%AC%EB%B3%B4%EA%B8%B0)

  - [제목 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%A0%9C%EB%AA%A9)

  - [텍스트 포맷팅 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%8F%AC%EB%A7%B7%ED%8C%85)

  - [아이템과 순서](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%95%84%EC%9D%B4%ED%85%9C%EA%B3%BC-%EC%88%9C%EC%84%9C)

  - [링크와 사진](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%A7%81%ED%81%AC%EC%99%80-%EC%82%AC%EC%A7%84)

  - [코드 입력 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EC%BD%94%EB%93%9C-%EC%9E%85%EB%A0%A5)

  - [표 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%ED%91%9C)

  - [분할선 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EB%B6%84%ED%95%A0%EC%84%A0)

  - [README.md ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#readmemd)

- [과제 ](https://github.com/ccss17/ProgrammerBase/tree/master/02-Day2#%EA%B3%BC%EC%A0%9C)

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

# Stackoverflow Survey

개발 공부를 하다보면 [스택오버플로우](https://stackoverflow.com/)의 답변을 한번쯤 참고해보셨을텐데요. 전세계 개발자가 바로 이 사이트를 통해 개발 관련 질문을 올리고 정보를 공유하고 있습니다. 

> 이곳에서 질문에 대한 답변이 사용자들에게 채택되면 점수가 오르는데, 얼마나 공신력이 있는 곳이면 상위 1% 의 스택오버플로우 유저는 구글 입사가 프리패스된다는 말도 들은적이 있네요.

이 커뮤니티는 매년 전세계 개발자를 대상으로 설문조사를 하는데 이 서베이를 보면 트렌디한 기술이 뭔지, 나만 모르고 있던 좋은 기술이 뭔지 알 수 있습니다. 다음 링크를 통해 2019년 설문조사에 들어가보세요.

https://insights.stackoverflow.com/survey/2019

왼쪽 카테고리를 보면 여러 항목에 대한 설문조사를 한 것이 보이는데 다음과 같이 **Technology** 분야가 메인 디쉬라고 볼 수 있을 것 같습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80893957-ba6eb780-8d11-11ea-86c0-3570463f1a79.png" width="30%" height="auto"> </div>

나머지 항목은 궁금하시면 더 살펴보셔도 되고 지금 이 시간에는 이 설문조사를 통해 전세계에서 가장 핫한 플랫폼과 에디터가 뭔지 알아보겠습니다.

## 개발자들이 가장 사랑하는 플랫폼

설문조사에서 **Platforms** 항목을 찾아보면 다음과 같은 설문결과를 볼 수 있습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80894214-1e927b00-8d14-11ea-9a86-81051ab2c8c8.png" width="40%" height="auto"> </div>

개발자들에게 인기있는 플랫폼 1위는 **53.3%** 로 리눅스네요. 어제 배웠던 도커는 3위를 차지했는데 이는 스택오버플로우가 2019년에 처음으로 도커에 대한 설문조사를 한 결과라고 하니까 개발자들이 얼마나 도커에 주목하고 있는지 감이 오시나요? 전세계 개발자들이 이런 플랫폼과 기술들에 왜 사랑에 빠졌는지 몰라서는 안되기 때문에 꼭 배워봐야 합니다. 

## 개발자들이 가장 사랑하는 개발환경

이제 **Most Popular Development Environments** 항목을 보면서 개발자들이 어떤 개발환경을 가장 좋아하는지 알아보겠습니다.

<div align="center">

<img src="https://user-images.githubusercontent.com/16812446/80894553-d163d880-8d16-11ea-854f-8f74fb11607f.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895772-8c926e80-8d23-11ea-92b2-df4cfdd80085.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895968-2528ee80-8d24-11ea-8bf5-070d5f503269.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895984-425dbd00-8d24-11ea-8d9d-dfdd6b7d09d1.png" width="40%" height="auto">

</div>



설문조사는 **"모든 개발자", "웹 개발자", "스마트폰 어플 개발자", "데브 옵스"** 를 대상으로 진행되었는데 "스마트폰 어플 개발자" 를 제외하고는 **Visual Studio Code** 즉, **VSCode** 가 1위를 차지했습니다. 심지어 "스마트폰 어플 개발자" 에서도 **VSCode** 가 Android Studio 와 매우 미세한 차이로 2위를 차지했으니, 전세계 개발자들이 **VSCode** 가 제공하는 개발환경에 얼마나 푹 빠져버렸는지 알 수 있겠죠?

---

그러면 이 전세계의 추세를 따라가봅시다! 그런데 리눅스와 도커는 계속 배우고 있으니까 **VSCode** 개발환경만 알아보면 되겠네요. 하지만 그러기 전에 **Git** 과 **Github** 을 가볍게 알아보겠습니다. 

# Git

> 참고 : https://git-scm.com/book/en/v2

코딩을 막 배우기 시작하면 종종 카톡이나 메일에 소스코드를 백업 하곤 합니다. 하지만 이 방식에는 몇 가지 단점이 있습니다. 먼저 소스코드의 저장장소가 매우 산발적이고 일관성이 없어서 매번 찾기가 힘듭니다. 그리고 소스코드의 변화과정을 제대로 이해하기 힘듭니다. 만약 백업하는 것도 잊어버리고 백업을 하지 않았다가 실수로 소스코드를 삭제해버린다면 복구할 수 있는 방법이 전혀 없습니다.

> 이런 문제는 규모가 큰 단체 프로젝트에서 더 심각해집니다. 누가 무엇을 고쳤는지, 소스코드 저장소가 어디에 있는지, 만약 누가 실수로 소스코드를 지워버렸을 때 복구를 할 수 없을 때 기업은 실질적인 금전적인 피해를 받게 됩니다. 

이 문제를 해결하기 위해 나온 것이 **버전 컨트롤 시스템(Version Control System)** 입니다. 줄여서 **VCS** 는 단어 그대로 **"프로젝트의 버전을 손쉽게 다룰 수 있게 해주는 시스템"** 입니다. VCS 에는 여러 종류가 있지만 이제 우리는 그 중에서 가장 많이 사용되는 VCS 인 `git` 을 간단하게 알아보겠습니다. `git` 을 익히면 제가 위에서 설명한 문제들이 다 해결되는 것입니다!

`git` 의 자세한 설명과 의미를 공부하기 위해서는 

https://git-scm.com/book/en/v2

https://git-scm.com/book/ko/v2

를 참고해주세요. 

>그리고 방학 때나 휴학을 했을 때 시간이 남으니까 `git` 의 `Branching` 기능까지 익혀두시길 **강력하게** 추천합니다. 왜냐면 여러분이 개발자로 살아가는 이상 **어차피 언젠가는 `git Branching` 기능까지 알아야만 하기 때문**입니다. 

- **`git` : 가장 인기있고 자주 사용되는 VCS 이다.**

  - `git` 은 파일을 **untracked 상태, modified 상태, staged 상태, committed 상태**로 관리한다.

## Git 설치

> 만약  컴퓨터 운영체제로 **Linux** 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 `git` 를 설치할 수 있다고 믿습니다. 

### Windows 설치

1. [이 링크](https://git-scm.com/download/win) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

2. `git` 을 설치한 후 가장 처음 해야 할 일은 초기 설정입니다. `git` 이 잘 설치되었다면 **Git Bash** 를 실행한 다음 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

    ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ git config --global user.name "<NAME>"
    $ git config --global user.email "<EMAIL>"
    ```

### MacOS 설치

1. [이 링크](https://git-scm.com/download/mac) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

2. `git` 을 설치한 후 가장 처음 해야 할 일은 초기 설정입니다. 터미널을 열어서 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

    ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ git config --global user.name "<NAME>"
    $ git config --global user.email "<EMAIL>"
    ```

### 우분투 도커 컨테이너에서 git 초기 설정

우분투 도커 컨테이너에서 접속하셔서 마찬가지로 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

> 종료된 컨테이너에 다시 접속하는 명령어는 `docker ps -a` 로 종료된 컨테이너의 아이디를 확인하고 `docker start -ai <ID>` 를 입력하는 것이었습니다. 그냥 완전히 새로운 컨테이너를 시작하는 명령어는 `docker run -it ccss17/ubuntu` 였습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git config --global user.name "<NAME>"
$ git config --global user.email "<EMAIL>"
```

## git 이 파일을 관리하는 상태

`git` 은 다음과 같은 상태로 파일들을 관리합니다. 이 상태들의 의미와 원리를 이해하면 **`git` 을 어느정도 이해했다** 고 볼 수 있습니다. 

- **untracked 상태 : `git` 이 변경사항을 추적하지 않는 파일이다.**

- **modified 상태 : 파일을 변경했지만 아직 스테이징되지 않은 상태이다.**

- **staged 상태 : 변경된 파일을 커밋이 될 리스트에 포함시킨 상태이다.**

- **committed 상태 : `git` 데이터베이스에 하나의 버전으로 저장된 상태이다.**

아직은 이게 뭔 소린지 감이 안오네요. `git` 을 실제로 실습해보면서 이 상태들이 어떤 건지 알아보겠습니다. 먼저 우분투 컨테이너에 접속한 상태에서 다음 명령어들을 실행하세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ mkdir git-test      # 디렉토리 생성
$ cd git-test
```

### git 레포지토리 생성하기 (untracked 상태)

그리고 다음 명령어를 실행해보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git init
```

이 명령어는 현재 디렉토리를 `git` 레포지토리로 만들고 `git` 이 파일의 변경을 추적하게 합니다.

- **`git init` : 디렉토리를 `git` 레포지토리로 만들어 디렉토리 내의 파일을 `git` 이 추적하게 한다.**

### 파일 생성하고 스테이징하기 (untracked 상태 &rarr; staged 상태)

이제 프로젝트를 위하여 `test.txt` 라는 파일을 만들었다고 하고 다음 명령어를 입력하세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ touch test.txt
$ git status
...
Untracked files:
	test.txt
...
```

`git status` 로 현재 `git` 레포지토리의 상태, 즉 디렉토리 내 파일들이 **untracked 상태, modified 상태, staged 상태, committed 상태** 중 어떤 상태인지 알아볼 수 있습니다.

- **`git status` : `git` 레포지토리의 상태를 출력한다.**

  - `-s` 옵션을 붙히면 간단하게 출력한다.

실행 결과가 위와 같은데 금방 만든 `test.txt` 가 `Untracked files` 인 걸로 보아 **untracked 상태**라는 것을 알 수 있습니다. 이 상태에 있는 파일들은 `git` 이 변경사항을 추적하면서 버전에 포함시키지 않습니다.

`git` 이 이 파일을 추적하고 버전에 포함시키도록 하기 위해 다음 명령어를 실행해주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git add test.txt
$ git status
...
Changes to be committed:
  ...
	new file:   test.txt
```

이로써 `test.txt` 가 `Changes to be committed`, 즉 **staged 상태**가 되었습니다. **staged 상태**는 이렇게 커밋이 되기로 예정된 파일을 의미합니다. 그리고 스테이징한다는 것은 파일을 **staged 상태**로 만든다는 것이죠.

- **`git add <FILE>` : `<FILE>` 을 스테이징한다.**

  - 즉, 파일을 커밋 예정 상태(**staged 상태**)로 만든다.

  - `git add .` 로 파일명을 일일이 입력하지 않고 모든 파일을 자동으로 `staged` 상태로 만들 수 있다.

### 커밋해서 하나의 버전으로 만들기 (staged 상태 &rarr; committed 상태)

이제 스테이징된 파일들을 커밋해서 하나의 버전으로 만들기만 하면 됩니다!

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git commit -m "my first commit"
$ git status
On branch master
nothing to commit, working tree clean
```

그러면 커밋할 때 당시의 레포지토리의 파일들이 하나의 스냅샷으로 찍혀서 하나의 버전이 되었습니다. 

- **`git commit` : 스테이징된 파일들을 커밋하여 하나의 버전으로 만들어 `git` 데이터베이스에 저장한다.**

  - `git commit -m <MESSAGE>` 로 커밋 메시지를 바로 입력할 수 있다.

이렇게 커밋된 스냅샷은 `git` 데이터베이스에 안전하고 일관되게 보관됩니다. 그래서 언제든지 이 커밋들을 열람할 수 있고 복원도 할 수 있고 그때 당시의 파일들이 어떤 상태였는지도 확인할 수 있습니다.

> 다만, 그렇기 때문에 커밋 메시지를 상당히 의미있게 작성하는 것이 중요합니다. 왜냐하면 나중에 커밋들을 살펴볼 때 커밋 메시지에 의존하여 이때 당시의 프로젝트가 어떤 기능이 추가되고 변경되었는지 판단할 수 있기 때문이죠.

### 변경된 파일 커밋하기 (modified 상태 &rarr; staged 상태 &rarr; committed 상태)

코딩을 하다보면 파일을 변경하지 않을 수 없겠죠? 그렇게 새로운 기능이나 변경사항을 추가하면 또 다시 커밋해서 하나의 버전으로 만들어두세요.

> 커밋은 레포지토리에 유의미한 크기의 기능이 추가되었을 때, 또는 레포지토리에 유의미한 변경이 이루어졌을 때 하는 것이 좋지만 처음에는 일단 그냥 "커밋을 많이 하는 것이 좋다" 라는 마인드로 `git` 을 사용해보세요. 그리고 이곳에서 배우진 않지만 `Branching` 기능도 일부러 자주자주 써서 익숙해져보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ echo "My test memo" > test.txt
$ cat test.txt
My test memo
$ git add .
$ git commit -m "My memo file"
```

위 명령어를 입력함으로써 `test.txt` 에 데이터를 추가하고 스테이징한 후 커밋하여 또 하나의 버전으로 만들어보세요.

### 커밋 기록 보기 

프로그램을 개발하면서 무언가 잘못되었을 때, 또는 프로젝트가 어떻게 변경되었는지 이해하고 싶을 때 커밋 기록을 살펴볼 수 있습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git log
commit 9a58815ccb87fb516feb22e02a55232cf45da7d5 (HEAD -> master)
Author: awef <awef@naver.com>
Date:   Sun May 3 09:48:23 2020 +0000

    My memo file
```

저는 위와 같은 결과가 나오네요. 초기 설정시 입력하였던 이름과 이메일이 커밋 기록에 남기 때문에 누가 변경한 시점부터 프로젝트가 잘못되었는지, 또는 잘되었는지 확인하는 용도로도 사용할 수 있어서 편리합니다.

- **`git log` : 커밋 기록을 출력한다.**

  - `git log -2` : 최근 커밋 `2` 개를 보여준다. 

  - `git log -p` : 변경 사항도 출력하면서 커밋 기록을 보여준다.

---

# Github

여러분이 지금 보고 있는 웹사이트인 **Github** 는 `git` 레포지토리를 다른 사람과 공유할 수 있는 플랫폼입니다. 이곳을 통하여 협업을 할 수 있기도 하고 자신이 관심있는 프로그램들이 무엇인지 알려줄 수도 있습니다.

> 최근에는 **Github** 에 있는 그 사람의 레포지토리들을 포트폴리오로 취급하고 능력을 가늠해보기도 한다니까 **Github** 에 레포지토리를 많이 공유하는 것이 좋을 것 같습니다.

## Github 가입 

**Github** 에 가입되어 있지 않으신 분들은 먼저 https://github.com/ 에서 가입을 해주세요.

## Github 레포지토리 생성

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/80912176-21be5300-8d76-11ea-8098-4ca30a560c4c.PNG" >
</div>

가입한 다음에는 왼쪽 위에서 초록색 **"New"** 버튼을 찾아서 누르면 레포지토리 생성 창으로 넘어갑니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/80912222-706bed00-8d76-11ea-8c25-b90e9bed11a4.PNG" >
</div>

그러고 레포지토리 이름을 그냥 **"git-test"** 라고 하고 테스트용 레포지토리니까 다른 사람들이 못 보게 **"Private"** 에 체크를 하고 아래에 **"Create repository"** 버튼을 눌러 생성을 완료해줍시다.

## git 에서 레포지토리 공유

이제 좀 전에 우분투 컨테이너에서 만들었던 레포지토리를 여기에 공유해보겠습니다. 먼저 다음 명령어에서 `<USER>` 를 자신의 아이디로 치환하여 입력함으로써 원격 레포지토리를 추가해주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git remote add origin https://github.com/<USER>/git-test
```

- **`git remote add <NAME> <URL>` : `<NAME>` 이라는 별칭으로 `<URL>` 의 원격 레포지토리를 등록한다.**

  - `git remote rm <NAME>` 으로 원격 레포지토리를 삭제할 수 있다.

  - `git remote rename <NAME> <NEW>` 으로 원격 레포지토리의 별칭을 수정할 수 있다.

그러고 나면 단순히 다음의 `git push` 명령어를 입력하는 것으로 레포지토리를 공유할 수 있습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git push -u origin master
```

- **`git push <NAME> <BRANCH>` : `<NAME>` 의 원격 레포지토리로 변경사항을 업데이트한다.**

  - `git push origin master` 로도 업데이트 할 수 있다.

## 원격 레포지토리 가져오고 수정하기

이제 다른 컴퓨터에서 원격 레포지토리를 가져와서 작업하거나, 다른 사람의 레포지토리를 가져와서 작업하고 싶은 상황이라고 하겠습니다. 그러면 `<USER>` 를 자신의 아이디로 치환하여 단순히 다음 명령어를 입력하면 됩니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd        # 홈 디렉토리로 이동
$ git clone https://github.com/<USER>/git-test git-test-remote
$ cd git-test-remote
```

그러면 홈 디렉토리 밑에 `git-test-remote` 라는 디렉토리가 생기고 들어가보면 `git push` 로 공유했던 프로젝트가 그대로 가져와졌다는 것을 알 수 있습니다.

- **`git clone <URL> <NAME>` : `<URL>` 의 원격 레포지토리를 가져와서 `<NAME>` 디렉토리에 복제한다.**

  - 만약 디렉토리 이름 `<NAME>` 을 생략하고 `git clone <URL>` 으로 입력하면 원격 레포지토리의 이름으로 디렉토리가 자동 생성된다.

이제 원격 레포지토리가 복제되었으니 작업을 하고 업데이트해보겠습니다. 사실 아까와 다를 것이 없습니다! 다음 명령어를 입력해보세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ echo "very important message" > test.txt
$ git add .
$ git commit -m "very important file.."
$ git push origin master
```

## 수정된 원격 레포지토리로부터 업데이트하기

이렇게 원격 레포지토리를 가져와서 수정한 후 다시 업데이트 해보았습니다. 그러면 다시 원래의 레포지토리로 돌아가서 누군가 수정한 것을, 또는 내가 다른 곳에서 수정한 내용을 업데이트해야겠죠? 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd ~/git-test
$ cat test.txt
My test memo
$ git pull origin master
$ cat test.txt
very important message
```

위 명령어를 입력해보면 `test.txt` 가 다른 곳에서 수정한 내용으로 업데이트 되었다는 것을 알 수 있습니다.

- **`git pull <REMOTE> <BRANCH>` : `<REMOTE>` 의 원격 레포지토리를 가져온 후 `<BRANCH>` 에 병합한다.**

> **5일**이라는 매우 제한된 시간 때문에 `Branch` 라는 개념을 이 시간에 설명하지는 않겠지만 `git` 은 레포지토리의 변경사항을 평행적으로 관리하기 위하여 여러개의 브랜치 즉, 가지들을 생성합니다. 가령 프로젝트에 새로운 기능을 추가하고 싶은데 그 기능이 프로젝트 전체와 잘 어울리는지 장담할 수가 없으니까 새로운 브랜치를 만들어서 마치 평행세계처럼 완전히 새로운 레포지토리에서 작업하는 것입니다.

`git init` 으로 디렉토리가 `git` 이 관리하는 레포지토리가 될 때 `git` 은 자동적으로 현재 브랜치를 `master` 브랜치로 만들기 때문에, `git pull origin master` 라고 하면 **`origin` 이라는 원격 레포지토리의 내용을 가져와서 `master` 브랜치로 병합해라**는 뜻이 되는 것입니다.

그래서 방금 말했던 새로운 브랜치에서 시험중이었던 기능이 충분히 검증이 되면 `master` 브랜치로 병합을 하게 되는 것입니다. 

---

# VSCode

이제 드디어 **VSCode** 에 대하여 알아보겠습니다. 도커 컨테이너를 종료하고 로컬에서 실습하면 됩니다. 

## VSCode 설치

> 만약 컴퓨터 운영체제로 **Linux** 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 **VSCode** 를 설치할 수 있다고 믿습니다.

### Windows 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=win64user) 에서 **VSCode** 설치파일을 다운로드 받아서 설치하세요.

### MacOS 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=osx) 에서 **VSCode** 설치파일을 다운로드 받아서 설치하세요.

## VSCode 간단 사용법 

> 참고 : https://code.visualstudio.com/docs

먼저 `git` 레포지토리를 **VSCode** 로 여는 두 가지 방법을 알아보겠습니다. 

### 로컬에서 레포지토리 만들기 

**여기서부터는 우분투 도커 컨테이너에서 작업하는 것이 아니라 로컬 컴퓨터에서 하겠습니다.** 일단 폴더(디렉토리)를 하나 만들고 그 폴더(디렉토리)를 **VSCode** 로 열어주세요.

지금까지 디렉토리를 `git` 레포지토리로 초기화할 때 디렉토리 위치에서 

```shell
$ git init
```

을 실행했었습니다. 하지만 이제 **VSCode** 에서 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> 를 누르면 다음과 같이 **VSCode** 의 모든 기능이 담겨있는 **명령 팔레트** 가 나오는데 

![](https://code.visualstudio.com/assets/docs/getstarted/userinterface/commands.png)

여기에서 **git init** 만 입력하면 **Git: Initialize Repository** 가 검색되어 나옵니다. 그것에 커서가 포커싱되었다면 그냥 <kbd>Enter</kbd> 쳐주세요. 그러면 **VSCode** 가 알아서 디렉토리를 `git` 레포지토리로 초기화합니다.

- **<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> : VSCode 에서 명령 팔레트를 연다.**

  - 명령 팔레트는 **VSCode** 의 모든 기능을 실행할 수 있는 메뉴판이다.

- **<kbd>Git: Initialize Repository</kbd> : **VSCode** 명령 팔레트 기능으로써 디렉토리를 `git` 레포지토리로 자동으로 초기화한다.**

  - 명령 팔레트에서 git init 만 검색해도 나온다.

### 새 파일 만들고 저장하기

**VSCode** 에서는 <kbd>Ctrl</kbd>+<kbd>n</kbd> 으로 새 파일을 만들 수 있고 <kbd>Ctrl</kbd>+<kbd>s</kbd> 로 파일을 저장할 수 있습니다. 

- **<kbd>Ctrl</kbd>+<kbd>n</kbd> : **VSCode** 에서 새 파일을 만든다.**

- **<kbd>Ctrl</kbd>+<kbd>s</kbd> : **VSCode** 에서 파일을 저장한다.**

새 파일을 만들고 `test.txt` 로 저장해보세요.

### 변경된 파일 스테이징하고 커밋하기

그리고 이 파일을 스테이징하고 커밋을 해볼텐데, 마찬가지로 **VSCode** 의 **명령팔레트**를 열어서 `git commit` 을 입력해주세요. 

![2020-05-04_16-45](https://user-images.githubusercontent.com/16812446/80945381-abc5f480-8e26-11ea-9e78-ed054d64fbe2.png)

그러면 위와 같이 여러가지 커밋 기능들이 있는데 **Git: Commit All** 에 커서를 포커싱하고 <kbd>Enter</kbd> 를 눌러주세요. 그러면 커밋 메시지를 입력할 수 있는 팝업이 뜨는데 입력하고 다시 <kbd>Enter</kbd> 를 치면 **VSCode**가 변경된 모든 파일을 지알아서 스테이징하고 커밋합니다.

- **<kbd>Git: Commit All</kbd> : **VSCode** 명령 팔레트 기능으로써 변경된 모든 파일을 자동으로 스테이징하고 커밋한다.**

  - 이 기능을 터미널에서 손수 실행하려면 

    ```shell
    git add .
    git commit -m "message"
    ```

    를 다 쳐야 한다.

그런데 커밋은 매우 자주 사용되기 때문에 **VSCode** 에서 별도의 단축키 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>g</kbd> 로 설정되어 있습니다. 이 단축키로 더욱 편하게 커밋을 할 수 잇습니다. 

### 원격 레포지토리 등록하기

이제 레포지토리를 **Github** 에 공유하기 위하여 원격 레포지토리를 등록해보겠습니다. 앞서 **Github** 에 `git-test` 라는 원격레포지토리를 만들었었는데, 이제는 `git-test2` 라는 레포지토리를 만들고 오세요.

다 만들었다면 **명령 팔레트**를 열고 <kbd>git add</kbd> 만 쳐주세요. 그러면 다음 그림과 같이

![2020-05-04_16-53](https://user-images.githubusercontent.com/16812446/80945842-b9c84500-8e27-11ea-9d44-06d50cb56d5a.png)

<kbd>Git: Add Remote</kbd> 가 뜨고 <kbd>Enter</kbd> 를 치면 차례대로 **Remote Name** 과 **Remote URL** 을 입력하게 됩니다. 그럼 차례대로 `origin` 과 `https://github.com/<USER>/git-test2` 를 입력하면 됩니다. 이것은 다음 명령어를 입력한 것과 똑같은 기능을 해줍니다.

```shell
$ git remote add origin https://github.com/<USER>/git-test2
``` 

- **<kbd>Git: Add Remote</kbd> : **VSCode** 명령 팔레트 기능으로써 원격 레포지토리를 등록한다.**

### 원격 레포지토리로 공유하기

원격 레포지토리까지 등록했으니 이제 공유를 해보겠습니다. **명령 팔레트**를 열고 **git push** 만 입력해보세요.

![2020-05-04_16-58](https://user-images.githubusercontent.com/16812446/80946179-6b677600-8e28-11ea-89cc-17084c76b067.png)

그리고 위 그림과 같이 <kbd>Git: Push to...</kbd> 에 커서를 두고 <kbd>Enter</kbd> 를 치면 원격 레포지토리를 지정하는 단계로 넘어가는데 `origin` 밖에 없을테니 그냥 <kbd>Enter</kbd> 를 한번 더 치면 됩니다. **아이디** 와 **비밀번호** 를 입력하는 팝업이 뜨면 **Github** 의 아이디와 비밀번호를 입력하면 됩니다.

- **<kbd>Git: Push to...</kbd> : **VSCode** 명령 팔레트 기능으로써 원격 레포지토리로 변경사항을 업데이트한다.**

그러면 **VSCode** 가 지알아서 `git push origin master` 기능을 수행해줍니다. 각자의 **`https://github.com/<USER>/git-test2`** 로 들어가서 확인해보세요!

### 원격 레포지토리 가져오고 수정하기

이제 우리가 올려뒀던 원격 레포지토리를 가져와보겠습니다. **명령 팔레트** 를 열어서 **git clone** 을 쳐보세요. 

![2020-05-04_17-08](https://user-images.githubusercontent.com/16812446/80946803-d06f9b80-8e29-11ea-951b-198532416531.png)

그러면 위와 같이 <kbd>Git: Clone</kbd> 이 나오는데 <kbd>Enter</kbd> 를 누르면 원격 레포지토리의 **URL** 을 입력하라는 창이 뜨죠. 그러면 각자의 **`https://github.com/<USER>/git-test2`** 를 입력하면 됩니다.

```shell
git clone https://github.com/<USER>/git-test2
```

과 완전 똑같은 기능을 하는 것이죠. 입력하면 디렉토리를 선택하는 창이 뜨는데 원하는 곳으로 선택하면 됩니다.

![2020-05-04_17-15](https://user-images.githubusercontent.com/16812446/80947291-cc904900-8e2a-11ea-9a34-02a055adf6e3.png)

그리고 위와 같이 <kbd>Open</kbd>, <kbd>Open in New Window</kbd> 가 뜨는데 지금은 후자를 선택해주세요.

- **<kbd>Git: Clone</kbd> : **VSCode** 명령 팔레트 기능으로써 원격 레포지토리를 로컬로 가져온다.**

이제 다음과 같이 `test.txt` 에 `VScode 편하다. GBC 재밌다` 를 치고 <kbd>Ctrl+S</kbd> 를 눌러 저장하세요.

![2020-05-04_17-17](https://user-images.githubusercontent.com/16812446/80947401-137e3e80-8e2b-11ea-8e59-d79f9789897a.png)

그렇게 한 다음 지금까지 해온대로 **명령 팔레트** 에서 <kbd>Git: Commit All</kbd>, <kbd>Git: Push to...</kbd> 을 차례로 실행하세요. 그러면 원격 레포지토리로 업데이트됩니다. 너무 빠르고 쉽게 되죠?

### 원격 레포지토리로부터 업데이트하기

이제 원래의 레포지토리, 즉 `text.txt` 에 아무런 내용이 없는 원래의 레포지토리를 열어주세요. 그리고 **명령 팔레트**에서 **git pull** 만 치면 다음과 같이 <kbd>Git: Pull from...</kbd> 이 뜨는데 시원하게 <kbd>Enter</kbd> 를 쳐주세요.

![2020-05-04_17-19](https://user-images.githubusercontent.com/16812446/80947604-7a9bf300-8e2b-11ea-8064-26e3a9bf53aa.png)

그러면 원격 레포지토리를 선택할 수 있는 창이 뜨는데 어차피 `origin` 밖에 없으니까 <kbd>Enter</kbd> 를 다시 한 번 눌러주시면 **VSCode** 가 지알아서 `git pull origin master` 를 실행하면서 `text.txt` 를 업데이트합니다.

## 더 빨라진 개발환경

**VSCode** 는 매우 편리한 단축키를 제공합니다. 이 단축키들의 주된 목적은 마우스 사용을 안하게 하는 것입니다. 왜냐하면 키보드에 올려둔 손으로부터 마우스까지의 거리는 매우 멀기 때문에 마우스를 쓰는 빈도가 높아질수록 코딩하는 시간이 계속 낭비되기 때문입니다. 

그래서 이런 단축키를 익혀두는 이유는 **"마우스를 최대한 사용하지 않기 위해서"** 라고 생각하시면 됩니다. 이 파트의 제목이 "더 빨라진 개발환경" 인데 이 말은 마우스 대신 단축키를 사용하기 때문에 빨라졌다는 것을 의미합니다. 여기서는 몇 가지 핵심적인 단축키만 가볍게 알아보겠습니다. 

> 더 많은 단축키는 공식 **VSCode** 의 메뉴얼 https://code.visualstudio.com/docs/editor/codebasics  을 참고하세요.

### 파일 열기

|기능|단축키|
|:---:|:---:|
|파일 열기|<kbd>Ctrl</kbd>+<kbd>p</kbd>|

**VSCode** 에서 파일을 열 때 왼쪽 **Explorer** 패널에서 파일을 클릭하여 열 수도 있지만 <kbd>Ctrl</kbd>+<kbd>p</kbd> 를 누르고 파일 이름을 입력하면 매우 빠르게 파일을 열 수 있습니다.

- 예시 

  코딩을 하다가 `memdump.c` 파일을 열어보고 싶어졌습니다. 그러면 왼쪽 **Explorer** 패널에서 클릭하여 열 수도 있지만, 다음과 같이 <kbd>Ctrl</kbd>+<kbd>p</kbd> 단축키를 사용할 수 있습니다.
  
  먼저 <kbd>Ctrl</kbd>+<kbd>p</kbd> 누르고 그 파일의 이름을 특정할 수 있는 문자열 `memd` 까지만 칩니다. 그러면 `memdump.c` 파일이 검색되어 나오는데 이제 그냥 <kbd>Enter</kbd> 를 치면 됩니다. 

  ![yaGfFjdSHi](https://user-images.githubusercontent.com/16812446/82407559-6818ef00-9aa4-11ea-959f-333c1f735b9a.gif)


### 파일 닫기 

|기능|단축키|
|:---:|:---:|
|파일 닫기|<kbd>Ctrl</kbd>+<kbd>w</kbd>|

열린 파일의 <kbd>X</kbd> 버튼을 눌러서 파일을 닫을 수도 있지만 <kbd>Ctrl</kbd>+<kbd>w</kbd> 를 누르면 매우 빠르게 닫을 수 있습니다. 

- 예시 

  `memdump.c` 파일을 열고 작업을 하다보니 파일을 닫고 싶어졌습니다. 그래서 그냥 다음과 같이 <kbd>Ctrl</kbd>+<kbd>w</kbd> 를 눌렀습니다.

  ![jynipQcKC2](https://user-images.githubusercontent.com/16812446/82407863-3eac9300-9aa5-11ea-9121-4221c6d99cd9.gif)

### 열린 파일 포커싱 

|기능|단축키|
|:---:|:---:|
|열린 파일 옮겨다니기|<kbd>Ctrl</kbd>+<kbd>Tab</kbd>|
|첫번째 열린 파일 포커싱|<kbd>Alt</kbd>+<kbd>1</kbd>|
|두번째 열린 파일 포커싱|<kbd>Alt</kbd>+<kbd>2</kbd>|
|세번째 열린 파일 포커싱|<kbd>Alt</kbd>+<kbd>3</kbd>|

위 단축키로 열린 파일을 빠르게 포커싱할 수 있습니다. 

- 예시 

  `README.md` 와 `kaslr.c` 와 `memdump.c` 파일을 열고 작업하고 있었습니다. 이때 다른 파일로 옮겨다니고 싶어서 <kbd>Ctrl</kbd>+<kbd>Tab</kbd> 을 눌렀습니다. 하지만 다음과 같이 이것보다 좀 더 편하게 <kbd>Alt</kbd>+<kbd>1</kbd> 으로 첫번째 파일을 포커싱하고 <kbd>Alt</kbd>+<kbd>2</kbd> 로 두번째 파일을 포커싱하고 <kbd>Alt</kbd>+<kbd>3</kbd> 로 세번째 열린 파일을 포커싱 할 수 있습니다.

  ![1FBbmCZKe3](https://user-images.githubusercontent.com/16812446/82408117-d8744000-9aa5-11ea-92c2-43e8475717d4.gif)

### 화면 옮기기 

|기능|단축키|
|:---:|:---:|
|화면 오른쪽으로 분할하여 옮기기|<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&rarr;</kbd>|
|화면 왼쪽으로 분할하여 옮기기|<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&larr;</kbd>|

코딩을 하다보면 두 파일을 같이 보고싶을 때가 있습니다. 그럴 때 마우스로 화면을 오른쪽이나 왼쪽으로 이동시키면 **VSCode** 가 자동으로 화면을 분할해주지면 위 단축키를 이용하면 훨씬 더 빠르게 화면을 분할하여 옮길 수 있습니다.

- 예시 

  `kaslr.c` 와 `memdump.c` 파일을 열고 작업하고 있었습니다. 그런데 이때 `memdump.c` 를 오른쪽 화면으로 옮기고 싶어져서 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&rarr;</kbd> 를 눌렀습니다.

  ![UXMBh2K8so](https://user-images.githubusercontent.com/16812446/82408373-6819ee80-9aa6-11ea-9aad-1cd2c5dce277.gif)

### 분할된 화면 포커싱 

|기능|단축키|
|:---:|:---:|
|오른쪽 화면 포커싱|<kbd>Ctrl</kbd>+<kbd>1</kbd>|
|왼쪽 화면 포커싱|<kbd>Ctrl</kbd>+<kbd>2</kbd>|

화면을 분할했을 때 왼쪽 화면으로 커서를 두고 싶을 때 <kbd>Alt</kbd>+<kbd>1</kbd> 로는 되지 않습니다. <kbd>Alt</kbd>+<kbd>1</kbd>, <kbd>Alt</kbd>+<kbd>2</kbd>, <kbd>Alt</kbd>+<kbd>3</kbd> 은 해당 화면에서의 열린 탭의 순서이기 때문입니다. 

왼쪽 화면이나 오른쪽 화면을 포커싱하고 싶다면 <kbd>Ctrl</kbd>+<kbd>1</kbd>, <kbd>Ctrl</kbd>+<kbd>2</kbd> 을 누르면 됩니다. 

- 예시 

  다음과 같이 분할된 화면을 <kbd>Ctrl</kbd>+<kbd>1</kbd>, <kbd>Ctrl</kbd>+<kbd>2</kbd> 로 빠르게 커서를 이동시킬 수 있습니다. 

  ![sUipBmhwXE](https://user-images.githubusercontent.com/16812446/82408662-07d77c80-9aa7-11ea-88e2-db0b8c95ea09.gif)

> 사실 <kbd>Ctrl</kbd>+<kbd>1</kbd>, <kbd>Ctrl</kbd>+<kbd>2</kbd> 은 왼쪽 화면과 오른쪽 화면을 포커싱 하는게 아니라 더 정확하게 첫번째 분할 화면을 포커싱, 두번째 분할 화면을 포커싱하는 단축키입니다. 그러면 자연스럽게 <kbd>Ctrl</kbd>+<kbd>3</kbd> 이 세번째 분할 화면을 포커싱하는 단축키라는 것을 유추할 수 있겠죠?

### 화면 레이아웃 변경

|기능|단축키|
|:---:|:---:|
|화면 레이아웃 변경|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>0</kbd>|

코딩을 하다보면 화면을 수평으로 분할하는 것이 아니라 수직으로 분할하는 것이 더 편할 때도 있습니다. 그럴때 이 단축키로 화면 레이아웃을 변경하면 됩니다. <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>0</kbd> 를 한번 더 누르면 레이아웃이 원래대로 되돌아옵니다.

- 예시 

  `readme.md` 파일을 작성하면서 **Markdown** 미리보기 창을 같이 보고 있었는데, 화면 레이아웃을 변경하는 것이 더 나을 것 같아서 다음과 같이 <kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>0</kbd> 로 변경을 합니다.

  ![Rq5xgcvRFC](https://user-images.githubusercontent.com/16812446/82408988-b8de1700-9aa7-11ea-82f7-da732c9ff046.gif)

### 화면 복제

|기능|단축키|
|:---:|:---:|
|화면 복제|<kbd>Ctrl</kbd>+<kbd>\\</kbd>|

매우 긴 파일을 코딩할 때 파일의 앞부분과 뒷부분을 동시에 보고 싶을 때가 있습니다. 그럴 때 이 단축키로 화면을 복제할 수 있습니다. 

- 예시 

  `readme.md` 파일을 작성하다가 이 파일의 첫부분을 점검하고 싶었습니다. 그래서 다음과 같이 <kbd>Ctrl</kbd>+<kbd>\\</kbd> 를 눌러 <kbd>Ctrl</kbd>+<kbd>2</kbd> 로 두번째 화면을 포커싱한 후 파일의 맨 처음으로 커서를 이동하였습니다. 

  ![v70ylfP1Ld](https://user-images.githubusercontent.com/16812446/82409239-44f03e80-9aa8-11ea-8b91-12df0d825110.gif)

> 여러번 누르면 여러번 복제됩니다.

---

# Markdown 

**Markdown** 은 여러가지 형식으로 텍스트를 작성할 수 있게 해주는 마크업 언어입니다. **Markdown** 파일은 확장자 `.md` 를 갖고 있습니다. **Markdown** 을 알아야 하는 주된 이유 중 하나는 레포지토리를 **Github** 에 공유할 때 프로그램을 효과적으로 설명하기 위해서입니다. 

**Markdown** 이 얼마나 효과적인 포맷팅 기능을 제공하는지는 지금 읽고 있는 이 파일들이 전부다 `.md` 파일인 것만 보아도 알 수 있습니다. **Markdown** 의 문법은 매우 간단하지만 매우 다양한 기능을 제공합니다. 여기에서는 핵심적인 문법만을 가볍게 알아보겠습니다. 

더 자세한 **Markdown** 의 문법을 알아보려면 **Google** 에 검색하거나

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

https://markdown-it.github.io/

을 참고하세요.

## **VSCode** 의 **Markdown** 미리보기

|기능|단축키|
|:---:|:---:|
|**Markdown** 미리보기|<kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>v</kbd>|

먼저 **VSCode** 를 열어서 `test.md` 파일을 하나 만들고 다음 내용을 입력하고 저장해봅시다. 

```markdown
# 제목 

**Markdown** 파일 연습용 파일입니다.
```

그리고 <kbd>Ctrl</kbd>+<kbd>k</kbd> , <kbd>v</kbd> 를 누르거나 오른쪽 위에서

![Screen Capture_select-area_20200520051136](https://user-images.githubusercontent.com/16812446/82373312-60335d80-9a58-11ea-9a64-19af6e44b7cb.png)

이 아이콘을 클릭하면 다음과 같이 **Markdown** 미리보기가 나타나서 **Markdown** 파일이 어떻게 랜더링되는지 실시간으로 보여줍니다. 이 환경에서 **Markdown** 을 효율적으로 작성할 수 있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82409433-b3350100-9aa8-11ea-8277-3f2c1de91c8c.gif" width="70%" height="auto">
</div>

## 제목 

가장 먼저 제목입니다. 다음과 같이 제목을 쓸 수 있습니다.

```markdown
# 가장 큰 제목

## 두번째로 큰 제목

### 세번째로 큰 제목

#### 세번째로 작은 제목

##### 두번째로 작은 제목

###### 가장 작은 제목
```

위 코드가 다음과 같이 랜더링됩니다.

---

# 가장 큰 제목

## 두번째로 큰 제목

### 세번째로 큰 제목

#### 세번째로 작은 제목

##### 두번째로 작은 제목

###### 가장 작은 제목

---

## 텍스트 포맷팅 

그 다음으로는 텍스트 포맷팅입니다. 

```markdown
별 하나로 묶으면 *이탤릭체가 된다*는 사실.

별 두개로 묶으면 **강조체 된다**는 사실.

틸드 두개로 묶으면 ~~취소선이 된다~~는 사실.

백 쿼터로 묶으면 코드체가 되어 `int a = 100;` 을 코드 폰트로 보여줄 수 있다는 사실.

> ">" 을 문장 맨 앞에 쓰면 인용구 스타일로 쓸 수 있다는 사실. 

>> ">>" 을 쓰면 이렇게 됩니다.

문장을 한번 개행하면 띄어지지가 않습니다.
보세요. 한번 개행했는데 띄어지지가 않습니다. 

**Markdown** 에서는 이렇게 두 번 개행해야 띄어집니다.

두 번 개행하니까 띄어지죠.
```

위 코드가 다음과 같이 랜더링됩니다.

---

별 하나로 묶으면 *이탤릭체가 된다*는 사실.

별 두개로 묶으면 **강조체 된다**는 사실.

틸드 두개로 묶으면 ~~취소선이 된다~~는 사실.

백 쿼터로 묶으면 코드체가 되어 `int a = 100;` 을 코드 폰트로 보여줄 수 있다는 사실.

> ">" 을 문장 맨 앞에 쓰면 인용구 스타일로 쓸 수 있다는 사실. 

>> ">>" 을 쓰면 이렇게 됩니다.

문장을 한번 개행하면 띄어지지가 않습니다.
보세요. 한번 개행했는데 띄어지지가 않습니다. 

**Markdown** 에서는 이렇게 두 번 개행해야 띄어집니다.

두 번 개행하니까 띄어지죠.

---

## 아이템과 순서

그 다음으로는 아이템과 순서입니다. 

```markdown
- 아이템입니다. 

  - 하위 아이템이에요. 두번 띄어써야 합니다.

    - 더 하위 아이템입니다. 

      이렇게 문장을 같은 레벨로 쓸 수 있습니다.
  
  - 아무말 

- 아무말 

1. 순서 아이템은 이렇게 1. 로 시작합니다.

2. 두번째 순서 아이템

    - 순서 아이템의 하위 아이템을 쓰려면 네 번 띄어써야 합니다. 

3. 그 다음 순서 아이템이에요. 

  - 순서 아이템의 하위 아이템을 두번 띄어 쓰면 이렇게 하위 레벨로 랜더링되지 않습니다.
```

위 코드가 다음과 같이 랜더링됩니다.

---

- 아이템입니다. 

  - 하위 아이템이에요. 두번 띄어써야 합니다.

    - 더 하위 아이템입니다. 

      이렇게 문장을 같은 레벨로 쓸 수 있습니다.
  
  - 아무말 

- 아무말 

1. 순서 아이템은 이렇게 1. 로 시작합니다.

2. 두번째 순서 아이템

    - 순서 아이템의 하위 아이템을 쓰려면 네 번 띄어써야 합니다. 

3. 그 다음 순서 아이템이에요. 

  - 순서 아이템의 하위 아이템을 두번 띄어 쓰면 이렇게 하위 레벨로 랜더링되지 않습니다.
---

## 링크와 사진

이제 링크와 사진을 삽입하는 문법입니다.

```markdown
개발자들이 가장 자주 사용하는 검색 엔진은 [Google](https://www.google.com) 입니다. 

한동대생들이 항상 이용하는 사이트는 [Hisnet](http://hisnet.handong.edu) 입니다. 

한동대 로고는 다음과 같습니다.

![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/HGU-Emblem-eng2.png/150px-HGU-Emblem-eng2.png) 

로컬에 저장되어 있는 이미지를 사용할 수도 있습니다. 

![스폰지](sponge.png) 

> 이 경우 `sponge.png` 가 로컬에 존재해야 합니다. 
```

위 코드가 다음과 같이 랜더링됩니다.

---

개발자들이 가장 자주 사용하는 검색 엔진은 [Google](https://www.google.com) 입니다. 

한동대생들이 항상 이용하는 사이트는 [Hisnet](http://hisnet.handong.edu) 입니다. 

한동대 로고는 다음과 같습니다.

![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/HGU-Emblem-eng2.png/150px-HGU-Emblem-eng2.png) 

로컬에 저장되어 있는 이미지를 사용할 수도 있습니다. 

![스폰지](sponge.png) 

> 이 경우 `sponge.png` 가 로컬에 존재해야 합니다. 

---

## 코드 입력 

백쿼터 \` 로 묶으면 int a = 100; 같은 코드를 `int a = 100;` 와 같이 가독성이 높은 코드체로 쓸 수 있습니다. 하지만 여러줄의 코드를 써야할 경우 \`\`\` 로 코드를 묶으면 됩니다. 

이때 한가지 편리한 기능은 시작하는 \`\`\` 의 오른쪽에 코드의 종류를 쓰면 코드에 색깔이 입혀져서 하이라이팅된다는 점입니다.


````markdown
```shell
$ git init
$ docker run -it ccss17/ubuntu
``` 
 
```python
s = "Python 문법 하이라이팅"
print s
```

```
s = "하이라이팅이 되지 않습니다."
print s
```
````

위 코드가 다음과 같이 랜더링됩니다.

---

```shell
$ git init
$ docker run -it ccss17/ubuntu
``` 
 
```python
s = "Python 문법 하이라이팅"
print s
```

```
s = "하이라이팅이 되지 않습니다."
print s
```
---

## 표 

**Markdown** 은 표도 지원합니다. 

```markdown
|첫번째|두번째|세번째|
|:---:|:---:|:---:|
|1|2|3|
|a|b|c|
```

위 코드가 다음과 같이 랜더링됩니다.

---

|첫번째|두번째|세번째|
|:---:|:---:|:---:|
|1|2|3|
|a|b|c|

---

## 분할선 

분할선은 전환되는 내용이 있을 때 사용하면 가독성을 높힐 수 있습니다.

```markdown
계속 되는 내용이 있는데

---

내용이 전환되면 이렇게 분할선을 넣으면 좋습니다.
```

위 코드가 다음과 같이 랜더링됩니다.

---

계속 되는 내용이 있는데

---

내용이 전환되면 이렇게 분할선을 넣으면 좋습니다.

---

## README.md 

`README.md` 라는 이름을 가진 파일은 특별한 파일입니다. 왜냐하면 **Github** 이 레포지토리의 `README.md` 파일을 자동으로 랜더링하여 웹페이지에 보여주기 때문입니다. 

**Github** 은 레포지토리의 최상위 경로에 있는 `README.md` 를 랜더링하여 보여줍니다. https://github.com/ccss17/ProgrammerBase 의 경우처럼 말이죠.

그리고 어떤 디렉토리로 들어가면 그 디렉토리의 최상위 경로에 있는 `README.md` 를 랜더링해서 보여줍니다. 여러분은 지금 `02-Day2` 의 디렉토리의 `readme.md` 파일이 랜더링된 것을 읽고 있습니다.

지금까지 **Markdown** 문법을 공부한 것은 이 `readme.md` 을 스스로 작성할 수 있는 능력을 기르기 위함입니다. 

---

# 과제 

- [hw2.md](hw2.md) 에 과제 가이드가 나와있으니 따라주시면 됩니다. 

- 과제를 발표를 하며 설명할 수 있어야 합니다. 
