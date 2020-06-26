# VSCode

---

# Table of Contents

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

---

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
