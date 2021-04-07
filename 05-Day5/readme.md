
# This reposity has been abandoned. Please see https://ccss17.github.io/ProgrammerBase

# 이 레포지토리는 더 이상 관리되지 않습니다. https://ccss17.github.io/ProgrammerBase 에 방문해주세요.

# Day 5 

GBC 첫번째 과정 **Programmer Base** 의 5일차 내용입니다.

> (gdb, pwddbg, gdb-gef)

---

**다음 내용을 학습하세요.**

# Git 과 Github 못다한 이야기

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

# 좋은 정보 얻기

- [좋은 정보 얻기](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EC%A2%8B%EC%9D%80-%EC%A0%95%EB%B3%B4-%EC%96%BB%EA%B8%B0)

  - [Awesome Repository](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#awesome-repository)

  - [Hacker News](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#hacker-news)

  - [Reddit ](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#reddit)

  - [Github trending](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#github-trending)

  - [Stackoverflow Survey](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#stackoverflow-survey-1)

  - [Dev Community](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#dev-community)

  - [검색](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EA%B2%80%EC%83%89)

    - [영어 검색](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EC%98%81%EC%96%B4-%EA%B2%80%EC%83%89)

    - [아니 그럼 어떻게 검색해야 하나?](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EC%95%84%EB%8B%88-%EA%B7%B8%EB%9F%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B2%80%EC%83%89%ED%95%B4%EC%95%BC-%ED%95%98%EB%82%98)

    - [원작자 찾기 ](https://github.com/ccss17/ProgrammerBase/blob/master/information.md#%EC%9B%90%EC%9E%91%EC%9E%90-%EC%B0%BE%EA%B8%B0)

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

이 부분은 옵션입니다. 관심 있으신 분들만 학습하면 됩니다.

- [Funny CLI ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#funny-cli)
