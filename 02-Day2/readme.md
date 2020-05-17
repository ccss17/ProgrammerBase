# Day 2

GBC 첫번째 과정 **Programmer Base** 의 2일차 내용입니다.

---

# 리눅스 교재 

오늘 내용을 수월하게 이해하기 위해서는 교재의 **Chapter 04** 내용을 먼저 실습해보아야 합니다.

교재에서 다음 분량을 읽고 우분투 도커 컨테이너에서 실습해주세요. 사실 너무 열심히 읽지 않아도 됩니다. 즉, 막 외우려고 애쓰지 않아도 된다는 뜻입니다. 다만 꼭 "정독" 을 하시고 한번쯤 책에 있는 실습을 따라해주세요. 

**(옵션)** 라고 되어있는 파트는 시간절약을 위해 넘겨도 됩니다.

## Chapter 04

- **186p ~ 203p 읽고 실습하기**

  - 셸의 기능과 종류, 셸 기본 사용법, 입출력 방향 바꾸기

- **206p ~ 217p 읽고 실습하기**

  - 배시 셸 환경 설정, 에일리어스와 히스토리

- **220p ~ 229p 읽고 실습하기**

  - **(옵션)** 프롬프트 설정, 환경 설정 파일

---

# stackoverflow survey

개발 공부를 하다보면 [스택오버플로우](https://stackoverflow.com/)의 답변을 한번쯤 참고해보셨을텐데요. 전세계 개발자가 바로 이 사이트를 통해 개발 관련 질문을 올리고 정보를 공유하고 있습니다. 

이곳에서 질문에 대한 답변이 사용자들에게 채택되면 점수가 오르는데, 얼마나 공신력이 있는 곳이면 상위 1% 의 스택오버플로우 유저는 구글 입사가 프리패스된다는 말도 들은적이 있네요.

이 커뮤니티는 매년 전세계 개발자를 대상으로 설문조사를 하는데 이 서베이를 보면 트렌디한 기술이 뭔지, 나만 모르고 있던 좋은 기술이 뭔지 알 수 있습니다. 다음 링크를 통해 2019년 설문조사에 들어가보세요.

https://insights.stackoverflow.com/survey/2019

왼쪽 카테고리를 보면 여러 항목에 대한 설문조사를 한 것이 보이는데 다음과 같이 **Technology** 분야가 메인 디쉬라고 볼 수 있을 것 같습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80893957-ba6eb780-8d11-11ea-86c0-3570463f1a79.png" width="30%" height="auto"> </div>

나머지 항목은 궁금하시면 더 살펴보셔도 되고 지금 이 시간에는 이 설문조사를 통해 전세계에서 가장 핫한 플랫폼과 에디터가 뭔지 알아보겠습니다.

## 개발자들이 가장 사랑하는 플랫폼

설문조사에서 **Platforms** 항목을 찾아보면 다음과 같은 설문결과를 볼 수 있습니다.

<div align="center"> <img src="https://user-images.githubusercontent.com/16812446/80894214-1e927b00-8d14-11ea-9a86-81051ab2c8c8.png" width="40%" height="auto"> </div>

개발자들에게 인기있는 플랫폼 1위는 역시나 **53.3%** 로 리눅스네요. 어제 배웠던 도커는 3위를 차지했는데 이는 스택오버플로우가 2019년에 처음으로 도커에 대한 설문조사를 한 결과라고 하니까 개발자들이 얼마나 도커에 주목하고 있는지 감이 오시나요? 전세계 개발자들이 이런 플랫폼과 기술들에 왜 사랑에 빠졌는지 몰라서는 안되기 때문에 꼭 배워봐야 합니다. 

## 개발자들이 가장 사랑하는 개발환경

이제 **Most Popular Development Environments** 항목을 보면서 개발자들이 어떤 개발환경을 가장 좋아하는지 알아보겠습니다.

<div align="center">

<img src="https://user-images.githubusercontent.com/16812446/80894553-d163d880-8d16-11ea-854f-8f74fb11607f.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895772-8c926e80-8d23-11ea-92b2-df4cfdd80085.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895968-2528ee80-8d24-11ea-8bf5-070d5f503269.png" width="40%" height="auto">

<img src="https://user-images.githubusercontent.com/16812446/80895984-425dbd00-8d24-11ea-8d9d-dfdd6b7d09d1.png" width="40%" height="auto">

</div>

설문조사는 **"모든 개발자", "웹 개발자", "스마트폰 어플 개발자", "데브 옵스"** 를 대상으로 진행되었는데 "스마트폰 어플 개발자" 를 제외하고는 `Visual Studio Code` 즉, `VSCode` 가 1위를 차지했습니다. 심지어 "스마트폰 어플 개발자" 에서도 `VSCode` 가 `Android Studio` 와 매우 미세한 차이로 2위를 차지했으니, 개발자들이 `VSCode` 가 제공하는 개발환경에 얼마나 푹 빠져버렸는지 알 수 있겠죠?

---

그러면 이 전세계의 추세를 따라가봅시다! 그런데 리눅스와 도커는 계속 배우고 있으니까 `VSCode` 개발환경만 알아보면 되겠네요. 하지만 그러기 전에 `git` 을 간단하게 알아보겠습니다. 

# git

> 참고 : https://git-scm.com/book/en/v2

코딩을 막 배우기 시작하면 종종 카톡이나 메일에 소스코드를 백업 하곤 합니다. 하지만 이 방식에는 몇 가지 단점이 있습니다. 먼저 소스코드의 저장장소가 매우 산발적이고 일관성이 없어서 매번 찾기가 힘듭니다. 그리고 소스코드의 변화과정을 제대로 이해하기 힘듭니다. 만약 백업하는 것도 잊어버리고 백업을 하지 않았다가 실수로 소스코드를 삭제해버린다면 복구할 수 있는 방법이 전혀 없습니다.

이런 문제는 규모가 큰 단체 프로젝트에서 더 심각해집니다. 누가 무엇을 고쳤는지, 소스코드 저장소가 어디에 있는지, 만약 누가 실수로 소스코드를 지워버렸을 때 복구를 할 수 없을 때 기업은 실질적인 금전적인 피해를 받게 됩니다. 

이 문제를 해결하기 위해 나온 것이 버전 컨트롤 시스템(Version Control System) 입니다. 줄여서 VCS 는 단어 그대로 **"프로젝트의 버전을 손쉽게 다룰 수 있게 해주는 시스템"** 입니다. VCS 에는 여러 종류가 있지만 이제 우리는 그 중에서 가장 많이 사용되는 VCS 인 `git` 을 간단하게 알아보겠습니다. `git` 을 익히면 제가 위에서 설명한 문제들이 다 해결되는 것입니다!

`git` 의 자세한 설명과 의미를 공부하기 위해서는 

https://git-scm.com/book/en/v2

https://ccss17.github.io/git.html

를 참고해주세요. 그리고 방학 때나 휴학을 했을 때 시간이 남으니까 `git` 의 `Branching` 기능까지 익혀두시길 **강력하게** 추천합니다. 왜냐면 여러분이 개발자로 살아가는 이상 **어차피 언젠가는 `git Branching` 기능까지 알아야만 하기 때문**입니다. 

- **`git` : 가장 인기있고 자주 사용되는 VCS 이다.**

  - `git` 은 파일을 **untracked 상태, modified 상태, staged 상태, committed 상태**로 관리한다.

## git 설치

> 만약 ~~없을 가능성이 높을테지만~~ 컴퓨터 운영체제로 `Linux` 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 `git` 를 설치할 수 있다고 믿습니다. 

### Windows git 설치

1. [이 링크](https://git-scm.com/download/win) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

2. `git` 을 설치한 후 가장 처음 해야 할 일은 초기 설정입니다. `git` 이 잘 설치되었다면 `Git Bash` 를 실행한 다음 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

    ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ git config --global user.name "<NAME>"
    $ git config --global user.email "<EMAIL>"
    ```

### MacOS git 설치

1. [이 링크](https://git-scm.com/download/mac) 에서 `git` 설치파일을 다운로드 받아서 설치하세요.

2. `git` 을 설치한 후 가장 처음 해야 할 일은 초기 설정입니다. 터미널을 열어서 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

    ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

    ```shell
    $ git config --global user.name "<NAME>"
    $ git config --global user.email "<EMAIL>"
    ```

### 우분투 도커 컨테이너에서 git 초기 설정

우분투 도커 컨테이너에서 접속하셔서 마찬가지로 `<NAME>, <EMAIL>` 을 본인의 이름과 이메일로 치환하여 다음 명령어를 입력해주세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git config --global user.name "<NAME>"
$ git config --global user.email "<EMAIL>"
```

## git 이 파일을 관리하는 상태

`git` 은 다음과 같은 상태로 파일들을 관리합니다. 이 상태들의 의미와 원리를 이해하면 조금 과장해서 `git` 을 이해했다고 볼 수 있습니다. 

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

### git 레포지토리 생성하기

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

# github

`github` 는 `git` 레포지토리를 다른 사람과 공유할 수 있는 플랫폼입니다. 이곳을 통하여 협업을 할 수 있기도 하고 자신이 관심있는 프로그램들이 무엇인지 알려줄 수도 있습니다.

> 최근에는 `github` 에 있는 그 사람의 레포지토리들을 포트폴리오로 취급하고 능력을 가늠해보기도 한다니까 `github` 에 레포지토리를 많이 공유하는 것이 좋을 것 같습니다.

## github 가입 

`github` 에 가입되어 있지 않으신 분들은 먼저 https://github.com/ 에서 가입을 해주세요.

## github 레포지토리 생성

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

# git 요약 

| 파일 상태 | 의미 |
|:---|:---|
|**untracked 상태**| `git` 이 변경사항을 추적하지 않는 파일이다.
|**modified 상태**| 파일을 변경했지만 아직 스테이징되지 않은 상태이다.|
|**staged 상태**| 변경된 파일을 커밋이 될 리스트에 포함시킨 상태이다.
|**committed 상태**| `git` 데이터베이스에 하나의 버전으로 저장된 상태이다.|

| `git` 명령어 | 하는 일 |
|:---|:---|
|**`git init`** | 디렉토리를 `git` 레포지토리로 만들어 디렉토리 내의 파일을 `git` 이 추적하게 한다.
|**`git status`** | `git` 레포지토리의 상태를 출력한다.
|**`git add <FILE>`** | `<FILE>` 을 스테이징한다.
|**`git commit`** | 스테이징된 파일들을 커밋하여 하나의 버전으로 만들어 `git` 데이터베이스에 저장한다.|
|**`git log`** | 커밋 기록을 출력한다.**|
|**`git remote add <NAME> <URL>`** | `<NAME>` 이라는 별칭으로 `<URL>` 의 원격 레포지토리를 등록한다.|
|**`git push <NAME> <BRANCH>`** | `<NAME>` 의 원격 레포지토리로 변경사항을 업데이트한다.
|**`git clone <URL> <NAME>`** | `<URL>` 의 원격 레포지토리를 가져와서 `<NAME>` 디렉토리에 복제한다.
|**`git pull <REMOTE> <BRANCH>`** | `<REMOTE>` 의 원격 레포지토리를 가져온 후 `<BRANCH>` 에 병합한다.

---

# VSCode

## VSCode 설치

> 만약 ~~없을 가능성이 높을테지만~~ 컴퓨터 운영체제로 `Linux` 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 `VSCode` 를 설치할 수 있다고 믿습니다.

### Windows 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=win64user) 에서 `VSCode` 설치파일을 다운로드 받아서 설치하세요.

### MacOS 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=osx) 에서 `VSCode` 설치파일을 다운로드 받아서 설치하세요.

## VSCode 간단 사용법 

> 참고 : https://code.visualstudio.com/docs

먼저 `git` 레포지토리를 `VSCode` 로 여는 두 가지 방법을 알아보겠습니다. 

### 로컬에서 레포지토리 만들기 

**여기서부터는 우분투 도커 컨테이너에서 작업하는 것이 아니라 로컬 컴퓨터에서 하겠습니다.** 일단 폴더(디렉토리)를 하나 만들고 그 폴더(디렉토리)를 `VSCode` 로 열어주세요.

지금까지 디렉토리를 `git` 레포지토리로 초기화할 때 디렉토리 위치에서 

```shell
git init
```

을 실행했었습니다. 하지만 이제 `VSCode` 에서 <kbd>Ctrl+Shift+p</kbd> 를 누르면 다음과 같이 `VSCode` 의 모든 기능이 담겨있는 **명령 팔레트** 가 나오는데 

![](https://code.visualstudio.com/assets/docs/getstarted/userinterface/commands.png)

여기에서 **git init** 만 입력하면 **Git: Initialize Repository** 가 검색되어 나옵니다. 그것에 커서가 포커싱되었다면 그냥 <kbd>Enter</kbd> 쳐주세요. 그러면 `VSCode` 가 알아서 디렉토리를 `git` 레포지토리로 초기화합니다.

- **<kbd>Ctrl+Shift+p</kbd> : `VSCode` 에서 명령 팔레트를 연다.**

  - 명령 팔레트는 `VSCode` 의 모든 기능을 실행할 수 있는 메뉴판이다.

- **<kbd>Git: Initialize Repository</kbd> : `VSCode` 명령 팔레트 기능으로써 디렉토리를 `git` 레포지토리로 자동으로 초기화한다.**

  - 명령 팔레트에서 git init 만 검색해도 나온다.

### 새 파일 만들고 저장하기

`VSCode` 에서는 <kbd>Ctrl+N</kbd> 으로 새 파일을 만들 수 있고 <kbd>Ctrl+S</kbd> 로 파일을 저장할 수 있습니다. 

- **<kbd>Ctrl+N</kbd> : `VSCode` 에서 새 파일을 만든다.**

- **<kbd>Ctrl+S</kbd> : `VSCode` 에서 파일을 저장한다.**

새 파일을 만들고 `test.txt` 로 저장해보세요.

### 변경된 파일 스테이징하고 커밋하기

그리고 이 파일을 스테이징하고 커밋을 해볼텐데, 마찬가지로 `VSCode` 의 **명령팔레트**를 열어서 `git commit` 을 입력해주세요. 

![2020-05-04_16-45](https://user-images.githubusercontent.com/16812446/80945381-abc5f480-8e26-11ea-9e78-ed054d64fbe2.png)

그러면 위와 같이 여러가지 커밋 기능들이 있는데 **Git: Commit All** 에 커서를 포커싱하고 <kbd>Enter</kbd> 를 눌러주세요. 그러면 `VSCode`가 변경된 모든 파일을 지알아서 스테이징하고 커밋합니다.

- **<kbd>Git: Commit All</kbd> : `VSCode` 명령 팔레트 기능으로써 변경된 모든 파일을 자동으로 스테이징하고 커밋한다.**

  - 이 기능을 터미널에서 손수 실행하려면 

    ```shell
    git add .
    git commit -m "message"
    ```

    를 다 쳐야 한다.

<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>g</kbd> 누르면 더 편함.

### 원격 레포지토리 등록하기

이제 레포지토리를 `Github` 에 공유하기 위하여 원격 레포지토리를 등록해보겠습니다. 앞서 `Github` 에 `git-test` 라는 원격레포지토리를 만들었었는데, 이제는 `git-test2` 라는 레포지토리를 만들고 오세요.

다 만들었다면 **명령 팔레트**를 열고 <kbd>git add</kbd> 만 쳐주세요. 그러면 다음 그림과 같이

![2020-05-04_16-53](https://user-images.githubusercontent.com/16812446/80945842-b9c84500-8e27-11ea-9d44-06d50cb56d5a.png)

<kbd>Git: Add Remote</kbd> 가 뜨고 <kbd>Enter</kbd> 를 치면 차례대로 **Remote Name** 과 **Remote URL** 을 입력하게 됩니다. 그럼 

```shell
git remote add origin https://github.com/<USER>/git-test2
``` 

를 입력했던 것처럼 각각 `origin` 을 입력하고 `https://github.com/<USER>/git-test2` 를 입력하면 되겠죠?

- **<kbd>Git: Add Remote</kbd> : `VSCode` 명령 팔레트 기능으로써 원격 레포지토리를 등록한다.**

### 원격 레포지토리로 공유하기

원격 레포지토리까지 등록했으니 이제 뭘 할까요. 공유를 해야죠? **명령 팔레트**를 열고 **git push** 만 입력해보세요.

![2020-05-04_16-58](https://user-images.githubusercontent.com/16812446/80946179-6b677600-8e28-11ea-89cc-17084c76b067.png)

그리고 위 그림과 같이 <kbd>Git: Push to...</kbd> 에 커서를 두고 <kbd>Enter</kbd> 를 치면 원격 레포지토리를 지정하는 단계로 넘어가는데 `origin` 밖에 없을테니 그냥 <kbd>Enter</kbd> 를 한번 더 치면 됩니다.

- **<kbd>Git: Push to...</kbd> : `VSCode` 명령 팔레트 기능으로써 원격 레포지토리로 변경사항을 업데이트한다.**

그러면 `VSCode` 가 지알아서 `git push origin master` 기능을 수행해줍니다. 각자의 **`https://github.com/<USER>/git-test2`** 로 들어가서 확인해보세요!

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

- **<kbd>Git: Clone</kbd> : `VSCode` 명령 팔레트 기능으로써 원격 레포지토리를 로컬로 가져온다.**

이제 다음과 같이 `test.txt` 에 `VScode 편하다. GBC 재밌다` 를 치고 <kbd>Ctrl+S</kbd> 를 눌러 저장하세요.

![2020-05-04_17-17](https://user-images.githubusercontent.com/16812446/80947401-137e3e80-8e2b-11ea-8e59-d79f9789897a.png)

그렇게 한 다음 지금까지 해온대로 **명령 팔레트** 에서 <kbd>Git: Commit All</kbd>, <kbd>Git: Push to...</kbd> 을 차례로 실행하세요. 그러면 원격 레포지토리로 업데이트됩니다. 너무 빠르고 쉽게 되죠?

### 원격 레포지토리로부터 업데이트하기

이제 원래의 레포지토리, 즉 `text.txt` 에 아무런 내용이 없는 원래의 레포지토리를 열어주세요. 그리고 **명령 팔레트**에서 **git pull** 만 치면 다음과 같이 <kbd>Git: Pull from...</kbd> 이 뜨는데 시원하게 <kbd>Enter</kbd> 를 쳐주세요.

![2020-05-04_17-19](https://user-images.githubusercontent.com/16812446/80947604-7a9bf300-8e2b-11ea-8064-26e3a9bf53aa.png)

그러면 원격 레포지토리를 선택할 수 있는 창이 뜨는데 어차피 `origin` 밖에 없으니까 <kbd>Enter</kbd> 를 다시 한 번 눌러주시면 `VSCode` 가 지알아서 `git pull origin master` 를 실행하면서 `text.txt` 를 업데이트합니다.

# VSCode 요약 

|VSCode 기능|하는 일|
|:---|:---|
|**<kbd>Ctrl+Shift+p</kbd>** | `VSCode` 에서 명령 팔레트를 연다.|
|**<kbd>Git: Initialize Repository</kbd>** | `VSCode` 명령 팔레트 기능으로써 디렉토리를 `git` 레포지토리로 자동으로 초기화한다.|
|**<kbd>Ctrl+N</kbd>** | `VSCode` 에서 새 파일을 만든다.|
|**<kbd>Ctrl+S</kbd>** | `VSCode` 에서 파일을 저장한다.|
|**<kbd>Git: Commit All</kbd>** | `VSCode` 명령 팔레트 기능으로써 변경된 모든 파일을 자동으로 스테이징하고 커밋한다.|
|**<kbd>Git: Add Remote</kbd>** | `VSCode` 명령 팔레트 기능으로써 원격 레포지토리를 등록한다.|
|**<kbd>Git: Push to...</kbd>** | `VSCode` 명령 팔레트 기능으로써 원격 레포지토리로 변경사항을 업데이트한다.|
|**<kbd>Git: Clone</kbd>** | `VSCode` 명령 팔레트 기능으로써 원격 레포지토리를 로컬로 가져온다.|
