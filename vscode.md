
# This reposity has been abandoned. Please see https://ccss17.github.io/ProgrammerBase

# 이 레포지토리는 더 이상 관리되지 않습니다. https://ccss17.github.io/ProgrammerBase 에 방문해주세요.

# VSCode

---

# Table of Contents

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

- [VSCode 업그레이드 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C)

  - [테마 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%85%8C%EB%A7%88)

    - [기본 테마](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EA%B8%B0%EB%B3%B8-%ED%85%8C%EB%A7%88)

    - [Dank Neon](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#dank-neon)

    - [Andromeda](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#andromeda)

    - [2077](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#2077)

    - [Eva Theme](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#eva-theme)

    - [Cyberpunk](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#cyberpunk)

    - [지평선](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%A7%80%ED%8F%89%EC%84%A0)

    - [SynthWave '84](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#synthwave-84)

  - [유용한 확장 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%9C%A0%EC%9A%A9%ED%95%9C-%ED%99%95%EC%9E%A5)

    - [Git Lens](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#git-lens)

    - [Git Graph](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#git-graph)

    - [Code Runner](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#code-runner)

    - [PDF](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#pdf)

    - [mdmath](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#mdmath)

    - [Bracket Pair Colorizer 2](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#bracket-pair-colorizer-2)

    - [Prettier - Code formatter](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#prettier---code-formatter)

    - [Diff Tool](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#diff-tool)

    - [Material Icon Theme](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#material-icon-theme)

    - [Glassit-VSC](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#glassit-vsc)

- [VSCode Vim](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-vim)

  - [단축키](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%8B%A8%EC%B6%95%ED%82%A4)

- [VSCode Vim 예시](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-vim-%EC%98%88%EC%8B%9C)

  - [Python - List to Dictionary](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python---list-to-dictionary)

  - [Python - copy & paste](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python---copy--paste)

  - [Python - multi cursor](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python---multi-cursor)

  - [Python - rename argument](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python---rename-argument)

  - [C 언어 - 변수 한 줄로 선언하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#c-%EC%96%B8%EC%96%B4---%EB%B3%80%EC%88%98-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0)

  - [Markdown - example 1](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#markdown---example-1)

  - [Markdown - example 2](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#markdown---example-2)

  - [Python - multicursor](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python---multicursor)

  - [Markdown - example 3](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#markdown---example-3)

- [VSCode 디버깅 ](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-%EB%94%94%EB%B2%84%EA%B9%85)

  - [Python 디버깅](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#python-%EB%94%94%EB%B2%84%EA%B9%85)

- [VSCode 와 Docker 로 머신러닝 공부하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-%EC%99%80-docker-%EB%A1%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EA%B3%B5%EB%B6%80%ED%95%98%EA%B8%B0)

  - [파이썬으로 배우는 기계학습](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EA%B8%B0%EA%B3%84%ED%95%99%EC%8A%B5)

  - [로컬 데이터셋 사용하기](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EB%A1%9C%EC%BB%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

  - [컴퓨터를 재부팅 했을 때](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#%EC%BB%B4%ED%93%A8%ED%84%B0%EB%A5%BC-%EC%9E%AC%EB%B6%80%ED%8C%85-%ED%96%88%EC%9D%84-%EB%95%8C)

- [VSCode Snippets](https://github.com/ccss17/ProgrammerBase/blob/master/vscode.md#vscode-snippets)

---

## **<div align="center"> ☀️ ️여기서부터 Day2 내용입니다. ☀️ </div>**

# VSCode

여기에서는 **VSCode** 에 대하여 알아보겠습니다. 도커 컨테이너가 아니라 로컬에서 실습하면 됩니다. 

## VSCode 설치

> 만약 컴퓨터 운영체제로 **Linux** 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 **VSCode** 를 설치할 수 있다고 믿습니다.

### Windows 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=win64user) 에서 **VSCode** 설치파일을 다운로드 받아서 설치하세요.

### MacOS 설치

1. [이 링크](https://code.visualstudio.com/docs/?dv=osx) 에서 **VSCode** 설치파일을 다운로드 받아서 설치하세요.

## VSCode 간단 사용법 

> 참고/출처 : https://code.visualstudio.com/docs

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

- **<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> or <kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> : VSCode 에서 명령 팔레트를 연다.**

  - 명령 팔레트는 **VSCode** 의 모든 기능을 실행할 수 있는 메뉴판이다.

- **<kbd>Git: Initialize Repository</kbd> : **VSCode** 명령 팔레트 기능으로써 디렉토리를 `git` 레포지토리로 자동으로 초기화한다.**

  - 명령 팔레트에서 git init 만 검색해도 나온다.

### 새 파일 만들고 저장하기

**VSCode** 에서는 <kbd>Ctrl</kbd>+<kbd>n</kbd> 으로 새 파일을 만들 수 있고 <kbd>Ctrl</kbd>+<kbd>s</kbd> 로 파일을 저장할 수 있습니다. 

- **<kbd>Ctrl</kbd>+<kbd>n</kbd> or <kbd>command</kbd>+<kbd>n</kbd> : **VSCode** 에서 새 파일을 만든다.**

- **<kbd>Ctrl</kbd>+<kbd>s</kbd> or <kbd>command</kbd>+<kbd>s</kbd> : **VSCode** 에서 파일을 저장한다.**

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
|파일 열기|<kbd>Ctrl</kbd>+<kbd>p</kbd> + <kbd>command</kbd>+ <kbd>p</kbd>|

**VSCode** 에서 파일을 열 때 왼쪽 **Explorer** 패널에서 파일을 클릭하여 열 수도 있지만 <kbd>Ctrl</kbd>+<kbd>p</kbd> 를 누르고 파일 이름을 입력하면 매우 빠르게 파일을 열 수 있습니다.

- 예시 

  코딩을 하다가 `memdump.c` 파일을 열어보고 싶어졌습니다. 그러면 왼쪽 **Explorer** 패널에서 클릭하여 열 수도 있지만, 다음과 같이 <kbd>Ctrl</kbd>+<kbd>p</kbd> 단축키를 사용할 수 있습니다.
  
  먼저 <kbd>Ctrl</kbd>+<kbd>p</kbd> 누르고 그 파일의 이름을 특정할 수 있는 문자열 `memd` 까지만 칩니다. 그러면 `memdump.c` 파일이 검색되어 나오는데 이제 그냥 <kbd>Enter</kbd> 를 치면 됩니다. 

  ![yaGfFjdSHi](https://user-images.githubusercontent.com/16812446/82407559-6818ef00-9aa4-11ea-959f-333c1f735b9a.gif)


### 파일 닫기 

|기능|단축키|
|:---:|:---:|
|파일 닫기|<kbd>Ctrl</kbd>+<kbd>w</kbd> or <kbd>command</kbd>+<kbd>w</kbd>|

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
|화면 오른쪽으로 분할하여 옮기기|<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&rarr;</kbd> or <kbd>command</kbd>+<kbd>k</kbd>+<kbd>&rarr;</kbd>|
|화면 왼쪽으로 분할하여 옮기기|<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&larr;</kbd> or <kbd>command</kbd>+<kbd>k</kbd>+<kbd>&larr;</kbd>|

코딩을 하다보면 두 파일을 같이 보고싶을 때가 있습니다. 그럴 때 마우스로 화면을 오른쪽이나 왼쪽으로 이동시키면 **VSCode** 가 자동으로 화면을 분할해주지면 위 단축키를 이용하면 훨씬 더 빠르게 화면을 분할하여 옮길 수 있습니다.

- 예시 

  `kaslr.c` 와 `memdump.c` 파일을 열고 작업하고 있었습니다. 그런데 이때 `memdump.c` 를 오른쪽 화면으로 옮기고 싶어져서 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>&rarr;</kbd> 를 눌렀습니다.

  ![UXMBh2K8so](https://user-images.githubusercontent.com/16812446/82408373-6819ee80-9aa6-11ea-9aad-1cd2c5dce277.gif)

### 분할된 화면 포커싱 

|기능|단축키|
|:---:|:---:|
|오른쪽 화면 포커싱|<kbd>Ctrl</kbd>+<kbd>1</kbd> |
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
|화면 레이아웃 변경|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>0</kbd> or <kbd>option</kbd>+<kbd>command</kbd>+<kbd>0</kbd>|

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

## **<div align="center"> 🌜 ️여기까지 Day2 내용입니다. 수고하셨습니다. 🌜️ </div>**

## **<div align="center"> ☀️ ️여기서부터 Day4 내용입니다. ☀️ </div>**

# VSCode 업그레이드 

`vim` 이 일반 에디터보다 좋다고 생각했다면 앞으로 `vim` 을 쓰기로 결정했을 겁니다. 하지만 `vim` 은 아무래도 CLI 의 범주에 속하다 보니까 아무리 좋은 플러그인들을 많이 사용해도 GUI 에디터들이 제공하는 편리한 인터페이스와 수많은 디버깅 기능들과 수많은 플랫폼별 개발 환경들이 지원되지 않습니다. 

하지만 **VSCode** 를 사용하면 **VSCode** 확장과 편리한 코드 찾기 기능, 편리한 디버깅 기능들을 사용할 수 있습니다. **VSCode** 확장 중에는 `vim` 도 있어서 **VSCode** 에서 `vim` 을 사용할 수도 있습니다.

**VSCode** 가 지원하는 Git 은 지난시간에 이미 알아보았습니다. 뿐만 아니라 **안드로이드, 아두이노, 웹 개발, Python, Java, C/C++, C#, Rust, 주피터 노트북** 등등 상상할 수 있는 모든 플랫폼을 **VSCode** 에서 매우 편하게 사용할 수 있는 확장이 마련되어 있습니다. 

이 중에서 몇가지 핵심적인 기능만 좀 더 알아보겠습니다. 

## 테마 

가장 먼저 역시 테마입니다. 눈이 먼저 즐거워야 공부도 잘되고 개발도 잘되더라구요. 하지만 이 파트는 **실용성이 전혀 없기 때문에 실습하지 않아도 되고 시간이 아깝다면 넘겨도 됩니다**.

**VSCode** 는 수많은 테마를 지원합니다. 그 중에서 여러분 마음에 꼭 드는 테마가 분명히 있을거에요. 다음 링크는 **VSCode** 의 확장 마켓플레이스에서 `theme` 으로 검색했을 때 나오는 결과입니다. 

- https://marketplace.visualstudio.com/search?term=theme&target=VSCode&category=All%20categories&sortBy=Relevance

한번 들어가서 마음에 드는 테마가 있는지 찾아보세요. 여기에서는 상위에 랭크된 몇 가지 테마를 소개해드리겠습니다. 

테마는 <kbd>File</kbd> &rarr; <kbd>Preferences</kbd> &rarr; <kbd>Color Theme</kbd> 에서 바꿀 수 있습니다. 또는 단축키 <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>Ctrl</kbd>+<kbd>t</kbd> 를 눌러도 됩니다. 

> 밝은 테마는 전혀 관심이 없어서 추천을 못해드리지만 밝은 테마도 정말 많이 있습니다!

### 기본 테마

다음 사진은 **VSCode** 의 기본 테마입니다. 

<img src="https://user-images.githubusercontent.com/16812446/82316911-7b767c80-9a08-11ea-814d-ea2868564b04.png" width="70%" height="auto">

물론 기본테마가 마음에 든다면 계속 쓰셔도 상관없습니다. 

### Dank Neon

다음 사진은 [**Dank Neon**](https://marketplace.visualstudio.com/items?itemName=wuz.dank-neon) 테마입니다.

<img src="https://user-images.githubusercontent.com/16812446/82317397-25560900-9a09-11ea-9585-d86e1fc6a7dc.png" width="70%" height="auto">

### Andromeda

다음 사진은 [**Andromeda**](https://marketplace.visualstudio.com/items?itemName=EliverLara.andromeda) 테마입니다.

![Screenshot from 2020-05-30 07-06-52](https://user-images.githubusercontent.com/16812446/83309406-21fe2100-a244-11ea-9609-e972b693eedb.png)

### 2077

다음 사진은 [**2077**](https://marketplace.visualstudio.com/items?itemName=Endormi.2077-theme) 테마입니다.

![Screenshot from 2020-05-30 07-07-52](https://user-images.githubusercontent.com/16812446/83309441-3cd09580-a244-11ea-91cc-999c9e379ad1.png)

### Eva Theme

다음 사진은 [**Eva Theme**](https://marketplace.visualstudio.com/items?itemName=fisheva.eva-theme) 테마입니다.

<img src="https://user-images.githubusercontent.com/16812446/82318292-921dd300-9a0a-11ea-82b8-ebd62be28e35.png" width="70%" height="auto">

### Cyberpunk

다음 사진은 [**Cyberpunk**](https://marketplace.visualstudio.com/items?itemName=max-SS.cyberpunk) 테마입니다.

![Screenshot from 2020-05-30 07-10-04](https://user-images.githubusercontent.com/16812446/83309556-8b7e2f80-a244-11ea-81bb-9cde5f247312.png)

![Screenshot from 2020-06-02 09-56-27](https://user-images.githubusercontent.com/16812446/83468277-49105900-a4b7-11ea-9d93-bc3b7aabfd63.png)

### Universe

다음 사진은 [**Universe**](https://marketplace.visualstudio.com/items?itemName=MatiasOlivera.universe) 테마입니다.

![Screenshot from 2020-05-30 07-10-54](https://user-images.githubusercontent.com/16812446/83309603-a8b2fe00-a244-11ea-9048-27967f402607.png)

### 지평선

다음 사진은 [**지평선**](https://marketplace.visualstudio.com/items?itemName=jolaleye.horizon-theme-vscode) 테마입니다.

![Screenshot from 2020-05-30 07-12-20](https://user-images.githubusercontent.com/16812446/83309673-dd26ba00-a244-11ea-960b-e606ab365f32.png)

### SynthWave '84

다음 사진은 [**SynthWave '84**](https://marketplace.visualstudio.com/items?itemName=RobbOwen.synthwave-vscode) 테마입니다.

![Screenshot from 2020-05-30 07-29-25](https://user-images.githubusercontent.com/16812446/83310549-60490f80-a247-11ea-852e-775a8be82897.png)


## 유용한 확장 

다음 링크는 **VSCode** 마켓 플레이스에서 확장을 평가순으로 정렬한 것입니다.

https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories&sortBy=Rating

다음 링크는 **VSCode** 마켓 플레이스에서 확장을 다운로드순으로 정렬한 것입니다.

https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories&sortBy=Installs

최상위에 랭크된 확장들은 설치하여 사용했을시 정말 좋은 확장들이기 때문에 나에게 필요한 확장이 있나 한번 찾아보세요. 여기에서는 몇가지 유용한 확장들만 알아보겠습니다. 

### Git Lens

(git lens)

### Git Graph 

[**Git Graph**](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) 는 여러가지 좋은 기능을 제공합니다. 핵심적으로 다음과 같이 `git` 커밋 기록과 브랜치를 시각적으로 보여줍니다.

<img src="https://raw.githubusercontent.com/mhutchie/vscode-git-graph/master/resources/demo.gif" width="70%" height="auto">

> 이미지 출처 : https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph

<img src="https://user-images.githubusercontent.com/16812446/82319050-d78ed000-9a0b-11ea-8e74-3f94a0e1c81e.png" width="70%" height="auto">

### Code Runner

[**Code Runner**](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) 는 다음과 같이 코드를 손쉽게 실행해볼 수 있게 해줍니다.

<img src="https://raw.githubusercontent.com/formulahendry/vscode-code-runner/master/images/usage.gif" width="70%" height="auto">

> 이미지 출처 : https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner

단순히 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>n</kbd> 만 누르면 되죠. 이 단축키만 누르면 **C/C++ 언어** 도 지알아서 컴파일하고 실행해주고 **Code Runner** 의 환경설정에서 컴파일 옵션을 바꿀 수도 있습니다. 

### PDF 

**VSCode** 에는 **PDF**를 편하게 볼 수 있게 해주는 확장이 있습니다. 두 가지 확장을 추천해드릴 것인데, 편한 것을 쓰면 됩니다.

[vscode-pdf](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf) 는 다음과 같이 **PDF** 파일을 **VSCode** 로 볼 수 있게 해주는 확장입니다.

<div align="center">

<img src="https://raw.githubusercontent.com/tomoki1207/vscode-pdfviewer/images/screenshot.png" width="70%" height="auto">

</div>

> 이미지 출처 : https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf

[LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) 은 ![](https://math.now.sh/?from=\LaTeX) 의 기능을 사용하게 해주는 강력한 확장이고, 그 기능 중에 **PDF** 도 **VSCode** 에서 볼 수 있게 해주는 기능도 있습니다.

### mdmath

[**mdmath**](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) 는 다음과 같이 **Markdown** 파일에 **Tex** 수식을 입력하면 그것을 `.html` 파일로 자동으로 랜더링해주는 확장입니다. 

<img src="https://raw.githubusercontent.com/goessner/mdmath/master/img/mdmath.gif" width="70%" height="auto">

개인적으로 자주 사용하고 있는 확장이기도 합니다. 

### Bracket Pair Colorizer 2

[**Bracket Pair Colorizer 2**](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2) 는 다음과 같이 코드의 **Bracket**, 즉 (), [], {} 과 그 상하관계에 저마다 다른 색깔을 입혀서 가독성을 높혀주는 확장입니다.

![](https://raw.githubusercontent.com/CoenraadS/Bracket-Pair-Colorizer-2/master/images/example.png)

![](https://raw.githubusercontent.com/CoenraadS/Bracket-Pair-Colorizer-2/master/images/forceUniqueOpeningColorDisabled.png)

### Prettier - Code formatter

[**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) 는 다음과 같이 코드를 분석해서 일관적인 코딩 스타일로 지알아서 고쳐주는 매우 유용한 확장입니다. 

<img src="https://user-images.githubusercontent.com/16812446/82320387-2473a600-9a0e-11ea-85aa-80b9c6b02bbd.gif" width="70%" height="auto">

### Diff Tool

[**Diff Tool**](https://marketplace.visualstudio.com/items?itemName=jinsihou.diff-tool) 는 두 파일의 다른 부분을 보여주는 확장입니다. 

### Material Icon Theme

[**Material Icon Theme**](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) 은 다음과 같이 밋밋한 파일들에 아이콘을 입혀서 가독성을 높혀줍니다.

![캡처](https://user-images.githubusercontent.com/16812446/82320708-acf24680-9a0e-11ea-8fb5-a0c5228e3afc.PNG) ![캡처](https://user-images.githubusercontent.com/16812446/82320855-e75be380-9a0e-11ea-9462-2e3e3f879081.PNG)

아이콘 테마는 <kbd>File</kbd> &rarr; <kbd>Preferences</kbd> &rarr; <kbd>File Icon Theme</kbd> 에서 바꿀 수 있습니다.

### Glassit-VSC

[**Glassit-VSC**](https://marketplace.visualstudio.com/items?itemName=s-nlf-fh.glassit) 는 **Windows** 와 **Linux** 에서 적용되는 투명창 효과 확장입니다. 이 확장을 적용하면 다음과 같이 **VSCode** 가 약간 투명해져서 배경화면이 보입니다. 

![Code_KFMh5BA08B](https://user-images.githubusercontent.com/16812446/82327355-3ad32f00-9a19-11ea-9c9c-edc3a20893e7.png)

# VSCode Vim

[**VSCodeVim**](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) 은 **VSCode** 에서 `vim` 키맵을 사용할 수 있도록 해줍니다. 그래서 기존의 CLI 에서의 `vim` 에서는 사용할 수 없었던 **VSCode** 의 모든 풍부한 디버깅 기능, 확장, **VCS** 등을 `vim` 과 함께 사용할 수 있게 됩니다. 어차피 나중에라도 **VSCodeVim** 을 비활성화 시킬 수 있기 때문에 한번 설치해보세요. 

## 단축키

### 주석 처리 

그에 앞서 **VSCode** 에서의 주석 처리 단축키를 알아보겠습니다.

| 기능 | `vim` 단축키 | **VSCode** 단축키 |
|:---:|:---:|:---:|
| 주석 | `\cc`  | `gcc`|

**VSCodeVim** 확장이 적용된 **VSCode** 에서 주석처리는 단순히 `gcc` 를 누르면 됩니다. `5gcc` 를 누르면 `5` 줄이 주석처리되는 식입니다.

### 단축키 설정

**VSCodeVim** 확장의 키맵이 **VSCode** 의 강력한 기능을 덮어버리는 경우도 있었기 때문에 개인적으로 다음의 설정을 통해 **VSCodeVim** 확장의 일부 기능을 비활성화시켰습니다. `...` 에는 또 다른 확장들의 설정이 있는 것입니다. 

```json
{
  ...
  "editor.lineNumbers": "relative",
  "vim.useSystemClipboard": true,
  "vim.useCtrlKeys": true,
  "vim.hlsearch": true,
  "vim.handleKeys": {
      "<C-a>": false,
      "<C-d>": false,
      "<C-f>": false,
      "<C-n>": false,
      "<C-o>": false,
      "<C-w>": false,
      "<C-k>": false,
  },
  ...
}
```

> 이렇게 개인적으로 개발환경 설정을 할 수 있는데 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> 로 명령 팔레트를 열어서 **setting json** 만 검색하면 다음과 같이 **Preferences: Open Settings (JSON)** 이 나옵니다. 이것을 실행하여 설정창이 뜨면 단순히 위의 설정을 복사해서 붙혀넣으면 됩니다. 

<img src="https://user-images.githubusercontent.com/16812446/82322033-cbf1d800-9a10-11ea-9726-10ef40cff6c5.PNG" width="50%" height="auto">

이런 설정을 통해 **VSCodeVim** 확장 단축키를 비활성화시켜서 원래 **VSCode** 단축키로 기능하게 한 단축키는 다음과 같습니다.

| 단축키 | **VSCodeVim** 확장 | **VSCode** 원래 기능 | 
|:---:|:---:|:---:|
| <kbd>Ctrl</kbd>+<kbd>d</kbd> | 화면 내리기 | 멀티 커서 |
| <kbd>Ctrl</kbd>+<kbd>n</kbd> | | 새 파일 만들기 |
| <kbd>Ctrl</kbd>+<kbd>w</kbd> | | 파일 닫기 |
| <kbd>Ctrl</kbd>+<kbd>f</kbd> | | 찾기 |
| <kbd>Ctrl</kbd>+<kbd>o</kbd> | | 파일 열기 |
| <kbd>Ctrl</kbd>+<kbd>a</kbd> | | 전체 선택 |

<kbd>Ctrl</kbd>+<kbd>d</kbd> 는 기본 **VSCode** 에서 멀티 커서 기능인데 **VSCodeVim** 확장을 설치하면 <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 덮어버려서 비활성화시켰고, <kbd>Ctrl</kbd>+<kbd>n</kbd> 은 기본 **VSCode** 에서 새 파일을 만드는 단축키인데 마찬가지로 **VSCodeVim** 확장이 이 단축키를 덮어버렸기 때문에 비활성화시켰습니다. 비슷한 이유로 <kbd>Ctrl</kbd>+<kbd>f</kbd>, <kbd>Ctrl</kbd>+<kbd>o</kbd>, <kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>Ctrl</kbd>+<kbd>w</kbd> 등도 기본 **VSCode** 기능을 하도록 **VSCodeVim** 확장을 비활성화시켰습니다. 

### 그외의 단축키 

그 외의 단축키는 `vim` 과 동일합니다.

여기에서는 이 설정이 적용된 **VSCode** 에서 `vim` 을 사용하여 어떻게 코드를 효율적으로 편집하는지 몇개의 예시를 보여드리겠습니다. **Python** 으로 예시를 들었지만 **모든 언어에 적용될 수 있는 상황들**입니다.

# VSCode Vim 예시

여기에서는 **VSCode** 에서 **VSCodeVim** 확장으로 어떻게 코드 편집을 편하게 편하게 할 수 있는지 보여드리겠습니다. **VSCodeVim** 을 사용하고 싶지 않은 분들이라도 한번 따라해보면서 코드 편집을 얼마나 더 효율적으로 할 수 있는지 꼭 체험해보세요. 

## Python - List to Dictionary

**Python** 코딩을 하다가 `lst = ['all', 'all2', 'all3', 'all4', 'all5']` 라는 리스트를 만들게 되었습니다. 그런데 이 자료구조가 딕셔너리로 사용되면 더 효율적이라는 것을 깨닫고 이 리스트를 딕셔너리로 고치려는 상황입니다. 

1. 먼저 다음과 같이 `,` 에 커서를 두고 `v` 로 드래그 모드로 들어가서 `'` 앞까지 드래그합니다. 

2. 그리고 **VSCode** 의 멀티커서 기능인 <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 꾹 누르고 있으면 매칭되는 모든 코드가 멀티 커서로 포커싱됩니다.

3. 그리고 **삭제하고 편집하기** 기능인 `c` 를 눌러 <kbd>Enter</kbd> 를 칩니다.

4. 그러면 멀티커서가 모든 `, ` 를 삭제하고 개행을 합니다. 그런다음 아직 개행되지 않은 `'all'` 을 개행시키고 <kbd>Ctrl</kbd>+<kbd>v</kbd> 로 블록 드래그 모드로 들어가서 `'all5'` 까지 커서를 내립니다.

5. 그리고 <kbd>Shift</kbd>+<kbd>i</kbd> 를 눌러 입력모드로 들어간다음 키값을 써주고 <kbd>Esc</kbd> 를 눌러 명령모드로 돌아옵니다.

6. 그리고 `r2`, `r3`, `r4`, `r5` 를 눌러 키값을 적절히 바꾸고 `5>>` 를 눌러 자동으로 탭 인덴트를 해줍니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82322465-8550ad80-9a11-11ea-9682-a1f291bb6883.gif" width="70%" height="auto">
</div>

> `0` 으로 문장 앞으로 커서를 옮기는 것이나 `f'` 로 `'` 로 커서를 옮기는 것 등의 설명까지 하면 너무 장황해져서 생략했습니다. 

## Python - copy & paste

다음의 상황은 코딩을 하다보니 `sub_section('math')` 라는 함수를 여러번 사용해야 하는 상황입니다.

1. `yy4p` 로 코드를 `4` 번 복사하여 붙혀넣습니다. 

2. 그리고 `'` 에 커서를 두고 <kbd>Ctrl</kbd>+<kbd>v</kbd> 로 블록드래그를 한 다음 맨 아래 코드까지 내려서 <kbd>Shift</kbd>+<kbd>i</kbd> 로 입력모드에 들어가서 `1` 을 입력합니다. 

3. `r2jr3jr4jr5` 를 입력해 파라미터를 수정합니다. 

4. 그런데 코딩하다보니 `for` 문으로 고치는게 더 적절하다는 것을 깨닫고 `for` 문으로 대체하려 합니다. 그래서 `for` 문을 하나 만들고 `sub_sectoin('math')` 코드를 `yy` 로 복사하여 가져와서 `p` 로 붙혀넣습니다. 

5. 그러고나서 `>>` 를 눌러 인덴트를 조정합니다. 

6. 마지막으로 `7k` 를 눌러 `sub_section('math1')` 코드로 가서 `5dd` 를 눌러 필요없어진 코드를 삭제합니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82323380-ef1d8700-9a12-11ea-97b1-d364f38941c0.gif" width="70%" height="auto">
</div>

## Python - multi cursor

다음의 상황은 코딩을 하면서 `sub_section` 이라는 함수를 만들었는데 갑자기 이 함수의 이름이 마음에 들지 않아서 바꾸고 싶은 상황입니다.

1. `sub_section` 함수 이름이 사용된 아무 곳에서나 커서를 두고 <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 꾹 눌러서 모든 `sub_section` 들이 멀티 커서로 포커싱되게 합니다.

2. **삭제하고 편집하기** 기능인 `c` 를 누르고 고치고 싶은 이름을 입력하면 모든 곳이 자동으로 편집됩니다. 

3. <kbd>Esc</kbd> 를 연타하여 생성된 멀티커서를 소멸해줍니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82324002-dc578200-9a13-11ea-987d-bb5282dc8e22.gif" width="70%" height="auto">
</div>

하지만 단번에 매칭되는 모든 단어에 멀티커서를 두고 싶다면 다음과 같이 하면 됩니다.

1. `subsection` 함수 이름에 커서를 둔다. 

2. <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> 을 누른다.

3. `b` 를 눌러 커서를 단어의 처음으로 옮기고 `cw` 로 삭제하고 편집하기를 눌러 함수 이름을 마음대로 변경한다. 

4. <kbd>Esc</kbd> 를 눌러 빠져나온다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82770651-3a50f300-9e74-11ea-8ee7-ca2981cdc3a9.gif" width="70%" height="auto">
</div>

## Python - rename argument

다음의 상황은 함수와 인자를 정의했는데, 인자의 이름을 바꾸어야 하는 상황입니다. 그런데 인자가 여러군데에서 사용되서 일일이 바꾸기 너무 귀찮을 것 같습니다. 하지만 괜찮습니다.

1. `test` 위에 커서를 올려두고 <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 `3` 번 눌러 `test` 를 멀티커서로 포커싱합니다. 

    - **위에서 보았듯 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> 을 누르면 <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 `3` 번 누를 필요 없이 단번에 멀티 커서가 생성됩니다.**

2. `c` 를 눌러 모든 `test` 를 지우고 입력하고 싶은 문자열을 입력합니다.

3. <kbd>Esc</kbd> 를 연타하여 멀티 커서를 소멸시킵니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82324486-aff03580-9a14-11ea-991e-fac98ec93be5.gif" width="70%" height="auto">
</div>

## C 언어 - 변수 한 줄로 선언하기

다음의 상황은 **C 언어** 를 코딩하고 있던 중 `pthread_t tid` 변수들이 여러 줄로 선언되어 있는 것을 한 줄로 만들고 싶은 상황입니다. 

1. 가장 처음 선언된 `pthread_t tid1` 변수에 커서를 두고 `J` 를 눌러 두번째 문장과 이어붙힙니다.

2. 그리고 `.` 을 연타하여 `pthread_t tid6` 이 선언된 문장까지 이어붙힙니다.

3. 그리고 `0f;` 를 눌러서 `;` 에 커서를 두고 `v` 로 드래그 모드로 들어가서 `e` 를 눌러서 `; pthread_t` 를 드래그합니다. 

4. <kbd>Ctrl</kbd>+<kbd>d</kbd> 를 연타하여 모든 `; pthread_t` 를 멀티 커서로 포커싱합니다. 

5. `c` 를 누르고 `,` 를 입력하고 <kbd>Esc</kbd> 를 연타하여 멀티 커서를 소멸시킵니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82325194-c480fd80-9a15-11ea-8552-9c11c996c0ac.gif" width="70%" height="auto">
</div>

## Markdown - example 1

다음의 상황은 **Markdown** 파일을 작성중 맨 밑에 있는 문장을 맨 위로 올리고 나머지 문장들을 그 문장의 하위 문장이 되게 하고 싶은 상황입니다. 

1. `gg` 로 커서를 맨 위로 올리고 `13dd` 를 눌러 나머지 문장을 잘라냅니다. 

2. `p` 를 눌러 문장을 붙혀넣고 `O` 로 간편하게 개행을 한 다음 <kbd>Esc</kbd> 로 다시 명령모드로 돌아옵니다. 

3. `13>>` 를 눌러 간편하게 탭 인텐트를 조정합니다. 그런데 탭 사이즈가 `4` 로 설정되어 있어서 너무 많이 뛰어진 것 같아서 탭 사이즈를 `2` 로 줄이고 싶습니다. 

4. <kbd>Ctrl</kbd>+<kbd>v</kbd> 를 눌러 블록 드래그 모드로 들어가고 `G` 를 눌러 커서를 맨 밑으로 내리고 `k` 를 한번 눌러 커서를 한 줄 위로 올립니다. 

5. 그리고 `l` 를 누르고 `x` 를 눌러 공백 `2` 개를 삭제합니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82324933-681dde00-9a15-11ea-9899-b8edb9638b6c.gif" width="70%" height="auto">
</div>

## Markdown - example 2

다음은 **Markdown** 파일을 작성하던 중 문장들을 아이템으로 분리하고 싶은 상황입니다. 

1. `0f.` 를 눌러 첫번째 문장이 끝나는 지점에 커서를 둡니다. 

2. `a` 를 누르고 <kbd>Enter</kbd> 를 쳐서 개행을 시킵니다.

3. 이 작업을 다음 문장에도 반복합니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82325719-a798fa00-9a16-11ea-898d-760c5898a288.gif" width="70%" height="auto">
</div>

## Python - multicursor

다음은 파이썬에서 딕셔너리를 만들었는데 값들의 이름이 마음에 안들어서 고치려는 상황입니다.

하지만 지금까지의 설명을 통하여 어떻게 멀티 커서를 사용하여 한번에 편집할 수 있는지 다 이해하셨을 거라고 믿습니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82326020-268e3280-9a17-11ea-92cd-c5261c39047e.gif" width="70%" height="auto">
</div>

## Markdown - example 3

다음은 **Markdown** 파일을 작성하다가 특정 문장을 헤더로 입력하고 싶은 상황입니다.

1. `f(vf)` 로 `(` 부터 `)` 까지 드래그하고 `y` 를 눌러 복사합니다.

2. 그리고 `gg` 로 맨 위로 커서를 옮기고 헤더를 입력한 다음 `p` 로 붙혀넣습니다. 

3. 하지만 헤더의 `(`, `)` 을 없애고 싶습니다. 그래서 `f(xf)x` 로 삭제합니다. 

4. 그런데 오타가 있다는 것을 발견하고 `toin` 을 드래그하고 멀티커서 <kbd>Ctrl</kbd>+<kbd>d</kbd> 로 그것과 똑같은 오타를 포커싱하여 `tion` 으로 고칩니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82326130-563d3a80-9a17-11ea-857f-a6fb7d8db4c8.gif" width="70%" height="auto">
</div>

# VSCode 디버깅 

과거에는 `gdb` 등의 CLI 디버깅 툴로 디버깅을 했었지만 **VSCode** 로 매우 편하게 디버깅할 수 있게 되었습니다. **VSCode** 는 거의 모든 프로그래밍 언어에 대한 풍부한 디버깅 기능을 제공합니다. 여기에서는 간단하게 **Python** 의 디버깅을 가볍게 알아보겠습니다. 하지만 **VSCode** 는 **Flutter**, **Rust**, **C/C++**, **NodeJS**, **Arduino**, **HTML/CSS/JS**, **Latex** 등등 매우 광범위한 언어에 대한 풍부한 디버깅 기능을 제공합니다. 

> 안드로이드 스튜디오에서 제공하는 안드로이드 가상머신 디버깅 기능도 **VSCode** 가 제공합니다.

> 그냥 생각나는 모든 프로그래밍 언어와 모든 플랫폼에 대한 디버깅 기능이 **VSCode** 확장으로 제공되고 있다고 봐도 무방합니다. **VSCode** 가 전세계 1등 에디터라서 각각의 기업들과 커뮤니티들이 앞다투어 자신의 제품을 **VSCode** 확장을 제공하려는 상황이기 때문입니다. 

더 자세한 **VSCode** 의 디버깅 방법과 다른 프로그래밍 언어에 대한 디버깅은 **Google** 을 검색하거나 **VSCode** 의 공식 메뉴얼

https://code.visualstudio.com/docs/editor/debugging

을 참고하세요. 

## Python 디버깅

**Python** 디버깅은 먼저 [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 을 설치해야 합니다. 가볍게 

```python
def for_test(num):
    result = 0
    for i in range(num):
        result += i
    return result

if __name__ == '__main__':
    ct = 3
    for_test(ct)
```

이라는 코드를 디버깅해보겠습니다. 디버깅의 자세한 설명은 [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 의 메뉴얼이나 다양한 블로그 글들을 참고해주세요. 

이때 `result` 라는 변수의 변화에 관심을 두었다고 하면 `result += i` 에 커서를 두고 <kbd>F9</kbd> 를 누르면 **Breakpoint** 가 생깁니다. 디버깅이란 자신이 관심있는 코드에 브레이크 포인트를 걸고 그곳에서 프로그램을 멈추게 하여 그때의 시점에서의 변수와 프로그램의 상태를 관찰하는 것입니다. 

그래서 실제로 다음과 같이 브레이크 포인트를 설정하고 <kbd>F5</kbd> 를 눌러서 디버깅을 시작할 수 있고 왼쪽 패널에서 `result` 변수의 변화를 관찰할 수 있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82329102-c5b52900-9a1b-11ea-96c5-a80faecf5924.gif" width="70%" height="auto">
</div>

브레이크 포인트에서 멈춘 시점에서 <kbd>F10</kbd> 을 누르면 한줄의 코드씩 실행시켜볼 수 있고 <kbd>F5</kbd> 를 누르면 끝까지 진행시켜버릴 수 있습니다. 

# VSCode 와 Docker 로 머신러닝 공부하기

여기에서는 **VSCode** 와 **Docker** 로 [김영섭 교수님](https://github.com/idebtor)의 [파이썬으로 배우는 기계학습](https://github.com/idebtor/KMOOC-ML) 의 주피터 노트북을 실습해보겠습니다. 이로써 **VSCode** 와 **Docker** 를 사용하면 머신러닝 공부가 얼마나 효율적이고 시간낭비 없이 진행될 수 있는지 알아보도록 하겠습니다. 머신러닝이나 주피터노트북에 관심이 없으신 분들은 이 부분을 넘어가도 됩니다.

머신러닝을 공부하려면 3가지 선택지가 있습니다.

1. 직접 일일이 모든 패키지와 환경을 수작업으로 세팅하기.

2. 무거운 아나콘다를 설치하고 첫번째 선택지보다는 덜 복잡한 세팅을 한 후에 웹 브라우저로 주피터 노트북을 사용하기.

3. 가볍운 도커로 한방에 모든 설정을 마무리한 후에 **VSCode** 로 주피터 노트북 학습하기.

## 파이썬으로 배우는 기계학습

여기에서는 **Docker** 로 머신러닝 환경설정을 단번에 설치하고 **VSCode** 로 주피터 노트북을 연동하여 사용해보겠습니다. 먼저 **VSCode** 의 [**Python** 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 과 위에서 소개해드린 **PDF** 확장을 설치해주세요.

그리고 [김영섭 교수님](https://github.com/idebtor/) 의 [**KMOOC**](http://www.kmooc.kr/) 강의 [파이썬으로 배우는 기계학습](http://www.kmooc.kr/courses/course-v1:HGUk+HGU05+2018_T1/about) 의 레포지토리 https://github.com/idebtor/KMOOC-ML 를 로컬 컴퓨터에 **Clone** 하겠습니다.

다음과 같이 쉘로 **Clone** 해도 되고,

```shell
$ g cl https://github.com/idebtor/KMOOC-ML
```

**VSCode** 에서 **Clone** 기능을 이용하여 **Clone** 해도 됩니다. 그러고 나서 레포지토리를 **VSCode** 로 열어주세요.

그리고 다음과 같이 `pdf/JoyML04-2PerceptronAlgorithm.pdf` 와 `ipynb/JoyML04-2Code.ipynb` 를 열어주세요.

![Screen Capture_code_20200612163342](https://user-images.githubusercontent.com/16812446/84477430-88fee980-acca-11ea-8c2d-a30b8ce83305.png)

이러면 재밌게 머신러닝 강의를 들으면서 **VSCode** 로 공부할 준비가 다 되었습니다. 이제 주피터 노트북의 기계학습 코드들을 실행할 수 있도록 **Docker** 컨테이너와 연동하기만 하면 됩니다.

기계학습 환경이 세팅되어 있는 이미지는 도커 허브에서 많이 찾을 수 있습니다. [**Tensorflow 이미지**](https://hub.docker.com/r/tensorflow/tensorflow) 는 번거로운 설치 없이 도커 컨테이너로 **tensorflow** 를 사용할 수 있게 해줍니다. [**PyTorch 이미지**](https://hub.docker.com/r/pytorch/pytorch) 도 번거로운 설치 없이 도커 컨테이너로 **pytorch** 를 사용할 수 있게 해주죠. 하지만 이 이미지들은 각각의 기계학습 라이브러리만을 담고 있어서 **tensorflow** 도 사용하고 싶고 **pytorch** 도 사용하고 싶고 **keras** 도 사용하고 싶은 사람에게 너무 불편합니다. 이것을 위하여 유저들이 다양한 기계학습 라이브러리와 주피터 노트북을 사용할 수 있도록 통합된 환경을 도커 이미지로 만들어 놓았습니다.

저도 **tensorflow**, **pytorch**, **opencv**, **torchtext**, **torchvision**, **jupyter_tensorboard**, **pandas**, **matplotlib** 등등이 다 함께 설치되어 있는 환경이 필요해서 개인적으로 [`torch-notebook` 이라는 도커 이미지](https://hub.docker.com/repository/docker/ccss17/torch-notebook)를 만들어보았습니다. 자세한 설명과 **Dockerfile** 의 소스코드는 [torch-notebook 레포지토리](https://github.com/ccss17/torch-notebook) 에 있습니다. 여기에서는 이 이미지를 받아서 기계학습 도커 컨테이너를 **VSCode** 와 연동해보겠습니다. 

다음 명령어를 실행해보세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker run -d -p 8888:8888 -p 6006:6006 ccss17/torch-notebook
77c5f7e57a3be90967cd7967f672b1cf97c339bce4a498b682247b920e338298
```

그러면 `-d` 옵션 때문에 컨테이너가 백그라운드로 실행되고, 위와 같이 컨테이너 아이디만 출력됩니다. 컨테이너가 완전히 실행될 때까지 기다리고 다음과 같이 `docker logs` 명령어로 컨테이너의 출력을 확인합니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker logs 7
...
     or http://127.0.0.1:8888/?token=bea66985c7d6c36d0712374ae803435c15229531e599b125
```

> 컨테이너 아이디 `77c5f7e5...` 는 각자 다를 수 있습니다. 이 컨테이너 아이디를 축약하여 `docker logs 7` 만 입력한 것입니다.

그러면 맨 밑에 **localhost** 의 `8888` 포트에 토큰이 파라미터로 전달된 형태의 **URL** 이 출력됩니다. 한 번 웹브라우저로 이 주소에 들어가보세요.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84479724-62db4880-acce-11ea-9711-07ff60797fc8.png" width="70%" height="auto">
</div>

그러면 그냥 이 상태에서도 **tensorflow**, **pytorch**, **opencv**, **torchtext**, **torchvision**, **jupyter_tensorboard**, **pandas**, **matplotlib** 등이 설치된 주피터 노트북과 텐저보드를 사용할 수 있습니다. 이제 이것을 **VSCode** 에 연동해보겠습니다.

**VSCode** 에서 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> 를 눌러 **명령 팔레트**를 연 후 `jupyter` 만 입력해보세요. 그럼 다음과 같이 **Python: Specify local or remote Jupyter server for connections** 기능이 뜨는데 이것을 실행하세요.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84479947-b9e11d80-acce-11ea-914b-1bb38040fbf8.png" width="70%" height="auto">
</div>

그리고 다음과 같이 **Existing** 을 누르면 주피터 노트북의 **URL** 을 입력할 수 있는 텍스트 필드가 떠오릅니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84480136-0b89a800-accf-11ea-8f1a-5a7a5070bdbc.png" width="70%" height="auto">
</div>

그러면 각자의 

<div align="center">

`http://127.0.0.1:8888/?token=bea66985c7d6c36d0712374ae803435c15229531e599b125` 

</div>

를 입력하고 <kbd>Enter</kbd> 를 치기만 하면 됩니다. 그러면 다음과 같이 창을 다시 로드하라는 메시지가 뜨는데 <kbd>Reload</kbd> 버튼을 누르기만 하면 됩니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84480416-7a670100-accf-11ea-8e87-29cb10612c54.png" width="70%" height="auto">
</div>

이제 연동이 끝났으니까 ▶ 버튼과 ⏩ 버튼을 눌러서 코드를 실행하면 됩니다. ▶ 버튼은 하나의 셀을 실행하는 버튼이고 ⏩ 버튼은 전체 셀을 실행하는 것입니다.

## 로컬 데이터셋 사용하기

하지만 이렇게 도커 컨테이너를 연동한 것은 단지 셀을 실행할 수 있도록 연결해준 것입니다. 로컬에 기계학습 데이터 셋이 있으면 아직 그것을 사용할 수 없죠. 이 경우 `docker run` 명령어에 `-v` 옵션을 붙혀서 사용하면 됩니다. `-v` 옵션은 로컬 컴퓨터에 있는 경로를 도커 컨테이너로 공유해주는 기능을 합니다.

### Windows 에서

**Windows** 시스템에서 기계학습 데이터 셋이 경로 `d:\repo\ml-data` 에 있다면 `-v d:\repo\ml-data:/workspace` 옵션을 추가하여 다음과 같이 도커 컨테이너를 실행하면 됩니다.

```shell
$ docker run -d -p 8888:8888 -p 6006:6006 -v d:\repo\ml-data:/workspace ccss17/torch-notebook
```

### MacOS 와 Linux 에서

**MacOS** 나 **Linux** 시스템에서 데이터 셋이 경로 `/home/user/repo/KMOOC-ML/ipynb` 에 있다면 `-v /home/user/repo/KMOOC-ML/ipynb:/workspace` 옵션을 추가하여

```shell
$ docker run -d -p 8888:8888 -p 6006:6006 -v /home/user/repo/KMOOC-ML/ipynb/data:/workspace ccss17/torch-notebook
```

를 실행하거나, 해당 경로로 이동하면 `$PWD` 가 현재 경로를 나타내는 것을 이용하여 `/home/user/repo/KMOOC-ML/ipynb` 로 이동하여 다음과 같이 실행하면 됩니다.

```shell
$ cd /home/user/repo/KMOOC-ML/ipynb
$ docker run -d -p 8888:8888 -p 6006:6006 -v $PWD:/workspace ccss17/torch-notebook
```

이렇게 하면 로컬에 있는 데이터 셋도 도커 컨테이너에서 잘 사용할 수 있습니다.

## 컴퓨터를 재부팅 했을 때

컴퓨터를 재부팅하거나 도커 자체를 껐다가 켰을 때 기계학습 환경을 구동중이던 도커 컨테이너가 종료될 수 있습니다. 이 경우 다음의 명령어로 도커 컨테이너를 다시 실행할 수 있습니다. 

```shell
$ docker start 7
```

그리고 도커 컨테이너가 구동중인 주피터 노트북의 **URL** 을 다시 알아내야 하는데, 그것을 알기 위하여 우리는 다음의 명령어를 입력했었습니다.

```shell
$ docker logs 7
...
     or http://127.0.0.1:8888/?token=bea66985c7d6c36d0712374ae803435c15229531e599b125
```

하지만 컴퓨터를 재부팅하는 등의 경우에 더 이상 이 로그가 보이지 않을 수도 있습니다. 이 경우 다음 명령어로 도커 컨테이너가 구동중인 주피터 노트북 리스트를 강제로 출력하면 됩니다.

```shell
$ docker exec 7 jupyter notebook list
Currently running servers:
http://0.0.0.0:8888/?token=0b95a3d951ae884e5d3b99a5bf642cbb801a5304a879c2db :: /workspace
```

도커 컨테이터 아이디의 축약인 `7` 은 각자 다를 수 있습니다.

# VSCode Snippets

**VSCode** 는 강력한 커스텀 스니펫 기능을 제공합니다. 사용자는 개인적인 스니펫을 설정해서 긴 코드를 짧은 단축키와 <kbd>Tab</kbd> 만으로 입력할 수 있습니다.

가령

## **<div align="center"> 🌜 ️여기까지 Day4 내용입니다. 수고하셨습니다. 🌜️ </div>**
