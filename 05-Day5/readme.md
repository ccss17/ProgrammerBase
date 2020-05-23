# Day 5 

GBC 첫번째 과정 **Programmer Base** 의 5일차 내용입니다.

---

# Table of Contents

- [Git 과 Github 못다한 이야기](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#git-%EA%B3%BC-github-%EB%AA%BB%EB%8B%A4%ED%95%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0)

  - [.gitignore](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#gitignore)

    - [.gitignore 의 편리한 기능 ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#gitignore-%EC%9D%98-%ED%8E%B8%EB%A6%AC%ED%95%9C-%EA%B8%B0%EB%8A%A5)

  - [Git Branching](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#git-branching)

    - [브랜치란? ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80)

    - [브랜치 생성](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%83%9D%EC%84%B1)

    - [브랜치 이주 ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EC%9D%B4%EC%A3%BC)

    - [브랜치 병합 시나리오 (1) - Fast-forward](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B3%91%ED%95%A9-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-1---fast-forward)

    - [브랜치 병합 시나리오 (2) - Merge Conflict](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B3%91%ED%95%A9-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-2---merge-conflict)

  - [user.github.io](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#usergithubio)

  - [gist](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#gist)

    - [gist 사용법 ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#gist-%EC%82%AC%EC%9A%A9%EB%B2%95)

    - [gist 명령어 ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#gist-%EB%AA%85%EB%A0%B9%EC%96%B4)

  - [Pull Request](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#pull-request)

    - [1. fork 하고 clone 하기](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#1-fork-%ED%95%98%EA%B3%A0-clone-%ED%95%98%EA%B8%B0)

    - [2. 편집하고 push 하기](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#2-%ED%8E%B8%EC%A7%91%ED%95%98%EA%B3%A0-push-%ED%95%98%EA%B8%B0)

    - [3. **pull request** 하기](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#3-pull-request-%ED%95%98%EA%B8%B0)

- [좋은 정보 얻기](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EC%A2%8B%EC%9D%80-%EC%A0%95%EB%B3%B4-%EC%96%BB%EA%B8%B0)

  - [Awesome Repository](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#awesome-repository)

  - [Hacker News](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#hacker-news)

  - [Reddit ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#reddit)

  - [Github trending](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#github-trending)

  - [Stackoverflow Survey](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#stackoverflow-survey)

  - [검색](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EA%B2%80%EC%83%89)

    - [영어 검색](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EC%98%81%EC%96%B4-%EA%B2%80%EC%83%89)

    - [아니 그럼 어떻게 검색해야 하나?](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EC%95%84%EB%8B%88-%EA%B7%B8%EB%9F%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B2%80%EC%83%89%ED%95%B4%EC%95%BC-%ED%95%98%EB%82%98)

    - [원작자 찾기 ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EC%9B%90%EC%9E%91%EC%9E%90-%EC%B0%BE%EA%B8%B0)

- [리눅스 교재](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B5%90%EC%9E%AC)

- [Funny CLI ](https://github.com/ccss17/ProgrammerBase/tree/master/05-Day5#funny-cli)

---

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

> 참고 : https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

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

> 지금까지 **Git Branching** 을 매우 간단하게 알아보았는데, 나중에 https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell 을 통하여 **Git Branching** 의 더욱 강력한 기능을 추가 학습하시길 강력하게 추천합니다.

> **VSCode** 에서는 왼쪽 하단부의 **Branch** 를 클릭하거나 명령 팔레트에서 **branch** 를 검색하는 것으로 매우 쉽게 **Branch** 를 생성하거나 이주할 수 있습니다.

## user.github.io

user.github.io 은 **Github** 이 제공하는 개인 블로그 플랫폼입니다. 저의 **Github** 아이디는 `ccss17` 인데 이 아이디로 user 를 치환하여 ccss17.github.io 에 접속해보면 제가 관리하고 있는 블로그가 보입니다. 이 블로그는 https//github.com/ccss17/ccss17.github.io 의 `index.html` 파일과 각각의 `*.html` 파일들이 랜더링 된 것입니다. 

이처럼 **Github** 에 아이디만 있다면 자신의 아이디로 user.github.io 라는 이름을 가진 레포지토리를 생성하고 그곳에 `index.html` 과 메모하거나 게시하고 싶은 정보를 `.html` 파일로 만들어 레포지토리를 **commit** 하고 **Github** 에 **push** 하면 자동으로 user.github.io 에 게시가 시작됩니다. 

> [**jekyll**](https://jekyllrb.com/) 을 사용하면 `.md` 파일만으로도 웹페이지를 생성할 수 있어 매우 편합니다. 

개인 블로그에 자신이 공부한 내용이나 알아낸 사실을 게시하면 그것이 모두 다 포트폴리오가 되고 스펙이 되서 자신의 가치를 높이는 일이 됩니다. 그러나 이 블로그 플랫폼을 사용하고 싶지 않은 분들도 있음을 감안해서 더 이상의 상세한 설명과 실습은 하지 않고 유명한 `*.github.io` 사이트들과 **Github** 의 공식 메뉴얼과 저의 ccss17.github.io 를 가볍게 보여드리는 것으로 마무리 하겠습니다. 

- **Github** 페이지 공식 메뉴얼 : https://pages.github.com/

- [sindresorhus](https://github.com/sindresorhus/sindresorhus.github.com) 의 [블로그](https://sindresorhus.com/) : https://github.com/sindresorhus/sindresorhus.github.com

- [도커 가이드](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html) : https://github.com/subicura/subicura.github.io 

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

[gist](https://gist.github.com/) 사용법은 매우 간단합니다. https://gist.github.com/ 에 들어가면 다짜고짜 제목과 파일이름 내용을 입력하는 텍스트 필드가 나오는데 이 3가지 텍스트 필드를 입력하고 <kbd>Create secret gist</kbd> 또는 <kbd>Create public gist</kbd> 버튼을 누르면 그게 다입니다. 그러면 gist 가 생성되는데 URL 을 다음과 같이 어디에서든 **clone** 할 수 있습니다. 

```shell
$ g cl https://gist.github.com/ccss17/ff6944df7e8f3c9ab518629915857d85
```

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

레포지토리가 자신의 소유의 레포지토리로 복제됩니다. 여기에서는 **hgu-student** 라는 아이디를 갖고 있는 학생이 레포지토리를 **fork** 해왔습니다. **fork** 된 레포지토리의 **URL** 도 원래의 **URL** 인 https://github.com/ccss17/pull-request-me 에서 https://github.com/hgu-student/pull-request-me 로 바뀌었습니다. 이제 이것을 로컬 컴퓨터로 **clone** 합니다. 지금까지 배웠던 **Git** 의 명령어를 다음과 같이 사용하면 됩니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g cl https://github.com/hgu-student/pull-request-me
```

도커 컨테이너에서 해도 되고 로컬 컴퓨터에서 **VSCode** 로 해도 됩니다. 그리고 사실 **당장 실습하고 싶지 않은 분들은 안하셔도 됩니다**. 

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

그런 다음 다음과 같이 지금까지 배웠던 **Git** 명령으로 스테이징 후 커밋합니다. 그리고 https://github.com/hgu-student/pull-request-me 이 **push** 까지 합니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g a 
$ g cm "메인 함수를 고침!"
$ g psom
```

### 3. **pull request** 하기

그런데 여러분의 레포지토리가 업데이트 되었을 뿐 원작자의 레포지토리가 업데이트 된 것은 아닙니다. 그래서 원작자에게 어서 빨리 내 레포지토리를 **pull** 해주세요 라고 말하기 위하여 **Pull Request** 를 합니다. 다음 사진과 같이 자신의 레포지토리의 왼쪽 상당부를 보면 <kbd>Pull requests</kbd> 버튼이 있습니다. 이 버튼을 눌러 **Pull Request** 페이지로 들어갑니다. 

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

---

# 좋은 정보 얻기

그러면 이제부터 좋은 정보나 최신기술을 어디에서 찾을까 에 대한 대답을 알아보겠습니다. 하지만 부족한 제가 알아볼 수 있는 한 알아보고 저만의 결론을 내린 것이기 때문에 이것들이 최선의 해답이 되지 않을 거라는 것은 명백합니다. 그러니 각자 제가 드리는 지식에 안주하지 말고 최신동향과 좋은정보에 예민해지려고 노력해야 합니다. 

## Awesome Repository

프로그래머만큼 최신기술과 좋은정보에 민감해야만 하는 직종은 없을겁니다. 그래서 프로그래머들은 각자의 분야에서 최신기술이나 좋은정보를 모아둔 **Awesome Repository** 를 만들기로 했고 다음과 같은 좋은 레포지토리들이 탄생했습니다. 

<div align="center">

|Awesome |Repository|
|:---:|:---|
|인공지능 | https://github.com/owainlewis/awesome-artificial-intelligence|
|기계학습| https://github.com/josephmisiti/awesome-machine-learning|
|해킹 | https://github.com/carpedm20/awesome-hacking|
|**Flutter** | https://github.com/Solido/awesome-flutter|
|**Python** | https://github.com/vinta/awesome-python|
|알고리즘 | https://github.com/tayllan/awesome-algorithms|
|**VSCode** | https://github.com/viatsko/awesome-vscode|
|**NodeJS**| https://github.com/sindresorhus/awesome-nodejs|
|**MacOS**| https://github.com/iCHAIT/awesome-macOS|
|**Web Extensions**| https://github.com/fregante/Awesome-WebExtensions|
|**C/C++**| https://github.com/fffaraz/awesome-cpp |
|**React**| https://github.com/enaqx/awesome-react|
|**웹 성능 최적화**| https://github.com/davidsonfellipe/awesome-wpo|
|**Docker**| https://github.com/veggiemonk/awesome-docker|
|**Nginx**| https://github.com/fcambus/nginx-resources|
|**Flask**| https://github.com/humiaozuzu/awesome-flask|
|**강의**| https://github.com/prakhar1989/awesome-courses|
|**수학**| https://github.com/rossant/awesome-math|
|**Vim**| https://github.com/mhinz/vim-galore|
|**마인크래프트**| https://github.com/bs-community/awesome-minecraft|

</div>

보시면 아시겠지만 레포지토리의 이름들이 각각의 분야의 이름을 기반으로 규칙적으로 `awesome-<분야>` 라고 되어있음을 알 수 있습니다. 그렇다면 이러한 **Awesome Repository** 들을 내가 관심있는 분야에서도 찾고 싶은데, 도대체 어떻게 해야 할까요? 

정답은 **Awesome Repository** 들을 모아둔 **Awesome Repository** 에 방문하는 것입니다.

<div align="center">

|Awesome |Repository|
|:---:|:---|
|**Awesome** |  https://github.com/sindresorhus/awesome|

</div>

이 레포지토리는 **Github** 레포지토리의 스타가 **470,793** 개([2020/05/22 기준](https://gitstar-ranking.com/)) 로 가장 많은 [sindresorhus](https://github.com/sindresorhus) 가 **Awesome Repository** 들을 모아둔 레포지토리로써 이 단일 레포지토리에 스타가 약 **134,000** 개가 달려있습니다. 

여기에서 각자 관심있는 주제나 분야, 툴들의 **Awesome** 한 정보들을 찾아보세요. 

## Hacker News

> 참고 : https://en.wikipedia.org/wiki/Hacker_News

> 참고 : https://www.quora.com/What-is-Hacker-News

[Hacker News](https://news.ycombinator.com/) 는 [Paul Graham](https://en.wikipedia.org/wiki/Paul_Graham_(programmer)) 이 만든 인터넷 커뮤니티로써 컴퓨터 해커에게 흥미로운 모든 것을 공유하기 위한 커뮤니티입니다. 

단 여기서 "해커" 란 정보보안가를 뜻하는 것이 아니라 좀 더 포괄적인 의미로의 "해커" 입니다. 해킹이란 원래 무언가를 능수능란하게 다루거나 호기심과 지적욕구에 의해 컴퓨터와 네트워크를 탐험하는 행위라는 의미 였는데 여기에서는 이와같은 포괄적인 의미로 보아야 할 것 같습니다. 

왜냐하면 해커 뉴스에는 컴퓨터 보안에 관련된 정보 뿐만 아니라 인공지능, 웹 개발, 게임 개발, 전자 회로, 수학 관련 글(*선형대수학 관련 글이 꽤 올라옵니다*), IT대기업(Google, Amazon, Facebook 등)의 최신동향 등등 정말 다양한 좋은 정보들이 많이 올라오기 때문입니다. 심지어 취업을 잘 하려면 어떻게 해야 하는지에 대한 글도 올라옵니다. 

이렇게 좋은 정보들에 예민하게 반응한다면 자신이 있는 공동체에 좋은 정보를 공유함으로써 그 공동체가 한 단계 더 성장할 수 있습니다. 그 공동체가 동아리가 될 수도 있고 기업이 될 수도 있고 친구들이 될 수도 있습니다. 그렇게 되면 좋은 정보의 원천이 된 여러분이 사람들로부터 더욱 인정받게 되고요. 

- 실제로 이 **ProgrammerBase** 를 만들게 된 계기와 아이디어를 **MIT** 의 [**Missing Semester**](https://missing.csail.mit.edu/) 에서 착안했는데, 이것 또한 다음과 같이 **Hacker News** 에서 발견한 것입니다.

  <img src="https://user-images.githubusercontent.com/16812446/82681473-c6062c00-9c88-11ea-993e-4cc9a626bffe.png" width="70%" height="auto">

  > 여러분이 이 **ProgrammerBase** 를 통하여 조금이라도 실력을 높힐 수 있었다면 제가 말했던 "공동체(고스트 동아리) 자체가 한 단계 성장" 하는 것의 실례가 되는 셈입니다. 

- **Hacker News** 에는 다음과 같이 [**Discord** 가 **Go** 언어에서 **Rust** 언어로 갈아타게 된 과정에 대한 글](https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f)도 올라왔었습니다. 

  <img src="https://user-images.githubusercontent.com/16812446/82681726-24cba580-9c89-11ea-87e5-dc7561ad4564.png" width="70%" height="auto">

  실제로 글을 읽어보면 대충 **Go** 의 가비지 콜렉터보다 **Rust** 의 가비지 콜렉터가 **Discord** 에서 더 좋아보이더라 라는 결론으로 **Rust** 를 쓰게 되었다고 했습니다. 물론 **Go** 도 최고의 언어이고 분명 **Rust** 보다 더 효율적으로 사용되는 상황과 분야가 있을 겁니다. 

  > 여러분이 이러한 새로운 프로그래밍 언어에 대한 좋은 정보를 갖춘 다음 여러분이 하고 있는 프로젝트에 이러한 새로운 제안을 하게 되서 그 혁신으로 프로젝트가 조금이라도 더 개선된다면 여러분의 입지는 더욱 커지는 것이고 능력을 더 인정받게 될 겁니다. 그리고 여러분 한 사람으로 인해 프로젝트와 그 공동체가 더욱 발전하게 될 겁니다. 

- **Hacker News** 에는 다음과 같이 [MS 에서 메모리를 혁신적으로 최적화하여 신경망 학습 시 메모리를 효율적으로 절약할 수 있는 기술에 대한 글](https://www.microsoft.com/en-us/research/blog/zero-deepspeed-new-system-optimizations-enable-training-models-with-over-100-billion-parameters/?OCID=msr_blog_zerodeep_tw)도 올라왔습니다. 

  ![Screen Capture_Navigator_20200523002033](https://user-images.githubusercontent.com/16812446/82683013-301fd080-9c8b-11ea-843f-8c91d5e6a5bc.png)

  대충 [microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) 라는 것을 쓰면 신경망 학습이 **5배**배 빨라지고 메모리 효율이 최대 **64배**배 높아진다는 내용입니다. 심지어 **PyTorch** 와 호환된다고까지 하니까 만약 여러분이 **PyTorch** 로 진행되는 프로젝트에 참여중이라면 충분히 이런 정보를 공유할 수 있고, 여러분이 속한 공동체를 발전시킬 수 있습니다. 

마지막으로 한 가지 사례만 더 들고 **Hacker News** 는 마무리 하겠습니다. 

- 어느날 **Hacker News** 에는 다음과 같이 [Can AI Become Consious?](https://cacm.acm.org/news/244846-can-ai-become-conscious/fulltext) 라는 글이 올라왔습니다. 

  <img src="https://user-images.githubusercontent.com/16812446/82683442-04511a80-9c8c-11ea-9fe2-60ede1f1975b.png" width="70%" height="auto">

  이 글에서는 정보통합이론(Integrated Information Theory) 를 소개하면서 핵심적으로 다음과 같은 사실을 설득하려 했습니다. 

  1. 인과적 힘을 갖는다면 어떤 물리 체계일지라도 의식을 갖는다. 뇌의 뉴런이 다른 뉴런을 자극하여 촉발시키는 것 또한 인과적 힘의 예시라고 볼 수 있고, 컴퓨터 회로에서 트랜지스터가 다른 트랜지스터에게 자극을 주는 것도 인과적 힘의 예시라고 볼 수 있다. 

  2. 정보통합이론은 임의의 물리 체계가 얼마나 의식적인가 측정하는 방법 또한 개발하였고, 이것을 의학에 응용하여 뇌손상을 입은 환자나 식물인간이 얼마나 의식을 갖고 있는지 측정하기도 하였다. 

  3. 정보통합이론은 의식이 인간에게만 존재하는 유일한 특성이 아니라고 말한다.

  4. 현재의 기계(컴퓨터)가 의식을 가질 수는 없으나 미래에 탄생할 기계가 의식을 갖게 되고 인간과 같은 지능을 갖게 될 것이라는 것은 의심할 수 없는 사실이다. 

  5. 지능이란 행동에 관한 것이다. 가령 당신은 당신에게 주어진 환경에서 살아남기 위하여 어떻게 행동할 것인가? 그러나 의식이란 행동에 관한 것이 아니다. 의식이란 존재에 관한 것이다. 

  6. 폰 노이만 구조로 구현된 표준적인 회로에서의 트랜지스터는 통상적으로 두 개 이상의 트랜지스터로부터 입력을 받고 두 개 이상의 트랜지스터에게 출력을 보낸다. 이것이 인과적 힘인 것은 맞지만 극단적으로 복잡한 인과적 힘을 갖고 있는 뇌의 약 860억개의 뉴런이 갖고 있는 인과적 힘과 명백히 다르다. 그러므로 폰 노이만 구조 위에서 실행되는 어떠한 인공지능이라 할지라도 그것은 인간의 뇌처럼 의식적이지 못하다. 

  만약 여러분이 인공지능 관련 프로젝트에 속해있고 이런 글을 읽었다면 인공지능이 의식을 가질 수 있는지에 대한 연구가 진행되어온 이 정보통합이론에 더 관심이 생겨서 "Integrated Information Theory" 나 "정보통합이론" 이라는 키워드로 검색을 하다가 

  [<img src="https://bookthumb-phinf.pstatic.net/cover/144/803/14480315.jpg?udate=20190327" width="150px" height="auto">](https://book.naver.com/bookdb/book_detail.nhn?bid=14480315) [<img src="https://bookthumb-phinf.pstatic.net/cover/121/665/12166506.jpg?udate=20170718" width="150px" height="auto">](https://book.naver.com/bookdb/book_detail.nhn?bid=12166506)

  이런 책들을 찾아보았을 수도 있습니다. 

## Reddit 

[레딧](https://www.reddit.com/)은 매우 광범위한 주제와 커뮤니티가 존재하는 거대 커뮤니티이지만 프로그래머들 또한 레딧에서 상당히 큰 생태계를 만들고 그곳에서도 매우 좋은 정보가 공유되고 있습니다. 여기에서는 가볍게 몇가지 서브레딧만 알아보고 나중에 여러분이 개인적으로 마음에 드는 서브레딧을 찾아보세요. 

- [**programming** 서브 레딧](https://www.reddit.com/r/programming/)

- [**sysadmin** 서브 레딧](https://www.reddit.com/r/sysadmin/)

- [**ArtificialInteligence** 서브 레딧](https://www.reddit.com/r/ArtificialInteligence/)

- [**Hacking_Tutorials** 서브 레딧](https://www.reddit.com/r/Hacking_Tutorials/)

- [**learnprogramming** 서브 레딧](https://www.reddit.com/r/learnprogramming/)

- [**MachineLearning** 서브 레딧](https://www.reddit.com/r/MachineLearning/)

## Github trending

[**Github trending**](https://github.com/trending) 은 현재 **Github** 에서 가장 핫하고 트렌드한 레포지토리가 올라오는 곳입니다. 이곳에서도 좋은 정보를 많이 얻을 수 있습니다. 왜냐하면 전세계의 개발자들이 최근동안 가장 관심을 기울이고 있는 레포지토리들이 올라오기 때문입니다. 

![firefox_FViJ96Yk9y](https://user-images.githubusercontent.com/16812446/82721758-4d8c8300-9cfb-11ea-96de-2bec87c27c46.png)

## Stackoverflow Survey

Stackoverflow Survey 도 좋은 정보를 얻을 수 있는 소스가 됩니다. 하지만 이미 다뤘기 때문에 넘기겠습니다.

## 검색

### 영어 검색

영어로 검색해야 좋은 정보를 얻을 수 있습니다. 

> 이것은 너무 당연하지만 한동대학교에 처음 입학한 새내기도 GBC 를 수강하므로 다시 한 번 영어 검색을 강조하겠습니다.

이것은 너무 당연한데 한글로 검색하면 대한민국 인구가 5천만명에 불과한 반면 영어권 화자 인구는 약 [11억명](https://ko.wikipedia.org/wiki/%EC%98%81%EC%96%B4_%EC%82%AC%EC%9A%A9%EC%9E%90_%EC%88%98%EC%97%90_%EB%94%B0%EB%A5%B8_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D) 입니다. **Google** 은 [페이지 순위 매기기 알고리즘](https://en.wikipedia.org/wiki/PageRank) 으로 여러분이 검색하는 키워드로 필터링 된 웹 페이지 중에서 사람들이 가장 많이 방문할 것같은 페이지 순서대로 검색 결과를 나열합니다. 그러므로 영어로 검색하면 11억 명의 거대한 집단지성이 도출한 가장 가치있는 결론을 **Google** 이 맨 위로 올려서 보여줍니다. 

> 이제 질문을 바꿔보겠습니다. 만약 여러분이 한 회사의 사장이라면 5천만명 중에서 1등한 사람을 뽑겠습니까, 11억명 중에서 1등한 사람을 뽑겠습니까. 이 질문에 대한 대답은 객관적으로 당연히 11억명 중에서 1등한 사람을 뽑아야 합니다. 

> 또 다시 질문을 바꿔보겠습니다. 그러면 11억명 중에서 1등인 그 사람이 영어를 쓰는데 나는 영어를 못해서 말이 안통해서 같이 일을 못한다면 어쩔 수 없이 5천만명 중에서 1등한 사람과 일해야겠습니까, 아니면 영어를 어떻게든 극복한 다음에 11억명 중에서 1등한 사람과 일해야겠습니까. 사실 이건 개인의 가치관의 차이가 있기 때문에 객관적인 확답을 내리긴 어렵지만 저는 개인적으로 영어를 극복한 다음 11억명 중에서 1등한 사람과 일해야 한다고 생각합니다. 그러니까 제 개인적인 의견은 어떻게든 영어의 장벽을 극복하고 한글 검색 보다 영어로 검색하는 것이 좋은 것 같다는 의견입니다.

### 아니 그럼 어떻게 검색해야 하나?

이것에 관한 건 순전히 경험적인 지식이므로 스스로 터득해야 합니다만, 제가 경험한 바로는 다음과 같이 검색하는 것이 가장 효과가 좋았습니다. 

- **[플랫폼]** **[세부 플랫폼]** **[세부 사항]** 

  - 가령 **Python** 코딩 중 `numpy` 모듈의 `where` 함수가 궁금하다면 **python numpy where** 이라고 검색하는 것입니다.

- **[세부 플랫폼]** **[세부 사항]** in **[플랫폼]** 

  - 가령 **Python** 코딩 중 `numpy` 모듈의 `where` 함수가 궁금하다면 **numpy where in python** 이라고 검색하는 것입니다.

더 세부적으로는 다음과 같은 링크에 구글 고급 검색 명령어

https://www.spyfu.com/blog/google-search-operators/

https://support.google.com/websearch/answer/2466433?hl=en

등을 찾을 수 있는데 이것으로 검색하는 방법도 있습니다.

> 구글 검색 명령어가 얼마나 강력한지 이것을 사용한 [구글 해킹](https://ko.wikipedia.org/wiki/%EA%B5%AC%EA%B8%80_%ED%95%B4%ED%82%B9) 이라는 용어도 생겼습니다. 

### 원작자 찾기 

검색할 때는 항상 원작자를 찾아야 합니다. 여러분이 기독교인이라면 세상과 인간의 원작자인 하나님과 성경을 찾을 것입니다. 갤럭시를 쓰고 있는데 그것에 문제가 생겼다면 그것의 원작자인 삼성을 찾아가야 합니다. 하지만 코딩할 때 문제가 생겨서 검색할 때를 보면 꽤 많은 학생들이 원작자의 공식 문서를 먼저 찾기보다 2차 창작물, 즉 블로그나 문답사이트부터 찾는 것을 볼 수 있습니다. 

하지만 언제나 원작자의 공식 문서를 먼저 찾아보는 것이 순서입니다. 그것이 가장 정확하고 명료한 설명이기 때문입니다. 그런데 원작자의 글을 도무지 찾을 수 없거나 원작자의 글이 너무 어려워서 이해가 안되면 그 다음에나 2차 창작물, 즉 블로그나 문답사이트를 알아보아야 합니다. 

- 가령 **Python** 에서 `numpy` 를 사용하던 중 `where` 이라는 함수에 대한 이해가 필요해졌습니다. 그러면 **Google** 에 **python numpy where** 이라고 검색합니다. 그러면 **Google** 이 다음과 같이 [원작자의 글](https://numpy.org/doc/stable/reference/generated/numpy.where.html) 을 1등으로 추천해주는 것을 볼 수 있습니다. 

  ![firefox_hLynsSG3O4](https://user-images.githubusercontent.com/16812446/82721812-f0dd9800-9cfb-11ea-9600-fbaa2572c8ec.png)

> 근대 철학의 아버지 데카르트는 너무나도 명료하여 조금의 망설임도 없이 진리로 받아들일 수 있는 사실을 모든 지식의 토대, 즉 공리로 삼고자했습니다. 그것은 (1) "나는 생각한다. 고로 나는 존재한다." (2) "모든 현상은 원인을 갖는다." (3) "결과가 원인보다 거대할 수 없다." (4) "정신에는 완전성, 공간, 시간, 그리고 운동의 개념이 내재되어 있다." 입니다. 데카르트가 옳다면 두번째 공리 "모든 현상은 원인을 갖는다." 에 따라 어떠한 대상물이라도 그 원작자가 항상 존재합니다. 왜냐하면 그 대상물 또한 그것을 있게한 원인을 갖기 때문입니다. 그러므로 원작자가 존재하지 않을 수 없으니 검색할 때 언제나 원작자를 찾으려고 하는 것이 좋습니다. 

---

# 리눅스 교재

교재에서 다음 분량을 읽고 우분투 도커 컨테이너에서 실습해주세요. 사실 너무 열심히 읽지 않아도 됩니다. 즉, 막 외우려고 애쓰지 않아도 된다는 뜻입니다. 이런게 있구나 하면서 훅훅 실습하면서 술술 넘기세요. 그리고 하다가 실습하기 힘든 부분이 있다면 그냥 너무 걱정하지 말고 넘겨도 됩니다. 

**(옵션)** 라고 되어있는 파트는 시간절약을 위해 아예 안봐도 됩니다.

## Chapter 06

- **276p ~ 290p, 292p ~ 295p 읽고 실습하기**

  - 프로세스의 개념, 프로세스 관리 명령

- **296p ~ 301p 읽고 실습하기**

  - 포그라운드/백그라운드 프로세스와 작업 제어, 

- **304p ~ 315p 읽고 실습하기**

  - **(옵션)** 작업 예약

## Chapter 10

- **504p ~ 513p 읽고 실습하기**

  - 사용자 계정 관련 파일

- **514p ~ 526p 읽고 실습하기**

  - **(옵션)** 사용자 계정 관리 명령

- **528p ~ 533p 읽고 실습하기**

  - **(옵션)** 그룹 관리 명령

- **537p ~ 548p 읽고 실습하기**

  - 사용자 정보 관리 명령 

- **549p ~ p 읽고 실습하기**

  - **(옵션)** 디스크 사용량(쿼터) 설정

---

# Funny CLI 

이제 여기까지 달려온 여러분들을 위해 머리를 좀 식히자는 의미에서 **퍼니 CLI**, 즉 실용성이 없이 순전히 재미를 목적으로 만들어진 **CLI** 들을 알아보겠습니다. 

이 부분은 **실용성이 전혀 없기 때문에** 직접 실습하셔도 되고 안하셔도 됩니다. 또 **시간이 아깝다면 Funny CLI 부분을 넘겨도 됩니다**. 즉, 아예 안봐도 됩니다.

> 이 **Funny CLI** 들 또한 이미 도커 컨테이너에 설치되어 있기 때문에 설치법은 모두 생략합니다. 각각의 공식 레포지토리에 들어가면 설치법을 알 수 있습니다. 

그러면 이제 도커 컨테이너에 접속해서 진행해주세요. 

## asciiquarium

**[`asciiquarium`](https://github.com/cmatsuoka/asciiquarium)** 은 아스키 코드로 만들어진 아쿠아리움을 뜻합니다. 

이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ asciiquarium
```

다음과 같은 아스키로 이루어진 아쿠아리움이 나옵니다. 

![render1588863585888](https://user-images.githubusercontent.com/16812446/81310305-e21da100-90be-11ea-9b15-ed6de1c600ca.gif)

> `q` 로 종료할 수 있어요. 

## nyancat

**[`nyancat`](https://github.com/klange/nyancat)** 은 **CLI** 로 고양이가 뛰어다니는 것을 보여주는 미친 프로그램입니다. 

이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ nyancat
```

다음과 같은 미친 고양이가 뛰어놉니다. 

![render1588863923651](https://user-images.githubusercontent.com/16812446/81310941-b5b65480-90bf-11ea-9540-641c5c71b96b.gif)

> <kbd>Ctrl</kbd>+<kbd>c</kbd> 로 종료할 수 있어요. 

## sl

**[`sl`](https://github.com/mtoyoda/sl)** 은 **CLI** 로 기차를 보여주는 프로그램입니다.

이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ /usr/games/sl
```

다음과 같이 기차가 지나갑니다. 

![render1588864227794](https://user-images.githubusercontent.com/16812446/81311546-805e3680-90c0-11ea-8bcb-fb64b154053f.gif)

## ChristBASHTree

**[`ChristBASHTree`](https://github.com/sergiolepore/ChristBASHTree)** 은 **CLI** 로 크리스마스 트리를 보여주는 프로그램입니다.

이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ ChristBASHTree
```

다음과 같이 크리스마스 트리가 나타납니다. 

![render1588865712684](https://user-images.githubusercontent.com/16812446/81314439-134ca000-90c4-11ea-9ef0-2ab491c70090.gif)

## unimatrix

**[`unimatrix`](https://github.com/will8211/unimatrix)** 은 **CLI** 로 매트릭스를 보여주는 프로그램입니다. 

이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ unimatrix -c red
```

다음과 같이 붉은 매트릭스 나타납니다. 

![7tIs8Ca4Xm](https://user-images.githubusercontent.com/16812446/81960485-fbd56000-964b-11ea-9c7b-40ff88e2f42f.gif)

## lolcat 

[`lolcat`](https://github.com/jaseg/lolcat) 은 우리가 이미 `vim` 을 연습할 때 설치하고 테스트 해봤던 프로그램입니다. 따라서 설치법과 실행법은 생략하고 다음의 실행결과만 가볍게 살펴보고 넘어가겠습니다.

![render1589351764615](https://user-images.githubusercontent.com/16812446/81779347-7d839b80-952f-11ea-891e-1f29490c678d.gif)

## pipe.sh

**[`pipe.sh`](https://github.com/pipeseroni/pipes.sh)** 는 **CLI** 로 파이프를 보여주는 프로그램입니다.

다음 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ pipes.sh
```

이렇게 파이프가 나타납니다. 

![render1588866558609](https://user-images.githubusercontent.com/16812446/81316124-2496ac00-90c6-11ea-8c0e-b66bc92029fe.gif)

## YuleLog

**[`YuleLog`](https://github.com/Duroktar/YuleLog)** 는 **CLI** 로 따뜻한 장작을 보여주는 프로그램입니다.

다음 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ YuleLog
```

따뜻한 장작이 나타납니다. 

![render1588865888181](https://user-images.githubusercontent.com/16812446/81315262-0ed4b700-90c5-11ea-92e6-c6e91cfabbf0.gif)

## nonogram

마지막으로 **[`nonogram`](https://github.com/ccss17/nonogram)** 는 네모로직 수학퍼즐을 지알아서 풀어서 **CLI** 로 결과를 출력해주는 제가 만든 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g cl https://github.com/ccss17/nonogram
```
그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd nonogram
$ python3 main.py test/55.txt
$ python3 main.py test/1010.txt
$ python3 main.py test/1515.txt
$ python3 main.py test/2020.txt
$ python3 main.py test/2525.txt
$ python3 main.py test/3030.txt
```

다음과 같이 프로그램이 각각의 샘플 네모로직 수학퍼즐이 지알아서 풀고 출력합니다.

> 소스코드와 더 자세한 설명을 원한다면 https://github.com/ccss17/nonogram 를 참고해주세요. 

![1cbY6BnXq5](https://user-images.githubusercontent.com/16812446/81961266-1825cc80-964d-11ea-82c1-96c9d26eed7f.gif)

가령 `15x15` 네모로직 수학퍼즐의 샘플의 구조를 특정하고 있는 `test/1515.txt` 파일은 

![](https://user-images.githubusercontent.com/16812446/72774545-5a667080-3c4e-11ea-951d-7668876134ac.png)

> 출처 : http://nemonemologic.com/play_logic.php?quid=10170&page=0&size=15

의 데이터를 담고 있는데 이것을 자동으로 풀기 위하여 `python3 main.py test/1515.txt` 를 입력하면 되는 것입니다. 

---

# 조금은 철학적인 이야기 

> 참고 : [『수학사상사 1』, 『수학사상사 2』, 『수학사상사 3』, 모리스 클라인](https://book.naver.com/bookdb/book_detail.nhn?bid=10236389)

> 참고 : [『수학의 확실성』, 모리스 클라인](https://book.naver.com/bookdb/book_detail.nhn?bid=2900590)

> 참고 : [『괴델의 증명』, 어니스트 네이글, 제임스 뉴먼, 더글러스 호프스태더](https://book.naver.com/bookdb/book_detail.nhn?bid=6395428)

> 참고 : [『컴퓨터과학이 여는 세계』, 이광근](https://book.naver.com/bookdb/book_detail.nhn?bid=9078133)

특별한 상황을 제외하고 유튜브 영상이나 드라마를 뒤에서부터 보는 사람은 아무도 없습니다. 왜냐하면 이해되지 않기 때문이죠. 왜 이해되지 않을까요? 그것은 모든 현상에는 원인이 있기 때문입니다. 어떤 사람을 이해하기 위하여 그의 과거를 이해해야만 하듯 현재 모습을 이해하기 위해선 그 원인을 알아야 합니다. 

그런데 컴퓨터 또한 인과관계에 귀속되어 있으므로 컴퓨터 과학을 공부해야 하는 우리는 그것을 있게 한 원인부터 알아보아야 합니다. 왜냐구요? 그것은 여러분이 유튜브 영상이나 드라마를 처음부터 보는 이유와 똑같습니다. 처음부터 안보면 제대로 이해할 수 없기 때문입니다. 

그러면 컴퓨터를 탄생시킨 것은 무엇입니까? 컴퓨터를 탄생시킨 것은 튜링의 논문 **《On Computable Numbers, with an Application to the Entscheidungsproblem》**(계산가능한 수에 대해서, 수리명제 자동생성 문제에 응용하면서) 에서 제안된 튜링기계라는 수학적 대상물입니다. 

그렇다면 이 튜링의 아이디어는 어디에서 나왔습니까? 튜링의 아이디어는 괴델의 논문 **《Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I》**(『수학원리』 및 그와 연관된 체계들 속에서 형식적으로 결정될 수 없는 명제에 관하여) 에서 나온 [불완전성 정리(Incompleteness Theorems)](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)에 대한 논증법에서 착안되었습니다. 

아니 그러면, 괴델의 불완전성 정리는 또 어떻게 나온 것입니까? 

지금부터 이것에 관한 이야기를 좀 하겠습니다. 이렇게 컴퓨터의 본질와 원류에 대한 역추적을 하는 이유는 다시 한 번 말하지만 거창한 이유가 아니라 단지 유튜브 영상이나 드라마를 처음부터 보는 이유와 똑같습니다. 컴퓨터를 좀 더 이해해서 좀 더 좋은 프로그래머가 되기 위해서입니다. 

> 그러니까 여러분도 너무 비장한 마음을 갖거나 긴장하지 마세요. 아, 그냥 지금까지 너무 길어서 처음부터 못보고 있었던 유튜브 영상 혹은 드라마를 처음부터 보는 시간이구나 라고 생각하세요. 

# 수학의 역사 

## 고대의 수학 

> 기원전 600년 ~ 기원전 300년

고대에는 손으로 수를 셈하면서 수의 개념이 추상화되었고 허벅지와 종아리가 이루는 모양을 관찰하는 것으로부터 각도의 개념이 추상화되었습니다. 원시문명에서도 물물교환, 시간기록, 땅 넓이 계산 등의 생계활동으로 인하여 자연히 수와 사칙연산 등의 수학적 개념이 추상화되었습니다. 

고대 그리스는 상형문자를 버리고 알파벳을 받아들였는데 이로써 더 자유롭고 쉽게 생각을 언어로 변환할 수 있게 됨으로써 지식의 발전이 가속화되었습니다. 이 시기에 기하학, 소수, 수열, 비례식 등이 연구되었는 유클리드가 고대 그리스의 수학을 정립하여 13권의 『원론』 을 집필했습니다. 

## 유클리드 『원론』 

> 기원전 330년 ~ 기원전 320년

유클리드는 공리로 『원론』을 시작했습니다. 공리란 더 이상 증명하지 말고 그냥 올바른 사실이라고 받아들이자고 약속한 명제입니다. 유클리드는 모든 수학적 대상물들을 이 공리로부터 추론된 정리로 구성하려 했습니다. 그래서 그는 모든 수학적 진술을 공리로부터 연역하려 했고 이로써 하나의 거대한 연역 체계를 만들었습니다.

- 예를 들어 『원론』 1권의 정리 1 은 **"유한한 길이의 직선으로 정삼각형을 만들 수 있다."** 입니다. 

  이 정리에 대한 증명을 보이겠습니다. 증명에는 정의 15 **"어떤 선으로 둘러싼 도형이 있어서, 한 점에서 직선들을 그었을 때 그 도형이 놓이는 부분이 모두 서로 같으면 그 도형을 원이라 한다."** 와 공리 1 **"모든 점에서 다른 모든 점으로 직선을 그을 수 있다."**, 공리 3 **"모든 점에서 모든 거리를 반지름으로 해서 원을 그릴 수 있다."** 이 필요합니다. 

  |증명|
  |:---|
  |주어진 선분을 ![](https://latex.codecogs.com/svg.latex?\overline{AB}) 라고 하자. 그러면 공리 3 에 의하여 두 점 ![](https://latex.codecogs.com/svg.latex?A,B) 를 중점으로 원을 그릴 수 있다. 두 원의 교점을 ![](https://latex.codecogs.com/svg.latex?C) 라고 하자. 공리 1 에 의하여 두 점 ![](https://latex.codecogs.com/svg.latex?A,C) 와 ![](https://latex.codecogs.com/svg.latex?B,C) 를 잇는 선분을 그을 수 있다. 정의 15 에 의하여 ![](https://latex.codecogs.com/svg.latex?\overline{AC}) 와 ![](https://latex.codecogs.com/svg.latex?\overline{AB}) 는 길이가 같다. 또한 정의 15 에 의하여 ![](https://latex.codecogs.com/svg.latex?\overline{BC}) 와 ![](https://latex.codecogs.com/svg.latex?\overline{AB}) 는 길이가 같다. 그러므로 세 직선 ![](https://latex.codecogs.com/svg.latex?\overline{CA},\overline{AB},\overline{BC}) 의 길이가 모두 같다. 그러므로 삼각형 ![](https://latex.codecogs.com/svg.latex?\triangle{ABC}) 는 정삼각형이다. ■ |

  <div align="center">
  <img src="https://t1.daumcdn.net/cfile/tistory/99F0C6425C15CFD828" width="50%" height="auto">
  </div>

  정말로 공리로부터 시작하여 정리가 연역되네요! 

『원론』에는 이런 정리들이 467개 있는데 10개의 공리에서 위와 같이 연역된 것입니다. 이 『원론』으로 인하여 현재 수학이라는 학문의 의미가 정립되었습니다. 즉, 수학이란 명백해보이는 명제를 증명없이 참으로 받아들여서 공리로 정하고 이것으로부터 수많은 정리를 연역해내는 학문이 되었습니다.

> 이 『원론』 으로 수학이 시작되었기에 인류 역사상 가장 중요한 책이라고 말하는 학자도 있습니다. 『원론』 은 인류가 『성경』 다음으로 가장 많이 읽은 책이기도 합니다. 

### 수학에 대한 인식

위와 같은 연역적 추론만으로 결론을 확립해야 한다는 방식, 즉 진리를 얻기 위하여 진리로부터 출발해야 한다는 방식도 후대에 그대로 전수되었습니다. 그리고 이 시기에 수학이 현실 세계를 직접 추상화한 것이므로 수학이 물질세계의 본질이고 수학이 자연의 짜임새과 구조를 알려준다는 인식이 생겼고, 한 대상의 추상화로 얻어낸 수학의 추상 법칙을 다른 자연적 대상에 적용할 수 있다는 인식이 생겼습니다. 이 인식도 후대에 받아들여졌습니다. 

## 로마의 등장 

> 기원전 27년 ~ 476년

하지만 로마인이 등장하면서 수학의 역사의 관점에서는 재앙의 역할을 했습니다. 로마의 국교로 기독교가 제정되었는데 기독교의 융성은 수학사에서 불행이었습니다. 이교도를 금지했기에 수많은 그리스 책들이 불태워졌기 때문입니다. 

## 인도와 아라비아 수학

> 200년 ~ 1200년

인도인들은 제단을 만들면서 기하학을 익혔고, 빚을 나타내기 위하여 음수의 개념을 생각했고, 그리스인들과 달리 무리수를 과감히 수로 취급하면서 유용한 결과를 많이 얻어내었습니다. 그러나 인도인들에게 엄밀한 연역과 증명, 공리적 방법은 없었습니다. 

아라비아 사람들은 대수학(algebra) 라는 이름을 만들었습니다. 아라비아 사람들의 업적이란 인도와 그리스 수학을 물려받아 잘 갖고 있다가 유럽에게 물려준 것이었습니다.

## 중세 유럽

> 400년 ~ 1100년

로마는 멸명하기 전에 기독교를 유럽에 전파했습니다. 이 때문에 유럽에서는 성직자를 양성하기 위하여 고등 교육 기관이 생겨났고 옥스퍼드 대학교, 케임브리지 대학교 등이 설립되었습니다. 1100년 십자군 전쟁으로 유럽인들이 아라비아 땅으로 가게 되었고 그곳에서 보존되어 있던 그리스 학문을 배우기 시작했습니다. 그리스 학문의 존재를 알게 되자 그리스 학문 번역서에 대한 관심이 막대하게 일어났지만 당시 번역본의 질은 너무 떨어졌습니다. 그럼에도 유럽인들은 그리스 학문에 매료되었습니다. 

## 중세 초기 이후 유럽

> 1100년 ~ 1450년

이 시기 수학 연구가 옥스퍼드 대학교, 파리 대학교, 빈 대학교에서 집중적으로 이루어졌습니다. 이 시기 학자들은 주로 고전의 저작을 읽고 해석하여 질 높은 번역본을 제작하는데에 온 힘을 기울였습니다.

## 르네상스 유럽 

> 1400년 ~ 1600년

르네상스의 모태인 이탈리아에서는 음모, 학살, 전쟁이 끊이지 않았습니다. 교황을 상대로한 전쟁이 계속 일어나면서 교회에 대한 지적 저항도 일어났습니다. 부패한 교회를 향한 루터과 칼뱅의 종교개혁이 일어났고 이 상황들은 자유롭고 비판적인 사고방식, 즉 수학을 발전시키기에 너무나도 좋은 사고방식을 정착시켰습니다.

또한 이탈리아는 지리적 요건 때문에 엄청난 부를 축적할 수 있었는데 이 부는 학문을 연구할 수 있는 여유를 제공해주었습니다. 한편 중세 초기 학자들이 질 높은 번역본을 만들려고 노력한 결과로 질 높은 그리스 저작들이 쏟아졌습니다. 그 저작들이 축적된 부를 만나서 학문 발전과 지식 전파를 가속화 시켰습니다. 

이 시기 코페르니쿠스, 케플러, 갈릴레오, 파스칼, 데카르트, 뉴턴, 라이프니츠 등의 학자들은 하나님이 온 우주를 수학적으로 창조했다고 거듭 강조했습니다. 그리고 하나님이 우주를 창조할 때 수학적 추상 법칙을 심어주었다고 믿었고 이 때문에 수학이란 자연의 불변의 법칙을 연구하는 절대적인 학문이라는 인식이 널리 퍼졌습니다.

### 르네상수 수학 연구 

여러분이 잘 알듯이 현재의 기호 체계, 대수학, 좌표평면, 함수 등의 수학적 개념이 이 시기에 정립되었습니다. 함수 개념이 도입되자 17세기에 곧바로 주요 과학 문제를 해결하기 위하여 뉴턴과 라이프니츠에 의해 미적분학이 탄생했습니다. 그러나 뉴턴과 라이프니츠가 자신이 내놓은 미적분학의 기본 개념들조차 명확하고 엄밀하게 정의하지 못하다 미적분학 자체가 엄밀하지 못하다는 비판을 받았습니다. 

하지만 수학자들은 엄밀하지 못한 논리적 토대에서도 열정만으로 수학 연구를 진행시켰습니다. 그리고 그 열정 이면에는 자신이 연구하는 수학 법칙이 자연으로부터 추상화된 것이고 하나님이 심어놓은 불변의 법칙이기 때문에 엄밀한 논리적 토대를 의심하지 않는 마음이 있었습니다. 

## 18세기 수학 

> 1700년 ~ 

르네상스 시기의 수학에서만 해도 수학 개념은 현실 세계에서 직접적 추상화를 거쳐 나온 것이었습니다. 하지만 18세기의 수학에는 그러한 1차 추상물로부터 더욱 추상화된 도함수, 적분, 다변수함수 미적분, 미분방정식, 무한급수 등의 개념이 도입되었습니다. 

동시에 미적분학의 논리적 기초를 마련하려는 노력은 계속되었습니다. 18세기 거의 모든 수학자 즉, 오일러, 라그랑주, 달랑베르, 라크루아 등이 미적분의 기초를 확립하려고 애썼지만 대다수의 노력이 아무런 성과가 없었습니다.

이렇게 미적분의 기초가 없음에도 미적분 연구는 계속되었는데 이는 수학자들이 물리적이고 직관적인 의미에 의지했었고 마음 속에 한 가지 단순한 모델을 지니고 있었기 때문이었습니다. 그 단순한 모델은 다항함수, 유리함수 같은 간단한 함수였습니다. 하지만 오일러의 혼합 함수, 비정칙 함수, 불연속 함수 등으로 연구를 확대해야 할 때 더 이상 그 단순한 모델에 빗대어 수학 연구를 진행할 수 없었습니다. 심지어 로그함수를 음수와 복소수로 확장해야 할 때 수학자들은 더 이상 의지할 대상이 없이 연구를 진행했습니다. 연구 성과가 나올 수 있었던 것은 오직 연산 규칙이 명확했다는 이유였습니다.

어떤 수학자들은 엄밀성 확보를 포기하며 유클리드의 『원론』의 엄밀함과 연역 체계를 이루는 공리적 방식이 너무 지나친 엄밀함이라고 비판하기까지 했습니다. 수학자들은 르네상스 때와 마찬가지로 하나님이 세계를 수학적으로 짰기 때문에 엄밀함 없이도 수학 이론들을 진리라고 믿을 수 있었습니다. 

이렇게 많은 논란이 있었으나 19세기까지 미적분학의 엄밀한 논리적 토대는 마련되지 않았습니다. 

## 19세기 수학

> 1800년 ~ 

19세기에는 수학이 특권층 출신의 소수에 의하여 발전되는 것이 아니라 폭넓은 계층의 집단에게 확대되었고 이에따라 모든 계급에서 라플라스, 르장드르, 푸리에, 가우스 등의 학자들이 몰려들었습니다.

> 실제로 가우스는 집안 사정 때문에 벽돌 굽는 노동자가 될 운명이었지만 어머니의 전폭적인 지원으로 수학자가 될 수 있었습니다.

미적분학이 18세기를 지배했다면 복소수함수가 19세기를 지배했습니다. 가우스가 복소수 변수 함수에 관한 기본 개념을 도입했습니다. 복소함수론이 정립되자 아벨과 야코비에 의해 타원함수와 아벨함수를 다루는 연구가 진행되었습니다. 이후 가우스의 제자 리만이 수학의 새 시대를 이끌어 갔습니다. 

### 대수학 연구 

어떤 방정식이 대수적으로 풀리는지에 대한 연구가 갈루아에 의해 해명되었고 그가 최초로 대수학 이론을 일관되게 정립했습니다. 

### 사원수 

수학자들은 속도 같은 방향을 나타내는 선분인 2차원 평면 벡터를 복소수로 표현할 수 있다는 것을 알고 있었습니다. 그러나 한 물체에 여러 힘이 작용하는 대상물도 존재했고 수학자들은 이것을 표현하기 위하여 여러 힘을 대수적으로 다루기 위한 수학적 대상물이 필요했습니다. 따라서 수학자들은 3차원 복소수로 공간 벡터를 표현하려고 애썼습니다. 해밀턴도 수년간 새로운 복소수를 찾으려고 노력한 끝네 3차원에 해당하는 복소수를 찾았으나 새로운 복소수를 위하여 다음 2가지를 포기해야 한다는 것을 알았습니다. 

1. 새로운 복소수는 성분이 3개가 아니라 4개이다. 

2. 새로운 복소수는 교환법칙이 성립하지 않는다. 

해밀턴은 이 새로운 복소수를 사원수(quaternion)라고 불렀습니다. 

### 사원수 발견의 의미 

수학자들은 실수와 복소수의 교환 법칙을 만족하지 않는데도 의미있고 유용한 수체계가 존재한다는 것을 깨달았습니다. 이 깨달음은 인류가 직관적으로 자명하다고 여겨왔던 실수와 복소수 체계가 사실은 인간의 창조물이었다는 것을 알려주었습니다. 그리고 이에 따라 수학자들은 사원수 이외에도 여러 다른 수 체계가 존재할 수 있음을 알게 되었습니다. 이것은 인류 지성사의 전환점이었습니다. 

고대 그리스로부터 온 우주가 수학으로 짜여져있다는 믿음이 중세 유럽으로 전수되었고 이후의 유럽인들은 하나님이 세상을 수학적으로 짰기 때문에 수학과 자연이 정확히 대응된다고 믿어왔습니다. 수학이 자연을 추상화시킨 것이므로 수학이 자연의 본질이라면 수학의 모순을 걱정하는 것 자체가 어불성설이었습니다. 하지만 사원수로 인하여 인류가 굳건히 믿어왔던 불변의 수 체계 실수와 복소수 이외에도 다른 수 체계가 존재한다는 것이 알려진 것입니다. 이로써 수학의 위상은 신의 창조물에서 인간의 창조물로 추락했고, 이로써 수학에 모순이 있을 수도 있다는 비극적인 인식이 수학자들 사이에 퍼지기 시작했습니다. 

실제로 사원수 발견 이후 해밀턴은 또 다시 겹사원수를 제시했고 클리포드는 다원수를 만들어냈습니다.

### 행렬 

지금까지의 도함수 같은 수학적 대상물들은 물리적 현상을 직접적으로 추상화시킨 개념이지만 이것과 달리 순전히 인간 지성의 창조물인 행렬식과 행렬이 탄생했습니다. 행렬을 최초로 독립된 대상으로 다룬 이는 케일리라서 그가 행렬 창시자로 여겨집니다.

## 비유클리드 기하학 

1800년경까지 모든 수학자들이 유클리드 기하학이 물리 공간과 그 공간 안에 있는 도형의 성질을 올바르게 이상화한 체계라고 믿었습니다. 마치 사원수가 발견되기 전에 사람들이 수론이 자연적 대상을 참되게 이상화한 불변의 체계라고 믿었던 것처럼 유클리드 기하학만큼은 인간의 창조물이 아니라 신의 창조물이고, 자연 대상의 도형에 관한 진리를 참되게 보여주고 있다고 믿어온 것입니다. 이 믿음이 얼마나 강했던지 수학자들은 논리적 기초가 부족했던 산술과 대수학, 해석학을 유클리드 기하학의 기초 위에 세움으로써 각각의 수학 체계의 참됨을 간접적으로 인정받으로 했습니다. 

하지만 이 대다수의 생각을 데이비드 흄이 『인간 본성에 관한 연구』(1739) 를 집필함으로써 정면으로 부정했습니다. 흄은 인간이 일련의 자연적 대상을 관찰함으로써 자의적으로 인과관계를 규명해낸 것이므로 유클리드 기하학 법칙들이 물리 세계의 진리라는 이유가 없다고 주장했습니다. 하지만 이 흄의 영향력은 칸트에 의하여 부정되었고 전복되었습니다. 칸트는 『순수 이성 비판』(1781) 을 집필함으로써 물리 세계가 정확히 유클리드 기하학을 따른다고 주장했습니다. 동시대 사람들은 흄이 아닌 칸트를 따랐습니다. 

### 『원론』 의 공리 5 : 평행선 공리

이처럼 유클리드 기하학이 물리 세계의 참된 이상화라는 믿음은 기원전 3000년에서 1800년경까지 흔들리지 않았습니다. 그 종교적인 믿음은 유클리드 기하학만큼은 절대로 인간의 창조물이 아니고 인간이 발견한 자연의 불변의 법칙이라는 믿음이었습니다. 

하지만 수학자들은 그 참됨을 의심한 것은 아니지만 유클리드 『원론』의 공리 5, 이른바 평행선 공리 **"두 개의 직선이 있고, 다른 한 직선이 두 개의 직선과 만나는데, 어느 한쪽의 두 내각을 더한 것이 ![](https://latex.codecogs.com/svg.latex?180\degree) 보다 작다고 하자. 그러면 두 직선을 길게 늘였을 때, 두 직선은 내각을 더한 것이 ![](https://latex.codecogs.com/svg.latex?180\degree) 보다 작은 쪽에서 만난다."** 를 마음에 들지 않아했습니다. 수학자들이 평행선 공리를 마음에 들지 않아 한 이유는 평행선 공리가 다른 공리보다 복잡해서 공리가 지녀야 한다고 여겨지는 간결함이 결여되어 있기 때문이었습니다.

- 다음 그림이 평행선 공리를 보여줍니다. 두 직선이 있을 때 다른 한 직선이 두 개의 직선과 만납니다. 그런데 두 내각 ![](https://latex.codecogs.com/svg.latex?\alpha,\beta) 를 더한 것이 ![](https://latex.codecogs.com/svg.latex?180\degree) 보다 작습니다. 그러면 두 직선을 길게 늘리면 두 직선은 두 내각 ![](https://latex.codecogs.com/svg.latex?\alpha,\beta) 이 있는 방향에서 만납니다. 

  <div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Parallel_postulate_en.svg/600px-Parallel_postulate_en.svg.png" width="50%" height="auto">
  </div>

수학자들은 이 의구심을 제거하기 위하여 『원론』의 나머지 9개의 공리에서 평행선 공리를 연역해내려고 노력했습니다. 이것이 성공한다면 평행선 공리는 평행선 정리가 되므로 자연히 의구심이 사라지게 될 것이기 때문이었습니다. 그러나 이 시도는 모두 성과를 거두지 못했습니다. 

그 시도들 중에서 사케리(1667~1733) 의 시도가 그나마 유의미한 성과를 냈었습니다. 사케리는 유클리드 평행선 공리와 대치되는 공리를 채택할 경우 모순되는 결과가 도출된다고 결론 내리면서 평행선 공리는 진리라고 주장했습니다. 

### 비유클리드 기하학의 전조 

사케리의 연구를 알고 있던 게오로크 S. 클뤼겔(1739~1812) 는 논문을 써서 평행선 공리가 진리라고 확신하는 근거가 경험에 있다고 주장했습니다. 이 주장은 매우 유의미한데 지금까지 평행선 공리를 자명함 때문이 아닌 경험에 의거하여 인정해왔다는 것이 밝혀졌기 때문입니다. 이에따라 클뤼겔은 사케리가 모순을 얻어낸 것이 아니라 단지 경험과 배치되는 결과를 얻어내었다는 것을 보여주었습니다. 

클뤼겔의 논문 이후에 람베르트, 카를 슈바이카르트, 타우리누스가 평행선 공리와 대치되는 명제를 채택하여 유클리드 기하학과 전혀 다른 기하학을 구성할 수 있다는 것을 확신했습니다. 하지만 이 세 사람 또한 비유클리드 기하학은 단지 모순이 없는 조금 신기한 수학 이론으로 여겼고 물리 세계에 적용되는 기하학은 유클리드 기하학이라고 생각했습니다. 

### 비유클리드 기하학의 탄생 

그러나 유클리드 기하학의 물리적인 참됨을 보장하는 근거는 어디에도 없었습니다. 가우스(1777~1855)는 비유클리드 기하학의 연구를 통해 이것을 깨달았고 심지어 물리 세계에 적용할 수도 있다는 것을 알아냈습니다. 그러나 그는 조롱이 우려되서 비유클리드 기하학에 대한 연구를 발표하지 않았습니다. 

흔히 로바체프스키(1793~1856)와 보여이(1802~1860) 두 사람이 비유클리드 기하학의 창시자로 여겨집니다.

가우스, 로바체프스키, 보여이는 평행선 공리가 나머지 9개 공리로부터 연역될 수 없다는 것을 깨달았습니다. 그리고 평행선 공리는 독립적이므로 이와 배치되는 공리를 택하여 새로운 공리 체계를 얻어낼 수 있는데 이 공리 체계는 논리적으로 아무런 문제가 없다는 것도 알아냈습니다. 

### 비유클리드 기하학의 의미 

비유클리드 기하학의 발명은 그리스 이래 가장 혁명적인 사건이었습니다. 왜냐하면 유클리드 기하학만큼은 인류가 인간의 창조물이 아닌 신의 창조물이고 자연의 불변의 법칙을 보여주고 있다고 굳게 믿어왔기 때문입니다. 칸트가 틀렸고 흄이 옳았던 것입니다. 

가우스는 유클리드 기하학이 반드시 물리 세계의 기하학이 아닐 수도 있다는 것을 깨닫고 수학의 참됨을 산술에서 찾으려 했습니다. 그러나 이후에 믿었던 산술도 사원수의 탄생으로 변하지 않는 불변의 진리가 아니라는 것을 깨달았습니다.

비유클리드 기하학의 탄생은 인간이, 아니 그 인간 중에서도 매우 논리적이고 객관적으로 사고한다고 여겨졌던 수학자들까지도 스스로의 추론이 아니라 얼마나 시대정신에 영향을 받는지를 극명하게 보여주었습니다. 객관적으로 생각했다고 믿어왔는데 결국 주관적인 생각에 불과했고 모든 믿음과 지식의 토대가 인간의 오만함에서 비롯된 착각이었던 것입니다. 인간은 자신이 만들어낸 창조물임에도 그것이 불변의 진리라고 믿었고 영원불멸하는 신적인 존재라고 추앙했던 것입니다. 

이에 따라 비유클리드 기하학과 유클리드 기하학에도 모순이 있는지 묻는 무모순성 문제가 제기되었습니다. 유클리드 기하학이 자연과 물리 세계에 완벽히 대응된다고 믿었을 때만 해도 모순이 있는지 의심하는 사람이 바보였습니다. 하지만 유클리드 기하학이 인간의 창조물이라는 것이 드러난 시점에서 아직까지 유클리드 기하학이 불변의 진리라고 믿는 사람이 바보가 되었습니다. 

또한 이로써 얼마든지 새로운 기하학이 창조될 수 있다는 인식이 생기게 되었습니다. 실제로 사영기하학, 타원기하학, 이중타원기하학, 아핀기하학 등이 생겨났습니다. 

비유클리드 기하학으로 공리의 자명함이라는 개념 자체가 위상을 잃었고 지금까지 가장 엄밀하고 객관적이라고 여겨졌던 증명에도 문제가 있다는 것이 드러났습니다.

## 해석학의 엄밀성 문제 

> 1800 ~

1800년경 수학자들은 해석학 분야의 논리적 허점을 보완하려 했습니다. 몇몇 수학자들은 산술 만큼은 참되다고 믿었기에 산술의 개념 위에 해석학을 세우려 했습니다. 가우스도 결국 유클리드 기하학의 참됨에 의구심을 드러냈지만 산술만큼은 참되다고 결론 내렸었습니다. 

## 실수의 기초 

> 1850 ~

수학사에서 가장 놀라운 사실은 19세기말까지 실수 체계의 논리적 토대가 세워지지 않았다는 것입니다. 대수학과 해석학이 광범위하게 발전했지만 실수의 정확한 구조와 성질을 파악하지 못한 사실은 수학이 얼마나 비논리적으로 발전해왔는가를 보여줍니다. 

수학자들이 해석학의 엄밀성을 수론에 기초를 둠으로써 수론의 무모순성도 해결해야 한다는 자각이 생겨났습니다. 또한 수학자들은 비유클리드 기하학으로 인하여 기하학이 진리로써의 위상을 상실했기 때문에 수론의 기초를 정립하여 수학의 참됨을 바로세우려 했습니다. 

실수 체계의 논리 구조에 대한 문제의 난점은 무리수였습니다. 그런데 무리수의 의미와 성질을 파악하기 위해선 유리수 체계의 확립이 선행되어야 했습니다. 칸토어와 데데킨트가 유리수를 기반으로 무리수 이론을 구성해내었습니다. 그리고 이들은 유리수와 무리수를 포함하는 수로써 실수 개념을 제시했습니다. 

특히 칸토어는 집합론을 창시하고 실수집합 구조를 이해하기 위하여 무한집합 개념을 도입했습니다. 

### 유리수의 기초 

그 다음 단계는 유리수의 기초를 확립하는 것이었습니다. 유리수는 자연수로부터 도출될 수 있었기 때문에 수학자들은 자연수의 논리 토대를 마련하려 했습니다. 바이어슈트라스가 1860년대에 자연수에서 유리수를 도출해내는데 성공했습니다. 페아노(1858~1932) 도 공리적 방식으로 자연수를 구성해내었습니다. 이렇게 자연수에 대한 논리적 토대가 확립되자 실수 체계의 기초를 건설하는 문제는 마무리 되었습니다. 

## 기하학의 기초 

비유클리드 기하학의 탄생으로 기하학의 기초를 확립해야 한다는 인식이 생겨 수학자들은 기하학의 기초를 확립하는 문제에 천착했습니다. 먼저 힐베르트는 비유클리드 기하학을 유클리드 기하학으로 환원함으로써 유클리드 기하학이 참되면 자동으로 비유클리드 기하학도 참됨을 보였습니다. 이후 힐베르트는 산술적 해석을 통하여 산술에 의존하여 유클리드 기하학의 무모순성을 보였습니다. 

그러므로 이제 문제는 산술입니다. 즉, 수론에 모순이 없다면 유클리드 기하학에도 모순이 없는 것이고 그 위에 세워진 해석학을 비롯한 모든 수학 체계가 모순이 없는 것이 됩니다. 

하지만 산술 또한 사원수의 등장으로 그 참됨이 의심받게 되었습니다. 산술에 대한 최초의 의혹은 헬름홀츠의 『계산과 측정』(1887) 에서 나왔습니다. 그는 산술 자체는 산술 연산의 논리적 결과를 일관되게 설명하는 방식에 불과할지도 모른다고 주장했습니다. 그러니까 마치 수론이 바둑이나 체스, 혹은 인간이 정한 게임 규칙처럼 인공적인 창조물에 불과할지도 모른다는 의혹이었습니다. 

따라서 힐베르트는 산술의 무모순성 문제를 1900년대 세계수학자대회에서 발표한 [문제 목록의 2번째 문제](https://ko.wikipedia.org/wiki/%ED%9E%90%EB%B2%A0%EB%A5%B4%ED%8A%B8_%EB%AC%B8%EC%A0%9C)로 포함시켰습니다. 

## 인간의 창조물인 수학 

고대 그리스인, 데카르트, 뉴턴, 오일러, 칸트를 비롯한 많은 이들이 수학이 실제 현상의 정확한 서술이고 진리라고 믿었지만 사원수와 비유클리드 기하학으로 인해 수학자들은 수학이 인위적인 창조물임을 인지하였습니다. 칸토어는 수학이란 현실세계과 관계없이 자유롭게 개념을 만들어내고, 그 수학적 대상물들은 오로지 무모순성이라는 조건에만 구애 받는 매우 자유로운 존재라고 했습니다. 

## 진리의 상실 

19세기 말에 수학의 모든 공리가 사람이 임의로 택한 명제에 불과하다는 견해가 득세하기 시작했습니다. 공리는 연역의 기반일 뿐 진리가 아니었습니다. 이로써 1900년대 수학은 물리 세계와 단절되었습니다. 즉, 수학 연구가 자연에 대한 진리를 찾는 것이 아닌 무의미한 인공적 대상물들에 관한 임의의 공리의 논리적 귀결을 찾는 학문임이 드러난 것입니다. 수학자들은 이 사태를 도무지 믿지 못했습니다. 에르미트, 힐베르트, 하디가 이 사태에 대한 부정적 견해를 표출했습니다. 특히 힐베르트는 1928년 세계수학자대회에서

*“수학에 진리가 없다면 그 발전은 어떻게 된다는 말입니까? 오늘날 회의주의와 낙담의 소리를 듣지만 이 모두를 우리에게 해악을 주는 일종의 주술이라고 생각합니다.”*

라고 말했습니다. 

## 수학의 기초 

러셀은 칸토어가 창시한 집합론에 역설이 존재함을 보였습니다. 이뿐 아니라 집합론에 관련된 여러 역설이 나왔습니다. 체르멜로가 칸토어 집합론의 소박한 전개 방식을 공리화하였고 프렝켈이 1922년에 이 공리 체계를 좀 더 개선하여 역설을 없앴습니다. 그러나 이 과정에서 사용된 선택 공리는 논란거리였고 아직도 수론의 무모순성은 증명되지 않았었습니다. 

이 상황에서 수학의 기초를 마련하려는 학파들 즉,  러셀의 논리주의 학파, 직관주의 학파, 힐베르트의 형식주의 학파가 생겼습니다. 

### 논리주의 학파 

러셀과 화이트헤드는 논리주의 학파를 창시하고 수학을 논리학으로부터 연역해내려고 했습니다. 이들은 논리학의 공리에서 산술을 연역해내었고 결국 해석학도 연역해내었습니다. 즉, 명제함수를 다루면서 집합론으로 내용을 전개한 후 그 기초 위에서 자연수를 도입했습니다. 자연수가 정의되면 실수, 복소수, 함수, 해석학, 기하학 전체를 구성할 수 있었고 이 내용을 『수학 원리』 에 담아 출판했습니다. 러셀은 논리학 공리만큼은 불변의 진리라고 믿었던 것입니다. 하지만 그는 이 견해를 1937년판 『수학 원리』 에서 버렸습니다. 

### 형식주의 학파 

힐베르트는 형식주의 학파를 창시하여 집합론을 사용하지 않고 수론의 기초를 마련하여 산술의 무모순성을 확립하려 했습니다. 힐베르트와 그 제자들, 폰 노이만 등은 힐베르트의 증명 이론, 즉 메타수학이라는 분야를 발전시켰습니다. 이것은 모든 수학 분야의 무모순성을 확립하는 방법론을 다루고 있었습니다. 이들에게 수학이란 무의미한 기호들을 기계적으로 조작하는 일련의 과정이었습니다. 즉 수학은 형식적 기호 체계의 모임입니다. 각각의 체계는 각자의 공리와 각자의 추론 규칙으로 각자의 정리를 도출합니다. 그러므로 수학의 임무란 연역 체계의 전개에 불과합니다. 이것은 몇 가지 공리와 몇 가지 추론 규칙으로 기계적으로, 즉 자동적으로 모든 수학적 진리를 이끌어낼 수 있다는 힐베르트 프로그램이었습니다. 

앞서 언급했듯 힐베르트는 기하학과 물리학의 무모순성을 산술의 무모순성으로 귀결시켰고, 형식주의자들은 얼마 안가 힐베르트 프로그램으로 산술의 무모순성을 확립할 수 있을 거라고 믿었습니다. 

## 괴델의 불완전성 정리 

하지만 괴델이 등장하여 불완전성 정리를 발표함으로써 어떤 공리 체계의 공리와 추론규칙으로는 그 체계의 무모순성을 확립할 수 없다는 것을 보였고, 더욱 충격적이게도 수론을 포괄하기에 충분한 형식 체계라면 반드시 증명될 수 없는 참인 명제를 갖고 있다는 것을 보였습니다. 

괴델의 결과는 러셀-화이트헤드 체계, 체르멜로-프랭켈 체계, 힐베르트의 공리화된 수론에 적용되었습니다. 

그렇다면 증명될 수 없는 참인 명제를 증명하기 위해 몇가지 공리와 추론규칙을 추가하면 되지 않을까요? 하지만 괴델은 불완전성 정리로 추가적인 공리와 추론규칙으로 체계를 확장한다고 해도 그 안에서 또 다시 결정불가능한 명제가 탄생한다는 것 또한 보였습니다. 

이로써 어떠한 공리 체계도 수학 전체는 고사하고 수학의 한 분야도 모두 포괄할 수 없다는 것을 보여주었고, 유클리드의 『원론』 에서 시작되어 수천년간 내려져오며 불변의 진리라고 여겨졌던 공리적 방식, 즉 연역적인 추론에는 한계가 있다는 것이 드러났습니다. 

## 이후의 상황 

절대적 엄밀성과 절대적 객관성을 추구하려는 모든 시도는 수포로 돌아갔고 수학자들은 엄밀성이라는 의미 자체에서도 합의점을 찾을 수 없었습니다. 집합론의 공리화도, 논리주의 학파도, 직관주의 학파도, 형식주의 학파도 보편적으로 수용할 수 있는 진리에 대한 접근법 확보라는 목표를 성취하지 못했습니다. 수학이 오늘날에도 여전히 활발한 것은 순전히 그 실용성 때문입니다. 

- 이때 괴델이 메타 수학 명제를 수학 명제로 격하시키는 것에 대한 설명 

- 이 수학적 논증법으로 탄생한 컴퓨터 또한 메타 수학 명제를 수학 명제로 격하시키는 프로그래밍이라는 과정을 하는 것임!!!!!!!!!!!!!!!!! ( 이 부분 매우 매우 강조 )

  - 많은 예시를 들어서 이 부분 강하게 설득.

  - 단, 컴퓨터는 괴델의 불완전성 정리에서 메타 수학 명제를 수학 명제로 격하시키는 것과 약~~간은 다르게 튜링 머신에서 세상에 존재하는 어떤 기계도 텍스트로 변환할 수 있고 그 텍스트를 흉내낼 수 있는 대상임. 

  - 예시 

    무한대 서점이 망한 이야기. 즉, "서점에서 책을 사고 판다" 라는 명제를 수학 명제로 격하시키는 것임. 결국에 프로그래밍으로 "서점에서 책을 사고 판다" 는 명제를 완전한 수학 명제로 격하시키는 과정 보여줌. 

  - 예시 

    심지어 더 나아가서 감각기관을 수학 명제로 격하시키는 예시 보여줌. 그떄 하진이에게는 과도한 사고 실험과 뇌피셜로 설명했었지만, 컴퓨터 비전이라는 특정 분야에 대한 기술적 설명을 곁들여서 설득력있게 "시각적 감각기관" 을 수학명제로 격하시키는 것을 설득력있게 보여주자. OpenCV 로. 
  
  - 이러한 격하가 가능한 것은 "변환" 과 "대체" 가능하기 때문. 

    - 이 "변환" 과 "대체" 라는 두 키워드를 강하게 어필하자. 

    - 예시 

      사고 실험을 하나 해보겠습니다. 밤에 잘을 잘때 저는 불을 끄러 스위치를 내려야 합니다. 하지만 잠을 자고 싶을 떄면 저는 항상 몸이 많이 피곤해서 침대에 누운 상태였죠. 그럼에도 불구하고 침대에 누운 상태에서 스위치를 내리고 싶어서 그럴 수 있는 방법이 있는지 고민했어요. 결국 한 가지 아이디어를 떠올렸는데 침대 옆에 일종의 지렛대를 만들고 스위치까지 연결되게 한 다음 그 지렛대에 힘을 가하면 스위치까지 힘이 전달되도록 하는 기계를 만드는 것입니다. 

      그러면 이 기계는 "스위치를 내리는 행위" 를 대체할 수 있게 되었습니다. 대체할 수 있게 된 것은 힘을 변환(사상)시킬 수 있었기 때문입니다. 

      이제 이런 기술공학물을 프로그래밍으로 연결시켜보겠습니다. 시간이 흘러서 IoT 프로그래밍, 안드로이드 어플리케이션 프로그래밍을 배운 저는 지렛대로 힘을 변환하는 것보다 훨씬 세련된 방법이 있다는 것을 알았습니다. 그리고 스위치를 변환하는 장치를 IoT 시스템에 연결하고 안드로이드 어플리케이션을 하나 만들어서 스마트폰 버튼을 누름으로써 신호를 IoT 서버에 전달하고 IoT 서버는 다시 그 신호를 스위치로 전달하여 스위치를 내릴 수 있게 한 거죠. 

      이것으로 "스마트폰 버튼을 누르는 행위" 가 "정전기" 로 변환되고 "정전기" 는 스마트폰 스크린 좌표 신호로 변환되어 어플리케이션으로 전달되고 어플리케이션은 그 전기자극을 서버로 전달하고 서버는 다시 스위치로 전기자극을 전달해서 스위치를 내리게 되었습니다. 변환 형태가 지렛대와 비교하여 좀 달라졌지만 똑같이 "스위치를 누르는 행위" 를 기술 공학물로 대체할 수 있게 되었죠. 
    
    - 이런 통찰력이 있다면 여러분은 여러분이 다른 사람보다 더 잘 이해하고 있는 분야에 여러분만의 기술 공학물을 만들 수 있습니다.

      이 "변환" 과 "대체" 로 사람이 서로 대화하는 것을 수학 명제로 격하 시킬 수 있겠다 란느 아이디어를 내었던 사람들도 있었죠. 

      그게 뭔지 아십니까? 그게 카카오톡입니다. 이제 좀 실감이 나시나요? 
    
    - 우리 프로그래머는 코드로써 자연적 대상을 수학 명제로 격하시켜서 변환하고 대체할 수 있는 것입니다. 

      - 가령 이 "변환" 과 "대체" 로 인간이 이동하는 행위도 대체할 수 있습니다. 그게 뭐지 아십니까/ 그게 자동차입니다.
      
        자동차 공학자들은 인간의 이동하는 행위를 변환하고 대체하였죠! 

        자동차 공학자들은 인간이 걷는 행위에 들어가는 힘을, 페달을 밟는 행위로 변환했습니다. 이로써 페달을 밟는 것인 자동차 엔진을 작동시키고 엔진은 연료를 소모하여 동력을 얻어내고 그 동력이 바퀴를 굴러가게 해서 결국 인간이 페달만 밟아도 이동할 수 있도록 이동 행위를 대체할 수 있었습니다. 
  
    - 그러면 인간의 지능을 프로그램으로 대체할 수도 있지 않을까 라는 생각도 충분히 할 수 있죠? 

      만약 인간의 지능을 기계로 대체하여 자동화할 수 있다면 자동차라는 기계가 우리에게 주는 편의를 동일하게 받을 수 있겠지요? 인간이 끝없이 이동하면 지치는 것과 달리 자동차는 끝없이 이동해도 지지ㅣ 않으니까, 만약 인간의 생각, 학습, 성장, 고민, 지성 활동을 대체한다면 인간이 끝없이 공부하고 학문을 발전시키면 지치는 것과 달리 프로그램은 지치지 않겠지요? 

      그러면 한 가지 고민을 할 수 있습니다. 인간의 뇌의 구조가 뭐고 생각의 원리란 뭘까? 만약 그 뇌의 구조를 밝혀낼 수 있고 생각의 원리를 규명할 수 있다면 수학 명제로 격하시킬 수 있을 것이고, 인공적인 지능을 만들 수 있을텐데!

      또 다시 동일하게 "변환" 과 "대체" 라는 원리를 적용해볼 수 있습니다. 뇌과학에서는 인간의 뇌를 구성하는 뉴런의 동작 원리를 규명해놓았습니다. 이 동작 원리가 규명되었으니 곧 바로 그것을 수학 명제로 변환하여 지능을 대체할 수 있었습니다. 그게 바로 퍼셉트론입니다. 
    
      인공지능 신경망이 뭔지 아십니까? 그것은 뇌과학에서 밝힌 뇌 속의 뉴런을 퍼셉트론으로 변환하여 대체한 것입니다. 이 퍼셉트론으로 신경망ㅇ르 만들고 인간의 뇌의 뉴런들의 네트워크를 흉내낼 수 있엇습ㄴ다. 그 결과 아직 부분적이고 불완전하지만 인공적으로 인간의 지성 활동을 흉내낼 수 있었고 그것을 결국 인공지능이라 부를 수 있게 되었습니다. 이 인공지능이 오늘날 글자도 알아맞추고 운전도 스스로 하고 동영상 추천까지 해줍니다. 
    
    - 자, 오늘은 여기까지이고 이제 제가 만든 프로그램으로써 "변화" 과 "대체" 의 자세한 예시를 들어주겠습니다. "네모로직을 해결하는 인간의 사유과정" 을 수학명제로 격하시키고 이것을 프로그램으로까지 변환시켜서 대체하는 예시입니다. 

      - 이것은 안들으실 분들은 안들으셔도 되요! 수업은 이미 끝났습니다. 회의는 여기까지입니다. 
    
    - 이뿐 아니라 심지어 "컴퓨터를 사용하는 특정 행위" 또한 자동화 될 수 있다는 것을 아시나요? --> 수강신청 자동화.. 
  
  - 저는 이것을 아는 것이 프로그래머로써 정말 기본이라고 생각합니다. 프로그래머도 기술 공학자에요. 그러니까 여러분도 기술 공학자인 것입니다. 어떤 공학물을 만들려 하십니까? 어 나는 우리 아버지가 세금 계산을 하시는데 그 세금 계산이 하루에도 정말 수백 수천번 계산을 해야 해서... 그것을 자동화시키려 한다. 그러면 그 계산 행위를 명확하게 규명한 다음 수학 명제로 변환시키면 되죠. 

    자동화시키고 싶은 자연 대상을 단순화시킨 다음 수학 명제로 직접적으로 대응될 때까지 닩순화시키면, 그떄부터는 프로그램으로 변환시키기가 너무 쉬워지는 거죠. 
  
  - 하지만 영국 "   " 에서는 이 자동화에 관하여 경고했어요. 

  - 이 자동화의 끝에 기술적 특이점이 올것이다.. 이 기술적 특이점에 관하여서는 내일 얘기하겠습니다. 

    - 기술적 특이점은 SF 소설에 등장하는 이야기도 아니고 제 머리속에서 나온 뇌피셜도 아닙니ㅏ. 저명하고 위대한 수학자들이 수많은 고려 끝에 진중한 어조로 경고한 인류 역사상 가장 큰 변혁점입니다. 

    - 이 특이점을 언급함 최초의 인물은 폰 노이만입니다. 

    - 기술적 특이점이 대중에게 최초로 널리 알려지게 된 계기는 빌 조이의 "우리는 왜 필요없는 존재가 될 것인가?" 란느 블로그 글 때문이었습니다. 정말 추천합니다. 꼭 읽어보세요. 여러분 컴퓨터 공학자 아닙니까. 그러면 일반인과 차이가 있어야 하지않겠습니까? 컴퓨터 공학자라면 반드시 읽어보셔야 할 글 중 하나니까 시간 나실 떄 그 전문을 꼭 읽어보세요. 

- 그다음 저는 (튜링에 관한 책)

- 여럽누 미국에서는 19X0 대에(『계산기는 어떻게 인공ㄴ지능이 되었을까?』 참고) 늘어나느 계산량을 감당하기 위해 수많은 살마들을 고용하고 계산기 사ㅛㅇ법을 가르쳤습니다. 프로그래밍과 컴퓨터 공학의 본질을 이해하지 못한다면 당신은 단지 이와 같은 계산기의 사용법을 익힌 그 당시 미국에 고용된 사람들과 ㄱ다를 것이 전혀 없습니다. 

왜냐하면 기술의 본질을 모르기때문에 새로운것을 창조해내거나 앞서나갈 수 없기때문이죠.

- 또한 다가올 시대에서 이끌려다니기만할 것입니다. 왜냐하면 역사적으로 모든 순간 속에서  모든 공간 속에서 "이해한 사람이 이해하지 못한 사람을 지배해왔고 이끌어왔고 앞서가갔기 때문" 이죠

- 조금 인문학 적인 내용으로 이야기가 빠지긴 했는데 역사를 보려고 마음을 먹으신 분은 한가지 팁을 드리자면 역사 속에서 자신만의 철학을 세우세요. 본질이 뭐고 왜 역사가 이렇게 발전했고 ㅐㅑ자신만의 철학을 세우고, 수정해나가면됩니다.

그렇게 역사를 공부하면서 오늘날까지, 즉 최신기술 까지 공부하셨다면 지금까지 쌓인 자신의 철학을 바타으로 미래를 예측하세요. 그리고 그 예측을 바탕으로 앞으로 나아갈 길을 창조하고 선택하는거죠

저는 저만의 철학을 세ㅜ었습니다. 기술은 자연을 대체하는 것이고 그 자동화가 가속화되가다가 언젠가 초진응이 나타날것이다.

그 자신만의 철학이 올지않다고 드러났다고 해도 부끄러워하지 않아도 되고 기죽을 필요 없습니다. 그 철학ㄹ을 수정하면 됩니다. 수학 발전상을 보면 인류는 처음에 진리라고 믿었던 이론을 세웠짖맘ㄴ 그 이론이 틀렸다는 것이 드러났고 그 이론들을 수정해야만 했습ㅂ니다.

    (그러므로  인간에게 철학이 필요하다-왜냐면앞으로의 길을 선택해야 하기 때문에 따라서 철학을 세워야 하고  그 엄밀함이 부족하다고 드러났다고 해도 부끄러워할 이유가 없다 고치면 된다 는 공리를 기록해둬야함).