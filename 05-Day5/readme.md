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

(gdb, pwddbg, gdb-gef)

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

user.github.io 은 **Github** 이 제공하는 개인 블로그 플랫폼입니다. 저의 **Github** 아이디는 `ccss17` 인데 이 아이디로 user 를 치환하여 https://ccss17.github.io 에 접속해보면 제가 관리하고 있는 블로그가 보입니다. 이 블로그는 https://github.com/ccss17/ccss17.github.io 의 `index.html` 파일과 각각의 `*.html` 파일들이 랜더링 된 것입니다. 

이처럼 **Github** 에 아이디만 있다면 자신의 아이디로 user.github.io 라는 이름을 가진 레포지토리를 생성하고 그곳에 `index.html` 과 메모하거나 게시하고 싶은 정보를 `.html` 파일로 만들어 레포지토리를 **commit** 하고 **Github** 에 **push** 하면 자동으로 user.github.io 에 게시가 시작됩니다. 

> [**jekyll**](https://jekyllrb.com/) 을 사용하면 `.md` 파일만으로도 웹페이지를 생성할 수 있어 매우 편합니다. 

개인 블로그에 자신이 공부한 내용이나 알아낸 사실을 게시하면 그것이 모두 다 포트폴리오가 되고 스펙이 되서 자신의 가치를 높이는 일이 됩니다. 그러나 이 블로그 플랫폼을 사용하고 싶지 않은 분들도 있음을 감안해서 더 이상의 상세한 설명과 실습은 하지 않고 유명한 `*.github.io` 사이트들과 **Github** 의 공식 메뉴얼과 저의 https://ccss17.github.io 를 가볍게 보여드리는 것으로 마무리 하겠습니다. 

- **Github** 페이지 공식 메뉴얼 : https://pages.github.com/

- [sindresorhus](https://github.com/sindresorhus) 의 [블로그](https://sindresorhus.com/) : https://github.com/sindresorhus/sindresorhus.github.com

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

여기에서 마음에 드는 레포지토리의 **Star** 버튼을 누르면서 관심있는 레포지토리들을 **Your stars** 페이지에 모아두세요. 이렇게 **Star** 버튼은 추천 뿐만 아니라 즐겨찾기 기능도 있는 것입니다.

## Stackoverflow Survey

매년 하는 [Stackoverflow Survey](https://insights.stackoverflow.com/survey/2019) 도 좋은 정보를 얻을 수 있는 소스가 됩니다. 하지만 이미 다뤘기 때문에 넘기겠습니다.

## 검색

### 영어 검색

영어로 검색해야 좋은 정보를 얻을 수 있습니다. 

> 이것은 너무 당연하지만 한동대학교에 처음 입학한 새내기도 GBC 를 수강하므로 다시 한 번 영어 검색을 강조하겠습니다.

이것은 너무 당연한데 한글로 검색하면 대한민국 인구가 5천만명에 불과한 반면 영어권 화자 인구는 약 [11억명](https://ko.wikipedia.org/wiki/%EC%98%81%EC%96%B4_%EC%82%AC%EC%9A%A9%EC%9E%90_%EC%88%98%EC%97%90_%EB%94%B0%EB%A5%B8_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D) 입니다. **Google** 은 [페이지 순위 매기기 알고리즘](https://en.wikipedia.org/wiki/PageRank) 으로 여러분이 검색하는 키워드로 필터링 된 웹 페이지 중에서 사람들이 가장 많이 방문할 것같은 페이지 순서대로 검색 결과를 나열합니다. 그러므로 영어로 검색하면 11억 명의 거대한 집단지성이 도출한 가장 가치있는 결론을 **Google** 이 맨 위로 올려서 보여줍니다. 

> 이제 질문을 바꿔보겠습니다. 만약 여러분이 한 회사의 사장이라면 5천만명 중에서 1등한 사람을 뽑겠습니까, 11억명 중에서 1등한 사람을 뽑겠습니까. 이 질문에 대한 대답은 객관적으로 당연히 11억명 중에서 1등한 사람을 뽑아야 합니다. 

> 또 다시 질문을 바꿔보겠습니다. 그러면 11억명 중에서 1등인 그 사람이 영어를 쓰는데 나는 영어를 못해서 말이 안통해서 같이 일을 못한다면 어쩔 수 없이 5천만명 중에서 1등한 사람과 일해야겠습니까, 아니면 영어를 어떻게든 극복한 다음에 11억명 중에서 1등한 사람과 일해야겠습니까. 사실 이건 개인의 가치관의 차이가 있기 때문에 객관적인 확답을 내리긴 어렵지만 저는 개인적으로 영어를 극복한 다음 11억명 중에서 1등한 사람과 일해야 한다고 생각합니다. 그러니까 제 개인적인 의견은 어떻게든 영어의 장벽을 극복하고 한글 검색 보다 영어로 검색하는 것이 좋은 것 같다는 의견입니다.

### 아니 그럼 어떻게 검색해야 하나?

**이것에 관한 건 순전히 경험적인 지식이므로 스스로 터득해야 합니다**만, 제가 경험한 바로는 다음과 같이 검색하는 것이 가장 효과적이었습니다. 

- **[플랫폼]** **[세부 플랫폼]** **[세부 사항]** 

  - 가령 **Python** 코딩 중 `numpy` 모듈의 `where` 함수가 궁금하다면 **python numpy where** 이라고 검색하는 것입니다.

- **[세부 플랫폼]** **[세부 사항]** in **[플랫폼]** 

  - 가령 **Python** 코딩 중 `numpy` 모듈의 `where` 함수가 궁금하다면 **numpy where in python** 이라고 검색하는 것입니다.

더 세부적으로는 다음과 같은 링크에 구글 고급 검색 명령어

https://www.spyfu.com/blog/google-search-operators/

https://support.google.com/websearch/answer/2466433?hl=en

등을 찾을 수 있는데 이것으로 검색하는 방법도 있습니다.

> 구글 검색 명령어가 얼마나 강력한지 검색만으로 개인을 해킹할 수 있다고 해서 [구글 해킹](https://ko.wikipedia.org/wiki/%EA%B5%AC%EA%B8%80_%ED%95%B4%ED%82%B9) 이라는 용어도 생겼습니다. 

### 아니 그럼 어떻게 검색해야 하나? (2)

또 **경험상** 비교할 때는 `플랫폼 대상 vs 대상` 으로 검색하는 것이 효과적이었습니다. 

> 경험적 지식이라는 사실을 계속 강조하는 것은 불확실한 지식이라는 것입니다.

- 가령 **Python** 코딩 중 기본 라이브러리인 `random.random` 와 외부 라이브러리의 `numpy.random` 의 비교가 필요하다면 **Python random.random vs numpy.random** 이라고 검색해보는 것입니다. 

### 원작자 찾기 

검색할 때는 항상 원작자를 찾아야 합니다. 여러분이 기독교인이라면 세상과 인간의 원작자인 하나님과 성경을 찾을 것입니다. 갤럭시를 쓰고 있는데 그것에 문제가 생겼다면 그것의 원작자인 삼성을 찾아가야 합니다. 하지만 코딩할 때 문제가 생겨서 검색할 때를 보면 꽤 많은 학생들이 원작자의 공식 문서를 먼저 찾기보다 2차 창작물, 즉 블로그나 문답사이트부터 찾는 것을 볼 수 있습니다. 

하지만 언제나 원작자의 공식 문서를 먼저 찾아보는 것이 순서입니다. 그것이 가장 정확하고 명료한 설명이기 때문입니다. 그런데 원작자의 글을 도무지 찾을 수 없거나 원작자의 글이 너무 어려워서 이해가 안되면 그 다음에나 2차 창작물, 즉 블로그나 문답사이트를 알아보아야 합니다. 

- 가령 **Python** 에서 `numpy` 를 사용하던 중 `where` 이라는 함수에 대한 이해가 필요해졌습니다. 그러면 **Google** 에 **python numpy where** 이라고 검색합니다. 그러면 **Google** 이 다음과 같이 [원작자의 글](https://numpy.org/doc/stable/reference/generated/numpy.where.html) 을 1등으로 추천해주는 것을 볼 수 있습니다. 

  ![firefox_hLynsSG3O4](https://user-images.githubusercontent.com/16812446/82721812-f0dd9800-9cfb-11ea-9600-fbaa2572c8ec.png)

> 근대 철학의 아버지 데카르트는 너무나도 명료하여 조금의 망설임도 없이 진리로 받아들일 수 있는 사실을 모든 지식의 토대, 즉 공리로 삼고자했습니다. 그것은 (1) "나는 생각한다. 고로 나는 존재한다." (2) "모든 현상은 원인을 갖는다." (3) "결과가 원인보다 거대할 수 없다." (4) "정신에는 완전성, 공간, 시간, 그리고 운동의 개념이 내재되어 있다." 입니다. 데카르트가 옳다면 두번째 공리 "모든 현상은 원인을 갖는다." 에 따라 어떠한 대상물이라도 그 원작자가 항상 존재합니다. 왜냐하면 그 대상물 또한 그것을 있게한 원인을 갖기 때문입니다. 그러므로 원작자가 존재하지 않을 수 없으니 검색할 때 언제나 원작자를 찾으려고 하는 것이 좋습니다. 

---

# 리눅스 교재

교재에서 다음 분량을 읽고 우분투 도커 컨테이너에서 실습해주세요. 사실 너무 열심히 읽지 않아도 됩니다. 즉, 막 외우려고 애쓰지 않아도 된다는 뜻입니다. 이런게 있구나 하면서 실습하면서 술술 넘기세요. 그리고 하다가 실습하기 힘든 부분이 있다면 그냥 너무 걱정하지 말고 넘겨도 됩니다. 

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
