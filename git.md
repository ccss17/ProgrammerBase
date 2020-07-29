# Git

---

# Table of Contents

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

- [Github](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github)

  - [Github 가입 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github-%EA%B0%80%EC%9E%85)

  - [Github 레포지토리 생성](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#github-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EC%83%9D%EC%84%B1)

  - [git 에서 레포지토리 공유](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EC%97%90%EC%84%9C-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B3%B5%EC%9C%A0)

  - [원격 레포지토리 가져오고 수정하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B3%A0-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0)

  - [수정된 원격 레포지토리로부터 업데이트하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EC%88%98%EC%A0%95%EB%90%9C-%EC%9B%90%EA%B2%A9-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%ED%95%98%EA%B8%B0)

- [더 빨라진 git](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-git)

- [Git 과 Github 못다한 이야기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-%EA%B3%BC-github-%EB%AA%BB%EB%8B%A4%ED%95%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0)

  - [.gitignore](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#gitignore)

    - [.gitignore 의 편리한 기능 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#gitignore-%EC%9D%98-%ED%8E%B8%EB%A6%AC%ED%95%9C-%EA%B8%B0%EB%8A%A5)

  - [Git Branching](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#git-branching)

    - [브랜치란? ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80)

    - [브랜치 생성](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%83%9D%EC%84%B1)

    - [브랜치 이주 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%9D%B4%EC%A3%BC)

    - [브랜치 병합 시나리오 (1) - Fast-forward](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B3%91%ED%95%A9-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-1---fast-forward)

    - [브랜치 병합 시나리오 (2) - Merge Conflict](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B3%91%ED%95%A9-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-2---merge-conflict)

    - [브랜치 삭제](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%82%AD%EC%A0%9C)

  - [user.github.io](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#usergithubio)

  - [hguappl.ghoster.cc/git/](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#hguappghosterccgit)

  - [gist](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#gist)

    - [gist 사용법 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#gist-%EC%82%AC%EC%9A%A9%EB%B2%95)

    - [gist 명령어 ](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#gist-%EB%AA%85%EB%A0%B9%EC%96%B4)

  - [Pull Request](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#pull-request)

    - [1. fork 하고 clone 하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#1-fork-%ED%95%98%EA%B3%A0-clone-%ED%95%98%EA%B8%B0)

    - [2. 편집하고 push 하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#2-%ED%8E%B8%EC%A7%91%ED%95%98%EA%B3%A0-push-%ED%95%98%EA%B8%B0)

    - [3. **pull request** 하기](https://github.com/ccss17/ProgrammerBase/blob/master/git.md#3-pull-request-%ED%95%98%EA%B8%B0)

---

## **<div align="center"> ☀️ ️여기서부터 Day2 내용입니다. ☀️ </div>**

# Git

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

> `git remote add` 가 `git add` 와 비슷하지만 스테이징하는 게 아니라 다만, 원격 레포지토리 URL 을 등록하는 것일 뿐입니다. `git remote add` 는 스테이징과 하등 상관없습니다.

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

> `git` 은 레포지토리의 변경사항을 평행적으로 관리하기 위하여 여러개의 브랜치 즉, 가지들을 생성합니다. 가령 프로젝트에 새로운 기능을 추가하고 싶은데 그 기능이 프로젝트 전체와 잘 어울리는지 장담할 수가 없으니까 새로운 브랜치를 만들어서 마치 평행세계처럼 완전히 새로운 레포지토리에서 작업하는 것입니다.

`git init` 으로 디렉토리가 `git` 이 관리하는 레포지토리가 될 때 `git` 은 자동적으로 현재 브랜치를 `master` 브랜치로 만들기 때문에, `git pull origin master` 라고 하면 **`origin` 이라는 원격 레포지토리의 내용을 가져와서 `master` 브랜치로 병합해라**는 뜻이 되는 것입니다.

그래서 방금 말했던 새로운 브랜치에서 시험중이었던 기능이 충분히 검증이 되면 `master` 브랜치로 병합을 하게 되는 것입니다. 

## **<div align="center"> 🌜 ️여기까지 Day2 내용입니다. 수고하셨습니다. 🌜️ </div>**

## **<div align="center"> ☀️ ️여기서부터 Day4 내용입니다. ☀️ </div>**

# 더 빨라진 git

`git` 은 지원하는 지능이 하도 많다보니 내부적으로 `alias` 를 지원합니다. 가령 `git commit -m` 이라는 명령어를 매번 입력하기가 너무 귀찮아서 견딜 수가 없으니까 다음 명령어를 입력하여 `alias` 를 지정할 수 있습니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g config --global alias.cm "commit -m"
```

> `zsh` 의 `alias` 에서 `alias g=git` 으로 `git` 의 에일리어스 `g` 를 설정했었기 때문에 `git` 이 아닌 `g` 만 입력해도 됩니다. 

그러면 이제부터 우리는 `git commit -m` 이 아니라 `g cm` 만 입력해도 되는 것입니다. 그런데 저의 `dotfiles` 를 설치하면서 이런 `git` 의 `alias` 들이 이미 `~/.gitconfig` 파일에 많이 설정되었습니다. 이 내용들을 확인하고 싶다면 

```shell
$ bat ~/.gitconfig
```

를 실행해보면 됩니다. `git` 의 `alias` 가 매우 많이 설정되어 있지만 그중에서 주요한 `alias` 들은 다음과 같습니다. 

<div align="center">

|`alias`|원래 명령어|완성된 명령어|의미|
|:---|:---|:---|:---|
|`i`|`init`|`g i`|`git` 레포지토리 관리를 시작하도록 한다.|
|`s`|`status`|`g s`|레포지토리 상태를 본다.|
|`sb`|`status -s -b`|`g sb`|레포지토리 상태를 간략하게 본다.|
|`cm`|`commit -m`|`g cm "<MESSAGE>"`|커밋을 한다.|
|`a`|`add --all`|`g a`|추가되거나 변경된 파일을 스테이징 한다.|
|`l`|`log --oneline`|`g l`|`git` 의 커밋 기록을 한줄씩 출력한다.|
|`lg`|`log --oneline --graph --decorate`|`g lg`|`git` 의 커밋 기록을 그래프로 출력한다.|
|`rao`|`remote add origin`|`g rao <REMOTE>`|원격 레포지토리를 추가한다.|
|`cl`|`clone`|`g cl <URL>`|원격 레포지토리를 복제해 온다.|
|`psom`|`push origin master`|`g psom`|원격 레포지토리로 푸쉬한다.|
|`plom`|`pull origin master`|`g plom`|원격 레포지토리를 가져온다.|
|`b`|`branch`|`g b <BRANCH>`|브랜치를 생성한다.|
|`bd`|`branch -d`|`g bd <BRANCH>`|브랜치를 삭제한다.|
|`m`|`merge`|`g m`|작업이 완료된 브랜치를 병합한다.|
|`o`|`checkout`|`g o <BRANCH>`|브랜치로 이동한다.|
|`ob`|`checkout -b`|`g ob <BRANCH>`|브랜치를 생성함과 동시에 이동한다.|

</div>

우리는 **2번째 날** `git` 을 연습할 때 `git-test` 디렉토리를 생성하고 그곳에서 여러가지 작업을 했습니다. 그때 입력한 명령어들을 쭉 나열해보면 다음과 같습니다. 

```shell
$ mkdir git-test
$ cd git-test
$ git init
$ touch test.txt
$ git status
$ git add test.txt
$ git status
$ git commit -m "my first commit"
$ git status
$ echo "My test memo" > test.txt
$ cat test.txt
My test memo
$ git add .
$ git commit -m "My memo file"
$ git log
$ git remote add origin https://github.com/<USER>/git-test
$ git push -u origin master
$ cd  
$ git clone https://github.com/<USER>/git-test git-test-remote
$ cd git-test-remote
$ echo "very important message" > test.txt
$ git add .
$ git commit -m "very important file.."
$ git push origin master
$ cd ~/git-test
$ cat test.txt
$ git pull origin master
$ cat test.txt
```

이제 새로운 레포지토리 `alias-test` 를 만들고 위 명령어들을 `alias` 로 단축해서 다시 입력해보겠습니다. 다음 명령어를 실행해보세요. 하지만 걱정하지마세요. `alias` 덕분에 생각보다 오래 안걸리니까요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd
$ mkdir alias-test
$ cd alias-test
$ g i
$ touch test.txt
$ g s
$ g a
$ g s
$ g cm "init"
$ g s
$ echo "My test memo" > test.txt
$ bat test.txt
$ g a
$ g cm "memo"
$ g l
$ g rao https://github.com/<USER>/alias-test
$ g psom
$ cd  
$ g cl https://github.com/<USER>/alias-test alias-test-remote
$ cd alias-test-remote
$ echo "message" > test.txt
$ g a
$ g cm "important file"
$ g psom
$ cd ~/alias-test
$ bat test.txt
$ g plom
$ bat test.txt
```

이로써 다음과 같이 `213` 타를 쳐야 했던 것을 `79` 타만 칠 수 있도록 대폭 절약을 해보았습니다.

<div align="center">

|원래 명령어|`alias` 명령어|
|:---|:---|
|`git init`|`g i`|
|`git status`|`g s`|
|`git add`|`g a`|
|`git status`|`g s`|
|`git commit -m`|`g cm `|
|`git status`|`g s`|
|`git add .`|`g a`|
|`git commit -m`|`g cm`|
|`git log`|`g l`|
|`git remote add`|`g rao`|
|`git push -u origin master`|`g psom`|
|`git clone`|`g cl`|
|`git add .`|`g a`|
|`git commit`|`g cm`|
|`git push origin master`|`g psom`|
|`git pull origin master`|`g plom`|
|**총합 `213` 개**|**총합 `79` 개**|

</div>

이러한 `git` 레포지토리 관리 패턴은 코딩을 할 때마다 반복되는데, 이 패턴을 개발자로 살아가면서 적게 잡아서 **10000** 번 반복한다고 한다면, 여러분은 **10000 * 213 = 2백 13만** 번 칠 것을 **10000 * 79 = 79만** 만쳤습니다. 

즉, 똑같은 일을 하는데 **134만** 번의 타자를 안 친것입니다!

## **<div align="center"> 🌜 ️여기까지 Day4 내용입니다. 수고하셨습니다. 🌜️ </div>**

## **<div align="center"> ☀️ ️여기서부터 Day5 내용입니다. ☀️ </div>**

# Git 과 Github 못다한 이야기

우리는 **Git** 과 **Github** 의 가장 기초적인 부분을 이미 다뤘었는데 여기에서는 **Git** 과 **Github** 에 관하여 아직 하지 못한 이야기를 해보겠습니다. 

## .gitignore

프로젝트를 진행하다보면 **Git** 이 추적하지 않았으면 하는 파일이 생깁니다. 가령 **C 언어** 프로그램을 코딩하다보면 컴파일된 바이너리 파일이 생기는데 그런 파일은 레포지토리에 포함시켜서는 안됩니다. 또 프로젝트에 대한 아이디어를 **idea.txt** 라는 파일에 기록해놓았다면 그 파일은 **Git** 이 추적하면서 레포지토리에 포함시키면 안 됩니다.

이런 파일들의 이름을 `.gitignore` 파일을 만들어서 기록해두면 **Git** 이 그 파일들을 더 이상 추적하지 않습니다. 즉 블랙리스트입니다.

- **`.gitignore` : 이 파일에 파일 이름을 넣으면 git 이 변경사항을 더 이상 추적하지 않는다.**

  - 가령 `idea.txt` 파일을 더 이상 추적하고 싶지 않고 싶다고 하겠습니다. 또 **C 언어** 소스가 컴파일된 바이너리 파일들을 `bin/` 디렉토리에 모아두었다면 이 디렉토리도 **Git** 이 더 이상 추적하면 안됩니다.

    이 경우 레포지토리에 `.gitignore` 파일을 만들어 다음과 같이 블랙리스트를 작성합니다. 

    ```.gitignore
    idea.txt
    bin/
    ```

    이렇게 하면 하위 디렉토리에서 `idea.txt` 가 생성되어도 **Git** 이 추적하지 않습니다. 

### .gitignore 의 편리한 기능 

하지만 프로젝트가 조금만 커져도 블랙리스트에 넣고 싶은 파일이 많아져서 `.gitignore` 에 작성해야할 블랙리스트 파일들이 너무 많아서 귀찮습니다. 그래서 `.gitignore` 는 특수문자를 통해 다음과 같은 편리한 기능을 제공합니다. 

<div align="center">

|작성 예시 | 기능 |
|:---|:---|
|`*.a`|모든 `.a` 파일들을 무시한다. |
|`!lib.a`|모든 `.a` 파일들을 무시하기로 했으나 `lib.a` 파일만 예외로 한다. |
|`/idea.txt`|현재 디렉토리의 `idea.txt` 만 무시한다. |
|`doc/*.txt`|`doc/notes.txt` 같이 `doc/` 디렉토리의 모든 `.txt` 파일을 무시한다.|
|`doc/**/*.txt`|`doc/` 디렉토리와 모든 하위 디렉토리의 `.txt` 파일을 무시한다.|

</div>

## Git Branching

> 참고/출처 : https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

프로젝트를 진행하면 새로운 기능을 추가할 때 그 기능이 전체 프로젝트와 호환되는지 알 수 없습니다. 개인 프로젝트라면 상관 없지만 함께 하는 프로젝트라면 걱정이 시작됩니다. **Git** 이 없을 때에는 이렇게 했습니다. 프로젝트를 통채로 복사하고 새로운 기능을 추가하고 호환되는지 충분히 검증한 다음에 원래의 레포지토리에 새로운 기능을 옮깁니다.

하지만 **Git** 은 이러한 과정을 자동화시켜주고 로그 기록으로 남기고 최악의 경우 복원하는 기능까지 제공합니다. 이것이 **Git** 의 **Branching** 기능입니다. 평행세계를 만드는 것입니다. 그리고 원래의 세계에서 평행세계로 넘어가서 그 세계에서 마음껏 실험적인 행동을 자행하는 것이죠. 그 평행세계가 바로 **Branch** 입니다. 

**Git** 은 최대한 **Branch** 를 자주만들고 **master** 브랜치로 병합하라고 권장합니다. 저도 **Branch** 를 만들고 **master** 브랜치에 병합하는 **습관** 을 평소에 들이라고 권고하고 싶습니다. 왜냐하면 **Git Branching** 기능으로 여러분의 개발 과정이 매우 매우 안정적으로 바뀔 것이기 때문입니다. 

### 브랜치란? 

그렇다면 브랜치란 대체 무엇인가요? 브랜치란 포인터입니다. 그러면 그 포인터는 무엇을 포인팅하고 있나요? 바로 커밋들을 포인팅하고 있습니다. **Git** 은 기본 브랜치로 **master** 브랜치를 갖고 있는데 이 **master** 브랜치는 언제나 마지막 커밋을 포인팅하고 있습니다. 실제로 커밋을 할 때마다 **master** 브랜치가 자동으로 마지막 커밋으로 포인팅을 변경해주고 있던 겁니다. 

> 엄밀히 말하면 `HEAD` 포인터가 포인팅하고 있는 브랜치는 커밋을 할 때마다 자동으로 마지막 커밋으로 이동하는 것입니다. 아래의 내용을 읽으면 자연히 이해할 수 있을 겁니다. 

### 브랜치 생성

그러면 이제 말로만 하지말고 직접 몸으로 부딪혀보면서 브랜치를 느껴보겠습니다. 브랜치란 포인터라고 했으므로 브랜치를 생선하는 것은 포인터를 만드는 것입니다. 

실습하고 싶은 분은 실습하고 싶은 다음 명령어로 **Git** 레포지토리를 하나 만들어주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ mkdir branch-test
$ cd branch-test
$ g i
$ touch main.c
$ v main.c
```

> 즉, 실습하고 싶지 않으면 하지 않아도 된다는 말입니다. 다만 꼭 정독해주세요. 

> 여러분의 도커 컨테이너에는 지금까지의 실습이 잘 진행되었다면 최소 3개의 **Git** 레포지토리가 있을 겁니다. 

그리고 `main.c` 에 다음과 같은 코드를 입력하고 저장하고 `vim` 을 종료하세요. 

```c
void main(){
  puts("what is branch?");
}
```

그리고 다음 명령어로 스테이징 후 커밋해주세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a
$ g cm "main.c"
```

이제 실제로 브랜치를 생성해보겠습니다. 

- **`git branch` : 현재 상주하고 있는 브랜치를 출력한다.**

- **`git branch <NAME>` : 새로운 브랜치 `<NAME>` 을 만든다.**

다음 명령어를 실행하여 `testing` 이라는 브랜치를 만드세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g b testing
```

> 우리는 alias 와 git alias 에서 각각의 단축키를 이미 알아보았습니다. 

그러면 다음과 같이 현재 커밋을 두 개의 포인터 `master` 와 `testing` 이 포인팅하고 있습니다.

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/two-branches.png" width="50%" height="auto">
</div>

> 위 그림은 이전의 커밋이 2개 있다는 것을 보여주지만 실제로 현재 우리의 레포지토리에는 커밋은 하나밖에 없습니다! 

아니 그럼 현재 우리가 어떤 브랜치에 상주하고 있는지 대체 어떻게 알 수 있는 것인가요? 그것은 바로 `HEAD` 라는 특별한 포인터로 알 수 있습니다.

- **`HEAD` : 현재 상주하고 있는 브랜치를 가르키는 포인터이다.**

  - 아니 그럼 또 `HEAD` 는 어떻게 알 수 있는 것입니까? **zsh** 을 사용하고 있다면 다음과 같이 프롬프트 우측에 `HEAD` 가 가르키고 있는 브랜치, 즉 현재 상주하고 있는 브랜치를 알 수 있습니다.

    ![](https://user-images.githubusercontent.com/16812446/82705303-67ee3e80-9cb2-11ea-9a66-096c35c4af92.png)

    하지만 굳이 현재 상주하고 있는 브랜치를 직접 알아내야 한다면 `g b` 또는 `cat .git/HEAD` 를 입력하면 됩니다. `git branch` 명령이 현재 상주하고 있는 브랜치를 출력하므로 `g b` 가 `HEAD` 의 내용을 출력해주는 것입니다. 
  
우리는 다음과 같이 아직 `master` 브랜치에 상주하고 있습니다. 

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/head-to-master.png" width="50%" height="auto">
</div>

### 브랜치 이주 

이제 `testing` 브랜치로 이주해서 온갖 실험적이고 진취적인 행동을 마음껏 해야겠습니다. 그러려면 `testing` 브랜치로 이주해야만 합니다. 

- **`git checkout <NAME>` : `<NAME>` 브랜치로 이주한다.**

- **`git checkout -b <NAME>` : `<NAME>` 브랜치를 생성함과 동시에 이주한다.**

  - 이 형태가 가장 자주 쓰입니다. 즉 `g ob <NAME>` 이 자주 쓰입니다. 

다음 명령을 실행하여 브랜치를 이주하세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g o testing
```

그러면 다음과 같이 `HEAD` 포인터가 `testing` 을 가르키게 됩니다.

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/head-to-testing.png" width="50%" height="auto">
</div>

좋습니다! 이제 평행세계로 이동한 것입니다. 마음껏 실험적이고 파괴적인(?) 행동을 할 수 있습니다. `main.c` 함수의 코드에 매우 실험적이고 새로운 기능을 추가하고 싶다고 하겠습니다. 다음과 같이 코드를 고쳐주세요.

```c
void message(){
  puts("branch is good");
}
void main(){
  message();
}
```

새로 추가한 함수가 너무 실험적이고 진취적이어서 본래의 레포지토리와 호환되는지 알 수 없을 것만 같습니다. 하지만 이곳은 `testing` 브랜치니까 아무런 걱정이 안됩니다. 이제 코드를 저장하고 다음 명령을 실행하여 커밋하세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a 
$ g cm "new function"
```

그러면 `testing` 브랜치는 다음과 같이 마지막 커밋을 포인팅하게 위하여 앞으로 나아갔지만 `master` 브랜치는 가만히 멈추어 있습니다. 

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/advance-testing.png" width="50%" height="auto">
</div>

이제 다음 명령어로 `master` 브랜치로 되돌아갑니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g o master
```

그러면 다음과 같이 `HEAD` 가 `master` 로 옮겨갔습니다. 

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/checkout-master.png" width="50%" height="auto">
</div>

실제로 다음 명령어로 `main.c` 파일을 확인해보면 `testing` 브랜치에서 수정한 파일이 아닌 원래의 파일을 볼 수 있습니다.

```shell
$ bat main.c
```

### 브랜치 병합 시나리오 (1) - Fast-forward

브랜치 병합은 두 가지 시나리오로 설명하겠습니다. 우선 첫번째 시나리오입니다.

이제 `testing` 브랜치에서 작업한 내용이 완전히 검증되었다고 하겠습니다. 그러면 남은 일은 `master` 브랜치에서 `testing` 브랜치를 병합하는 것입니다.

- **`git merge <NAME>` : `<NAME>` 브랜치를 현재의 브랜치로 병합한다.**

다음 명령어로 브랜치를 병합해주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g m testing
```

![powershell_faVuEHeNG7](https://user-images.githubusercontent.com/16812446/82707007-22cc0b80-9cb6-11ea-9c25-f82c6d669dad.png)

커밋 구조를 보면 `master` 브랜치가 `testing` 브랜치 바로 뒤에 있기 때문에 이 경우 **Git** 은 단순히 `master` 브랜치가 `testing` 브랜치가 포인팅하고 있는 커밋을 포인팅하게 합니다. 이것을 **Fast-forward** 병합이라고 합니다. 

### 브랜치 병합 시나리오 (2) - Merge Conflict

이제 다시 `testing` 브랜치에서 `master` 브랜치로 되돌아온 상황입니다. 이 경우 `master` 브랜치에서 `main.c` 를 다음과 같이 고쳤다고 하겠습니다. 

```c
void main(){
  puts("branch is good");
}
```

그런 다음 다음 명령어로 스태이징을 하고 커밋을 합니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a  
$ g cm "new main"
```

그러면 현재 상황은 다음과 같습니다. 

<div align="center">
<img src="https://git-scm.com/book/en/v2/images/advance-master.png" width="50%" height="auto">
</div>

`master` 브랜치도 한 단계 더 나아갔습니다. 이 상황에서 다음의 명령어로 `testing` 브랜치를 병합합니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g m testing
Auto-merging main.c
CONFLICT (content): Merge conflict in main.c
Recorded preimage for 'main.c'
Automatic merge failed; fix conflicts and then commit the result.
```

그러면 `main.c` 에 병합 충돌이 발생했다는 메시지가 발생하면서 자동 병합에 실패하게 됩니다. 이 메시지가 발생하면 정확하게 `git status` 명령어로 어떤 파일에서 충돌이 발생한 것인지 확인해야 합니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g s
```

그러면 다음과 같이 **both modified:** 에 해당하는 파일 목록이 출력되는데 그 목록에는 `main.c` 가 포함되어 있음을 알 수 있습니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82708683-d387da00-9cb9-11ea-84a4-35a1a0779b19.png" width="70%" height="auto">
</div>

이 경우 `main.c` 를 열어서 병합 충돌이 발생한 코드를 확인해주어야 합니다. 실제로 `main.c` 를 열어보면 다음과 같이 되어있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82708726-eac6c780-9cb9-11ea-8327-bc41adb9ceba.png" width="70%" height="auto">
</div>

병합충돌이 발생하면 **Git** 은 위와 같이 자동으로 충돌 영역을 `=======` 로 구분해줍니다. 그리고 `HEAD` 가 가르키는 브랜치(`master`)의 변경사항과 `testing` 브랜치의 변경사항을 비교하여 보여줍니다. `HEAD` 에서 변경된 부분은 `<<<<<<< HEAD` 에서부터 `=======` 까지이고 `testing` 브랜치에서 변경된 부분은 `=======` 부터 `>>>>>>> testing` 까지입니다. 정말 편하죠? 

여러분은 두 변경사항 중 하나를 택하거나 둘 다 택하여 `<<<<<<<` 와 `=======` 그리고 `>>>>>>>` 를 없애주어야 합니다. 여기에서는 `main.c` 를 다음과 같이 고쳐주겠습니다. 

```c
void message(){
  puts("branch is good.");
}
void main(){
  message();
}
```

그런 다음 다음 명령어로 다시 커밋해주면 병합이 최종적으로 완성됩니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a
$ g cm "merge testing"
```

### 브랜치 삭제 

이제 마지막으로 병합이 완료된 `testing` 브랜치를 삭제하는 일만 남았습니다. 

- **`git branch -d <NAME>` : 병합이 완료된 `<NAME>` 브랜치를 삭제한다.**

- **`git branch -D <NAME>` : 병합이 완료되지 않은 `<NAME>` 브랜치를 삭제한다.**

다음 명령어로 `testing` 브랜치를 삭제하세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g bd testing
```

> 지금까지 **Git Branching** 을 매우 간단하게 알아보았는데, 나중에 https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell 을 통하여 **Git Branching** 의 더욱 강력한 기능을 추가 학습하시길 강력하게 추천합니다.

> **VSCode** 에서는 왼쪽 하단부의 **Branch** 를 클릭하거나 명령 팔레트에서 **branch** 를 검색하는 것으로 매우 쉽게 **Branch** 를 생성하거나 이주할 수 있습니다.

## user.github.io

user.github.io 은 **Github** 이 제공하는 개인 블로그 플랫폼입니다. 저의 **Github** 아이디는 `ccss17` 인데 이 아이디로 user 를 치환하여 https://ccss17.github.io 에 접속해보면 제가 관리하고 있는 블로그가 보입니다. 이 블로그는 https://github.com/ccss17/ccss17.github.io 의 `index.html` 파일과 각각의 `*.html` 파일들이 랜더링 된 것입니다. 

이처럼 **Github** 에 아이디만 있다면 자신의 아이디로 user.github.io 라는 이름을 가진 레포지토리를 생성하고 그곳에 `index.html` 과 메모하거나 게시하고 싶은 정보를 `.html` 파일로 만들어 레포지토리를 **commit** 하고 **Github** 에 **push** 하면 자동으로 user.github.io 에 게시가 시작됩니다. 

> [**jekyll**](https://jekyllrb.com/) 을 사용하면 `.md` 파일만으로도 웹페이지를 생성할 수 있어 매우 편합니다. 

개인 블로그에 자신이 공부한 내용이나 알아낸 사실을 게시하면 그것이 모두 다 포트폴리오가 되고 스펙이 되서 자신의 가치를 높이는 일이 됩니다. 그러나 이 블로그 플랫폼을 사용하고 싶지 않은 분들도 있음을 감안해서 더 이상의 상세한 설명과 실습은 하지 않고 유명한 `*.github.io` 사이트들과 **Github** 의 공식 메뉴얼과 저의 https://ccss17.github.io 를 가볍게 보여드리는 것으로 마무리 하겠습니다. 

- **Github** 페이지 공식 메뉴얼 : https://pages.github.com/

- [sindresorhus](https://github.com/sindresorhus) 의 [블로그](https://sindresorhus.com/) : https://github.com/sindresorhus/sindresorhus.github.com

- [도커 가이드](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html) : https://github.com/subicura/subicura.github.io 

## hguapp.ghoster.cc/git/

hguapp.ghoster.cc/git/

(한동대 컴퓨터보안 동아리 고스트의 사설 깃허브. 도커로 운영중.)

## gist

[gist](https://gist.github.com/) 는 짤막한 파일을 빠르게 공유할 때 사용되는 **Github** 의 레포지토리 관리 플랫폼입니다. 

실제로 저는 강의평가 설문조사 때 그 수많은 강의에 대한 평가가 약간 귀찮아서 다음과 같은 자동으로 최고 평점을 매길 수 있는 **Javascript** 코드를 짰었습니다. 

```javascript
for (let v of document.getElementsByTagName('input')){
  if(v.getAttribute('name').includes('ans') &&
     (v.getAttribute('value') == 5 || 
     v.getAttribute('value') == 10 || 
     v.getAttribute('value') == 15))
    v.click();
}
```

하지만 이 코드 또한 카톡이나 메일로 관리할 수는 없으니 **Git** 같은 VCS 를 사용해야 할텐데, 레포지토리로 관리하자니 이렇게 짧은 코드를 그렇게까지 관리해야 한다는 것이 억울했습니다. 그래서 [gist 로 관리하는 레포지토리](https://gist.github.com/ccss17/ff6944df7e8f3c9ab518629915857d85)를 하나 만들었습니다.

### gist 사용법 

[gist](https://gist.github.com/) 사용법은 매우 간단합니다. https://gist.github.com/ 에 들어가면 다짜고짜 제목과 파일이름 내용을 입력하는 텍스트 필드가 나오는데 이 3가지 텍스트 필드를 입력하고 <kbd>Create secret gist</kbd> 또는 <kbd>Create public gist</kbd> 버튼을 누르면 그게 다입니다. 그러면 **gist** 가 생성되는데 URL 을 다음과 같이 어디에서든 **clone** 할 수 있습니다. 

```shell
$ g cl https://gist.github.com/ccss17/ff6944df7e8f3c9ab518629915857d85
```

이 **gist** 또한 **staging**, **commit**, **push** 등등이 모두 다 가능한 **Git** 레포지토리와 똑같이 다룰 수 있습니다.

### gist 명령어 

**gist** 를 매우 쉽게 사용할 수 있게 해주는 [`gist`](https://github.com/defunkt/gist) 명령어가 있습니다. 이 명령어를 사용하는 방법은 매우 간단합니다. 

> 여러분의 도커 컨테이너에는 이미 설치되어 있으니 설치할 필요가 없습니다. 설치법은 공식 레포지토리 https://github.com/defunkt/gist 를 참고하세요.

1. `gist --login` 으로 **Github** 아이디와 비밀번호를 입력하여 인증과정을 거친다. 이 과정은 단 한 번만 거치면 된다. 

2. `gist <FILE>` 로 **gist** 에 업로드하고 싶은 파일을 업로드한다. 

    - `test.py` 를 **gist** 에 공유하고 싶다면 `gist test.py` 를 입력하면 끝이다.

## Pull Request

**Github** 협업하기의 기본인 **Pull Request** 는 말 그대로 **pull** 해주기를 요청하는 것입니다. 주로 같이 프로젝트를 하는 사람끼리 **Pull Rquest** 를 하지만, **Github** 에서 오픈소스를 많이 찾아다니면서 마음이 드는 오픈소스를 사용하다가 그것을 발전시키고 싶다면 그 레포지토리를 좀 더 낫게 고친 다음 원작자에게 **Pull Request** 를 할 수도 있습니다. 이러한 오픈소스 활동은 전세계에서 수없이 많이 이루어지고 있습니다. 여러분도 이 오픈소스 활동에 참여하여 여러분만의 창의성을 발휘해서 프로그램을 발전시킨 다음 **Pull Request** 를 꾸준히 한다면 여러분의 실력과 명성도 꾸준히 쌓여나갈 것입니다. 

**그렇다면 오픈소스를 어떻게 찾는 것일까요? 질문을 좀 더 일반적으로 바꾸어서 최신 정보와 좋은 정보를 어디에서 찾을 수 있는 것일까요. 그리고 이런 오픈소스 프로젝트에 실질적으로 참여하게 해주는 **Pull Request** 라는 것은 어떻게 하는 것일까요?**

먼저 후자의 질문에 대한 대답을 배워보겠습니다. **Pull Requests** 의 과정은 다음과 같습니다.

1. **fork** 하고 **clone** 하기

2. **편집** 하고 **push** 하기

3. **pull request** 하기

이제 이 과정을 제가 **Pull Request** 를 마음껏 연습할 수 있도록 만든 레포지토리 https://github.com/ccss17/pull-request-me 에서 실습해보겠습니다. 

### 1. fork 하고 clone 하기

그러면 https://github.com/ccss17/pull-request-me 에 들어가서 오른쪽 상단부를 보세요. 그러면 다음과 같이 <kbd>Fork</kbd> 버튼이 보입니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82676804-eda5c600-9c81-11ea-8089-0668f53c5072.png" width="70%" height="auto">
</div>

이 버튼을 시원하게 눌러주세요. 그러면 다음과 같이 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82677048-5ee57900-9c82-11ea-99f5-3567455581bc.png" width="70%" height="auto">
</div>

레포지토리가 자신의 소유의 레포지토리로 복제됩니다. 여기에서는 **hgu-student** 라는 아이디를 갖고 있는 학생이 레포지토리를 **fork** 해왔습니다. **fork** 된 레포지토리의 **URL** 도 원래의 **URL** 인 https://github.com/ccss17/pull-request-me 에서 https://github.com/hgu-student/pull-request-me 로 바뀌었습니다. 이제 이것을 로컬 컴퓨터로 **clone** 합니다. 지금까지 배웠던 **Git** 의 명령어를 다음과 같이 사용하면 됩니다. **hgu-student** 라는 **Github** 아이디를 갖고 있는 학생이라면 다음과 같은 명령어를 입력하면 됩니다.

```shell
$ g cl https://github.com/hgu-student/pull-request-me
```

이제 각자 **fork** 한 자신의 레포지토리를 다음 명령어를 입력해서 **clone** 해주세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g cl https://github.com/<USER>/pull-request-me
```

도커 컨테이너에서 해도 되고 로컬 컴퓨터에서 **VSCode** 로 해도 됩니다.

### 2. 편집하고 push 하기

레포지토리를 **clone** 해보면 `readme.md` 와 `main.c` 파일이 보입니다. 여기에서는 여러분이 `main.c` 를 살펴보다가 코드 포맷이 상당히 마음에 들지 않았다고 가정하겠습니다. 실제로 다음과 같이 `main.c` 를 여러보니 코드 포맷이 엉망입니다. 

> 그리고 심지어 함수의 인자를 빈 괄호 `()` 로 두는 것은 [안정성의 이유 때문에 권고되지 않습니다](https://stackoverflow.com/questions/3156423/why-dont-we-use-void-in-main). 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82677543-25613d80-9c83-11ea-9123-4bc9d8a8407e.png" width="70%" height="auto">
</div>

그래서 여러분은 이 코드를 다음과 같이 고치려고 마음먹었습니다. 

```c
int main(void) 
{
    printf("main :)\n");
    return 0;
}
```

> `vim` 으로 고치든 **VSCode** 로 고치든 그것은 알아서 선택해주세요. 

그런 다음 다음과 같이 지금까지 배웠던 **Git** 명령으로 **staging**, **commit**, **push** 를 합니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a 
$ g cm "메인 함수를 고침!"
$ g psom
```

### 3. **pull request** 하기

그런데 여러분의 레포지토리가 업데이트 되었을 뿐 원작자의 레포지토리가 업데이트 된 것은 아닙니다. 그래서 원작자에게 어서 빨리 내 레포지토리를 **pull** 해주세요 라고 말하기 위하여 **Pull Request** 를 합니다. 다음 사진과 같이 자신의 레포지토리의 왼쪽 상당부를 보면 <kbd>Pull requests</kbd> 탭이 있습니다. 이 탭을 눌러 **Pull Request** 페이지로 들어갑니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82678481-a5d46e00-9c84-11ea-8724-2104619a9622.png" width="70%" height="auto">
</div>

**Pull Request** 페이지의 오른쪽 상단부에는 다음과 같이 <kbd>New</kbd> 버튼이 있습니다. 이 버튼을 눌러 드디어 원작자에게 보낼 **Pull Request** 를 생성해줍니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82678642-e9c77300-9c84-11ea-8e97-9c32244d222a.png" width="70%" height="auto">
</div>

그러면 마지막으로 내가 편집한 레포지토리와 원작자의 레포지토리를 비교할 수 있고 어떤 브랜치로 **Pull Request** 를 할 것인지 선택하는 페이지가 보입니다. 지금은 그냥 왼쪽에 보이는 <kbd>Create pull request</kbd> 버튼을 눌러줍시다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82678798-2f843b80-9c85-11ea-8fa8-91aa00201baa.png" width="70%" height="auto">
</div>

그러면 **Pull Request** 의 제목과 설명을 할 수 있는 텍스트 필드가 나타나는데, 지금은 역시 그냥 텍스트 필드 우측 하단에 있는 <kbd>Create pull request</kbd> 버튼을 한번 더 눌러주세요. 

그러면 이제 정말 **Pull Request** 가 완료되었습니다. 이제 원작자가 여러분이 멋지게 고친 레포지토리를 비교하고 괜찮다고 판단하여 **pull** 을 하기만을 기다리면 됩니다. 

## **<div align="center"> 🌜 ️여기까지 Day5 내용입니다. 수고하셨습니다. 🌜️ </div>**
