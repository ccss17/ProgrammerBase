# Day 2

GBC 첫번째 과정 **Programmer Base** 의 2일차 내용입니다.

---

# stackoverflow survey

개발 공부를 하다보면 [스택오버플로우](https://stackoverflow.com/)의 답변을 한번쯤 참고해보셨을텐데요. 전세계 개발자가 바로 이 사이트를 통해 개발 관련 질문을 올리고 정보를 공유한답니다. 전세계 개발자들이 활동하는 가장 큰 커뮤니티 중 하나이기 때문에 새벽 시간에 질문을 올려도 답변이 매우 빨리 올라오는 곳이죠.

이곳에서 질문에 대한 답변이 사용자들에게 채택되면 점수가 오르는데, 얼마나 공신력이 있는 곳이면 상위 1% 의 스택오버플로우 유저는 구글 입사가 프리패스된다는 말도 들은적이 있네요.

어쨌든 이 커뮤니티는 매년 전세계 개발자를 대상으로 설문조사를 하는데 이 개발자 서베이를 보면 트렌디한 기술이 뭔지, 최신 기술이 뭔지, 나만 모르고 있던 좋은 기술이 뭔지 알 수 있습니다. 다음 링크를 통해 2019년 설문조사에 들어가보세요.

https://insights.stackoverflow.com/survey/2019

왼쪽 카테고리를 보면 여러 항목에 대한 설문조사를 한 것이 보이는데 다음과 같이 **Technology** 분야가 메인 디쉬라고 볼 수 있을 것 같습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80893957-ba6eb780-8d11-11ea-86c0-3570463f1a79.png" width="250" height="400"> </div>

나머지 항목은 궁금하시면 더 살펴보셔도 되고 지금 이 시간에는 이 설문조사를 통해 전세계에서 가장 핫한 플랫폼과 에디터가 뭔지 알아보겠습니다.

## 개발자들이 가장 사랑하는 플랫폼

설문조사에서 **Platforms** 항목을 찾아보면 다음과 같은 설문결과를 볼 수 있습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80894214-1e927b00-8d14-11ea-9a86-81051ab2c8c8.png" width="400" height="400"> </div>

개발자들에게 인기있는 플랫폼 1위는 역시나 **53.3%** 로 리눅스네요. 이는 윈도우와 맥OS 보다 높은 수치입니다. 

어제 배웠던 도커는 3위를 차지했는데 이는 스택오버플로우가 2019년에 처음으로 도커에 대한 설문조사를 한 결과라고 하니까 개발자들이 얼마나 도커에 주목하고 있는지 감이 오시나요? 설문조사 데뷔 첫해만에 맥OS, 안드로이드, AWS 등을 제치고 전세계 플랫폼 3위를 차지했다면 엄청나네요. 

전세계 개발자들이 이런 플랫폼과 기술들에 왜 사랑에 빠졌는지 몰라서는 안됩니다. (매니저 스크립트로 이전) 막말로 제가 인력거꾼이 되려고 인력거 운전법을 열심히 배웠는데 자동차가 개발되었다면 최신 기술에 민감하지 못한 저는 시장에서 도태되고 말겠죠. 프로그래머 생태계는 그런 최신 기술이 역사상 유례없는 속도로 발전하고 있기 때문에 더욱 변화에 예민해져야만 합니다. 그런 의미에서 기존 **GBC Linux** 를 **GBC Programmer Base** 로 바꾸고 도커같은 트렌디한 기술들을 배워보지 않을 수가 없겠죠?

## 개발자들이 가장 사랑하는 개발환경

마지막으로 **Most Popular Development Environments** 항목을 보면서 개발자들이 어떤 개발환경을 가장 좋아하는지 알아보겠습니다.

<div align="center">

<img src="https://user-images.githubusercontent.com/16812446/80894553-d163d880-8d16-11ea-854f-8f74fb11607f.png" width="300" height="300">

<img src="https://user-images.githubusercontent.com/16812446/80895772-8c926e80-8d23-11ea-92b2-df4cfdd80085.png" width="300" height="300">

<img src="https://user-images.githubusercontent.com/16812446/80895968-2528ee80-8d24-11ea-8bf5-070d5f503269.png" width="300" height="330">

<img src="https://user-images.githubusercontent.com/16812446/80895984-425dbd00-8d24-11ea-8d9d-dfdd6b7d09d1.png" width="300" height="330">

</div>

설문조사는 **"모든 개발자", "웹 개발자", "스마트폰 어플 개발자", "데브 옵스"** 를 대상으로 진행되었는데 "스마트폰 어플 개발자" 를 제외하고는 `Visual Studio Code` 즉, `VSCode` 가 1위를 차지했습니다. 심지어 "스마트폰 어플 개발자" 에서도 `VSCode` 가 `Android Studio` 와 매우 미세한 차이로 2위를 차지했으니, 개발자들이 `VSCode` 가 제공하는 개발환경에 얼마나 푹 빠져버렸는지 알 수 있겠죠?

---

리눅스와 도커는 계속 배우고 있으니까 `VSCode` 개발환경만 알아보면 되겠네요. 하지만 그러기 전에 `git` 과 `vim` 을 간단하게 알아보겠습니다. 

# git

> 참고 : https://git-scm.com/book/en/v2

코딩을 막 배우기 시작하면 종종 카톡이나 메일에 소스코드를 백업 하곤 합니다. 하지만 이 방식에는 몇 가지 단점이 있습니다. 먼저 소스코드의 저장장소가 매우 산발적이고 일관성이 없어서 매번 찾기가 힘듭니다. 그리고 소스코드의 변화과정을 제대로 이해하기 힘듭니다. 하루는 그렇게 백업하는 것도 잊어버리고 백업을 하지 않았다가 실수로 소스코드를 삭제해버리고 말았지만 복구할 수 있는 방법이 전혀 없었습니다.

이런 문제는 개인 프로젝트보다 규모가 훨씬 큰 단체 프로젝트에서 더 심각해집니다. 누가 무엇을 고쳤는지, 소스코드 저장소가 어디에 있는지, 만약 누가 실수로 소스코드를 지워버렸을 때 복구를 할 수 없을 때 기업은 실질적인 금전적인 피해를 받게 됩니다. 

이 문제를 해결하기 위해 나온 것이 버전 컨트롤 시스템(Version Control System) 입니다. 줄여서 VCS 는 단어 그대로 **"프로젝트의 버전을 손쉽게 다룰 수 있게 해주는 시스템"** 입니다. VCS 에는 여러 종류가 있지만 이제 우리는 그 중에서 가장 많이 사용되는 VCS 인 `git` 을 간단하게 알아보겠습니다. `git` 을 익히면 제가 위에서 설명한 문제들이 다 해결되는 것입니다!

`git` 의 자세한 설명과 의미를 공부하기 위해서는 https://git-scm.com/book/en/v2 를 참고해주세요. 그리고 방학 때나 휴학을 했을 때 시간이 남으니까 `git` 의 `Branching` 기능까지 익혀두시길 **강력하게 강력하게** 추천합니다. 왜냐면 여러분이 개발자로 살아가는 이상 **어차피 언젠가는 `git Branching` 기능까지 알아야만 하기 때문**입니다. 

- **`git` : 가장 인기있고 자주 사용되는 VCS 이다.**

  - `git` 은 파일을 세 가지 상태 modified, staged, committed 로 관리한다.

## git 설치

만약 ~~없을 가능성이 높을테지만~~ 컴퓨터 운영체제로 `Linux` 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 `git` 를 설치할 수 있다고 믿습니다. 

### Windows git 설치

1. [이 링크](https://git-scm.com/download/win) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

### MacOS git 설치

1. [이 링크](https://git-scm.com/download/mac) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

### Ubuntu 컨테이너에 git 설치 

그리고 우분투 도커 컨테이너에 접속해서 다음 명령어로 `git` 을 설치해주세요.

```shell
$ apt install -y git
```

## git 이 파일을 관리하는 상태

- **untracked 상태 : `git` 이 변경사항을 추적하지 않는 파일이다.**

- **modified 상태 : 파일을 변경했지만 아직 스테이징되지 않은 상태이다.**

- **staged 상태 : 변경된 파일을 커밋이 될 리스트에 포함시킨 상태이다.**

- **committed 상태 : `git` 데이터베이스에 하나의 버전으로 저장된 상태이다.**

`git` 을 실제로 실습해보면서 이 상태들이 뭔지 알아보겠습니다. 먼저 우분투 컨테이너에 접속한 상태에서 다음 명령어들을 실행하세요.

```shell
$ cd                  # 홈 디렉토리로 이동
$ mkdir git-test      # 디렉토리 생성
$ cd git-test
```

그러면 홈 디렉토리 밑에 `git-test` 디렉토리에 위치하게 됩니다.

### git 설치 후 초기 설정

`git` 을 설치한 후 가장 처음 해야 할 일은 초기 설정입니다. `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요.

```shell
$ git config --global user.name "<NAME>"
$ git config --global user.email "<EMAIL>"
```

### git 레포지토리 생성하기

그리고 곧바로 

```shell
$ git init
```

을 실행합시다. 이 명령어는 현재 디렉토리를 `git` 레포지토리로 만들고 `git` 이 파일의 변경을 추적하게 합니다.

- **`git init` : 디렉토리를 `git` 레포지토리로 만들어 디렉토리 내의 파일을 `git` 이 추적하게 한다.**

### 파일 생성하고 스테이징하기 (untracked 상태 &rarr; staged 상태)

이제 프로젝트를 위하여 `main.c` 라는 프로그램을 개발하고 싶다고 하고 다음 명령어를 입력하세요.

```shell
$ touch main.c
$ git status
...
Untracked files:
	main.c
...
```

`git status` 로 현재 `git` 레포지토리의 상태, 즉 디렉토리 내 파일들이 **untracked 상태, modified 상태, staged 상태, committed 상태** 중 어떤 상태인지 알아볼 수 있습니다.

- **`git status` : `git` 레포지토리의 상태를 출력한다.**

  - `-s` 옵션을 붙히면 간단하게 출력한다.

실행 결과가 위와 같은데 금방 만든 `main.c` 가 `Untracked files` 인 걸로 보아 **untracked 상태**라는 것을 알 수 있습니다. 이 상태에 있는 파일들은 `git` 이 변경사항을 추적하면서 버전에 포함시키지 않습니다.

`git` 이 이 파일을 추적하고 버전에 포함시키도록 하기 위해 다음 명령어를 실행해주세요.

```shell
$ git add main.c
$ git status
...
Changes to be committed:
  ...
	new file:   main.c
```

이로써 `main.c` 가 `Changes to be committed`, 즉 **staged 상태**가 되었습니다. **staged 상태**는 이렇게 커밋이 되기로 예정된 파일을 의미합니다. 그리고 스테이징한다는 것은 파일을 **staged 상태**로 만든다는 것이죠.

- **`git add <FILE>` : `<FILE>` 을 커밋 예정 상태로 만듭니다.**

  - `git add .` 로 파일명을 일일이 입력하지 않고 모든 파일을 자동으로 `staged` 상태로 만들 수 있다.

### 커밋해서 하나의 버전으로 만들기 (staged 상태 &rarr; committed 상태)

이제 스테이징된 파일들을 커밋해서 하나의 버전으로 만들기만 하면 됩니다! 다음 명령어를 입력하세요.

```shell
$ git commit -m "my first commit"
$ git status
On branch master
nothing to commit, working tree clean
```

그러면 커밋할 때 당시의 레포지토리의 파일들이 하나의 스냅샷으로 찍혀서 하나의 버전이 되었습니다. 

- **`git commit` : 스테이징된 파일들을 커밋하여 하나의 버전으로 만들어 `git` 데이터베이스에 저장한다.**

  - `git commit -m <MESSAGE>` 로 커밋 메시지를 바로 입력할 수 있다.

### 변경된 파일 커밋하기 (modified 상태 &rarr; staged 상태 &rarr; committed 상태)

코딩을 하다보면 파일을 변경하지 않을 수 없겠죠? 그렇게 새로운 기능이나 변경사항을 추가하면 또 다시 커밋해서 하나의 버전으로 만들어두세요. 커밋은 레포지토리에 유의미한 크기의 기능이 추가되었을 때, 또는 레포지토리에 유의미한 변경이 이루어졌을 때 하는 것이 좋지만 처음에는 일단 그냥 "커밋을 많이 하는 것이 좋다" 라는 마인드로 `git` 을 사용해보세요. 그래야만 파일이 변경된 기록이 자주 남겨져서 복원할 시점, 변경기록을 살펴볼 스냅샷들이 많아지거든요.

```shell
$ echo "#include <stdio.h>" > main.c
$ git add .
$ git commit -m "add header.."
```

위 명령어를 입력함으로써 `main.c` 에 헤더를 추가하고 스테이징한 후 커밋하여 또 하나의 버전으로 만들어보세요.

### 커밋 기록 보기 

프로그램을 개발하면서 무언가 잘못되었을 때, 또는 프로젝트가 어떻게 변경되었는지 이해하고 싶을 때 커밋 기록을 살펴볼 수 있습니다.

```shell
$ git log
commit 9a58815ccb87fb516feb22e02a55232cf45da7d5 (HEAD -> master)
Author: awef <awef@naver.com>
Date:   Sun May 3 09:48:23 2020 +0000

    e
```

저는 위와 같은 결과가 나오네요. 초기 설정시 입력하였던 이름과 이메일이 커밋 기록에 남기 때문에 누가 변경한 시점부터 프로젝트가 잘못되었는지, 또는 잘되었는지 확인하는 용도로도 사용할 수 있어서 편리합니다.

- **`git log` : 커밋 기록을 출력한다.**

## github

`github` 는 `git` 레포지토리를 다른 사람과 공유할 수 있는 플랫폼입니다. 이곳을 통하여 협업을 할 수 있기도 하고 자신이 관심있는 프로그램들이 무엇인지 알려줄 수도 있습니다. 최근에는 `github` 에 있는 그 사람의 레포지토리들을 포트폴리오로 취급하고 능력을 가늠해보기도 한다니까 `github` 에 레포지토리를 많이 공유하는 것이 좋을 것 같습니다.

### github 가입 

`github` 에 가입되어 있지 않으신 분들은 먼저 https://github.com/ 에서 가입을 해주세요.

### github 레포지토리 생성

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/80912176-21be5300-8d76-11ea-8098-4ca30a560c4c.PNG" >
</div>

가입한 다음에는 왼쪽 위에서 초록색 **"New"** 버튼을 찾아서 누르면 레포지토리 생성 창으로 넘어갑니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/80912222-706bed00-8d76-11ea-8c25-b90e9bed11a4.PNG" >
</div>

그러고 레포지토리 이름을 그냥 **"git-test"** 라고 하고 테스트용 레포지토리니까 다른 사람들이 못 보게 **"Private"** 에 체크를 하고 아래에 **"Create repository"** 버튼을 눌러 생성을 완료해줍시다.

### git 에서 레포지토리 공유

이제 좀 전에 우분투 컨테이너에서 만들었던 레포지토리를 여기에 공유해보겠습니다.

```shell
$ git remote add origin https://github.com/ccss17/git-test
$ git push origin master
```

### 원격 레포지토리 가져오기

(자신이 올린 레포지토리 갖고 오기)

(레포지토리 업데이트 하기)

(다른 사람이 올린 레포지토리 갖고 오기)

## markdown 파일

### readme.md 파일

# VSCode

## VSCode 설치

만약 ~~없을 가능성이 높을테지만~~ 컴퓨터 운영체제로 `Linux` 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 `VSCode` 를 설치할 수 있다고 믿겠습니다.

### Windows 도커 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=win64user) 에서 `VSCode` 설치파일을 다운로드 받아서 설치하세요.

### MacOS 도커 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=osx) 에서 `VSCode` 설치파일을 다운로드 받아서 설치하세요.

# vim

- 일반 텍스트 에디터보다 VIM 이 얼마나 더 빠른지

  - VIM 의 장점 2 

    - 손을 키보드에 댄 그 상태 그대로 안움직인다 -> 이게 얼마나 좋은건지 직접 써본사람만 안다 

    - 타수가 줄어든다. -> 시간 절약 

# github

`github` 사용법

- `readme.md` 라는 특별한 이름의 파일 설명 

# Markdown

- `markdown` 파일 사용법

- hguapp.ghoster.cc/git/ 과 github.com/ccss17 에서 내가 이미 올려둔 markdown 예시 보여주기

- {USERID}.github.io 사용법 알려주기 (다른 날에 해도 됨)

  - 예시로 내가 수학공식 올리던거 알려주기

# VSCode

- `vscode` 사용법 

# 교재

- (기존 GBC) Ch02 디렉토리와 파일, Ch04 쉘 사용하기

# CLI `zsh`, `vim`, `tmux`, `ssh`

- 매니저 스크립트 만들고 이런 최신기술을 클린코더 말투로 몰랐나요, 몰랐다면 왜 몰랐습니까? 라며 건전한 비판. 

  - bash 쉘을 전쟁터에 나갈 떄 칼과 화살을 갖고 가는 것. 도전을 주기 위해 하는 것..