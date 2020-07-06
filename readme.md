# Programmer Base

컴퓨터 공학자에게 기반 지식이 되는 **수학의 역사**, **괴델의 불완전성 정리**, **튜링기계**, **기술적 특이점** 등과 프로그래머에게 유용한 툴(**VSCode**, **vim**, **tmux**, **zsh** 등)과 그것의 생산성을 최대화할 수 있는 여러가지 팁들을 5일 동안 가이드해주는 레포지토리입니다.

## inspired by

이 프로젝트는 **MIT** 의 **[Missing Semetser](https://missing.csail.mit.edu/)** 에서 영감을 받아서 만들어졌습니다. **Missing Semeter** 의 서문은 다음과 같이 프로그래머들이 컴퓨터 공학적 지식을 배우는데에는 많은 배움을 얻을 수 있지만, 정작 그들이 수많은 시간을 쏟게 되는 툴과 툴을 효율적으로 사용할 수 있는 방법에 대한 적절한 리드를 받을 수 없었던 상황을 지적합니다. 

> Classes teach you all about advanced topics within CS, from operating systems to machine learning, but **there’s one critical subject that’s rarely covered, and is instead left to students to figure out on their own: proficiency with their tools.** We’ll teach you how to master the command-line, use a powerful text editor, use fancy features of version control systems, and much more!

> Students spend hundreds of hours using these tools over the course of their education (and thousands over their career), so **it makes sense to make the experience as fluid and frictionless as possible.** Mastering these tools not only enables you to spend less time on figuring out how to bend your tools to your will, but it also lets you solve problems that would previously seem impossibly complex.

이 레포지토리는 이러한 아이디어에서 착안하여 제가 주관적으로 선정한 프로그래밍을 할 때 필요한 여러가지 툴들과 **Linux** 에 관련된 내용과 컴퓨터에 대한 약간 철학적인 이야기에 대한 내용을 담고 있습니다.

## Notice 

- 모든 내용은 출처를 명시하였습니다. 잘못된 내용에 대한 지적과 풀 리퀘스트는 항상 환영합니다. 

- 본 내용들은 누구나 자유롭게 무료로 학습할 수 있습니다.

- 본문에서 말하는 "교재" 란 

  <div align="center">
  
  [<img src="https://bookthumb-phinf.pstatic.net/cover/077/993/07799304.jpg" width="20%" height="auto">](https://book.naver.com/bookdb/book_detail.nhn?bid=7799304)

  </div>

  를 뜻합니다. 

## 읽는 법

- **N 번째** 날에는 **Day N** 을 **정독** 하면 됩니다. 

- 다음의 표시가 있는 코드 부분은 실제로 직접 실행해보면 실습하면 됩니다. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ (execute-me)
  ```

- 명시적으로 "**실습 하지 않아도 된다**" 는 식의 언급이 없다면 모든 내용을 실습해야만 합니다. 

- 명시적으로 "**실습 하지 않아도 된다**" 는 식의 언급이 있다면 실습하지 않아도 되나 꼭 정독은 해야합니다. 

## 읽지 않는 법 

- 맥락에서 약간 벗어나지만 나름대로 필요한 내용은 

  > (맥락에서 약간 벗어나지만 나름대로 필요한 내용)

  으로 표시했습니다. 이 부분은 시간절약을 위해 아예 안봐도 됩니다.

- 몇몇 파트에서 **요약**을 하면 편리하겠다 싶은 부분을 요약정리를 했는데

  자신에게 필요없다 싶으면 시간절약을 위하여  넘겨도 됩니다.

- 만약

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  가 없는 코드 부분은 굳이 실행하지 않아도 되고 실행해도 됩니다. 시간 절약을 위하여 넘겨도 됩니다. 

# Contents

## [Day 1](01-Day1/)

- Docker

- 리눅스 교재

- 조금은 철학적인 이야기 : [조금은 철학적인 이야기](https://github.com/ccss17/ProgrammerBase/blob/master/math.md#%EC%A1%B0%EA%B8%88%EC%9D%80-%EC%B2%A0%ED%95%99%EC%A0%81%EC%9D%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0) ~ [예시 : 기초 명제 논리학](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EC%98%88%EC%8B%9C--%EA%B8%B0%EC%B4%88-%EB%AA%85%EC%A0%9C-%EB%85%BC%EB%A6%AC%ED%95%99)

## [Day 2](02-Day2/)

- 리눅스 교재

- Stackoverflow Survey

- Git

- Github

- VSCode

- Markdown

- 조금은 철학적인 이야기 : [다시 점검해보고 넘어가기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%8B%A4%EC%8B%9C-%EC%A0%90%EA%B2%80%ED%95%B4%EB%B3%B4%EA%B3%A0-%EB%84%98%EC%96%B4%EA%B0%80%EA%B8%B0) ~ [3. 핵심 논증](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-%ED%95%B5%EC%8B%AC-%EB%85%BC%EC%A6%9D)

## [Day 3](03-Day3/)

- 리눅스 교재

- vim

- tmux

- 조금은 철학적인 이야기 : [3-(1) 자기 자신이 증명될 수 없다고 주장하는 형식문](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-1-%EC%9E%90%EA%B8%B0-%EC%9E%90%EC%8B%A0%EC%9D%B4-%EC%A6%9D%EB%AA%85%EB%90%A0-%EC%88%98-%EC%97%86%EB%8B%A4%EA%B3%A0-%EC%A3%BC%EC%9E%A5%ED%95%98%EB%8A%94-%ED%98%95%EC%8B%9D%EB%AC%B8-) ~ [불완전성 정리의 의미](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC%EC%9D%98-%EC%9D%98%EB%AF%B8)

## [Day 4](04-Day4/)

- CLI

- 더 빨라진 git

- `bash` ➜ `zsh` - 더 빨라진 쉘

- 더 빨라진 tmux

- 더 빨라진 vim

- VSCode 업그레이드

- VSCode Vim

- VSCode 디버깅

- 조금은 철학적인 이야기 : [튜링의 증명](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%ED%8A%9C%EB%A7%81%EC%9D%98-%EC%A6%9D%EB%AA%85)

## [Day 5](05-Day5/)

- Git 과 Github 못다한 이야기

- 좋은 정보 얻기

- 리눅스 교재

- Funny CLI

- 조금은 철학적인 이야기 : [기술적 특이점](https://github.com/ccss17/ProgrammerBase/blob/master/future.md)

## Content List

위에서 **Day1** 부터 **Day5** 까지 컨텐츠들을 5일 동안 학습할 수 있도록 순서를 적절히 배치해놓았는데, 해당 내용의 일관된 내용을 살펴보고 싶으시다면 다음의 리스트를 보시면 됩니다.

- **[Docker](docker.md)**

- **[Information](information.md)**

- **[Git](git.md)**

- **[VSCode](vscode.md)**

- **[Markdown](markdown.md)**

- **[Tmux](tmux.md)**

- **[Vim](vim.md)**

- **[CLI](cli.md)**

## 조금은 철학적인 이야기

### [수학의 역사](https://github.com/ccss17/ProgrammerBase/blob/master/math.md)

- [조금은 철학적인 이야기 ](https://github.com/ccss17/ProgrammerBase/blob/master/math.md#%EC%A1%B0%EA%B8%88%EC%9D%80-%EC%B2%A0%ED%95%99%EC%A0%81%EC%9D%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0)

- [수학의 역사 ](https://github.com/ccss17/ProgrammerBase/blob/master/math.md#%EC%88%98%ED%95%99%EC%9D%98-%EC%97%AD%EC%82%AC)

### [괴델의 불완전성 정리](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md)

- [컴퓨터의 역사 ](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EC%BB%B4%ED%93%A8%ED%84%B0%EC%9D%98-%EC%97%AD%EC%82%AC)

- [괴델의 불완전성 정리 ](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EA%B4%B4%EB%8D%B8%EC%9D%98-%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC)

### [튜링의 증명](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md)

- [튜링의 증명](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%ED%8A%9C%EB%A7%81%EC%9D%98-%EC%A6%9D%EB%AA%85)

### [기술적 특이점](https://github.com/ccss17/ProgrammerBase/blob/master/future.md)

- [미래 ](https://github.com/ccss17/ProgrammerBase/blob/master/future.md#%EB%AF%B8%EB%9E%98)

- [Why the future doesn't need us](https://github.com/ccss17/ProgrammerBase/blob/master/future.md#why-the-future-doesnt-need-us)

- [기술적 특이점의 의미](https://github.com/ccss17/ProgrammerBase/blob/master/future.md#%EA%B8%B0%EC%88%A0%EC%A0%81-%ED%8A%B9%EC%9D%B4%EC%A0%90%EC%9D%98-%EC%9D%98%EB%AF%B8)

- [ProgrammerBase 를 마치며](https://github.com/ccss17/ProgrammerBase/blob/master/future.md#programmerbase-%EB%A5%BC-%EB%A7%88%EC%B9%98%EB%A9%B0)

# Rule

GBC 참여자들은 **PASS** 와 **FAIL** 에 관련된 내용이니 [rule.md](rule.md) 를 꼭 확인해주세요. 