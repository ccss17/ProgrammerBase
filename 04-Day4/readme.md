# Day 4 : [User](04-User/readme.md)

# (기존 GBC) Ch08 리눅스 부팅과 종료, Ch10 사용자 관리

# `slack`

# 유닉스 필로 소피 
  
# 코딩 컨벤션 (유닉스 필로소피)

  - suckless 스타일
  
  - googld 코딩 스타일 

    https://www.google.com/search?client=firefox-b-d&q=unix+philosophy

    https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html

    https://www.kernel.org/doc/Documentation/process/coding-style.rst

    https://man.openbsd.org/style

    https://www.google.com/search?client=firefox-b-d&q=google+coding+style

    https://github.com/google/styleguide/blob/gh-pages/pyguide.md

    그럼 처음으로 다뤄볼 주제는 코딩 컨벤션입니다. 코딩 컨벤션은, 프로그래밍 스타일에 대한 가이드라인입니다. 프로그래밍 스타일, 즉 코딩 스타일은 코드를 어떻게 작성할지에 관한 규칙입니다. 코딩 스타일은 코드의 기능에 실질적으로 영향을 주지는 않지만 코드의 가독성을 높혀주고 유지보수성을 높혀줍니다.

    대표적으로 indentation style, vertical alignment, spaces style, tabs style 등이 있습니다.

    indentation style 이란 코드의 블록과 컨트롤 플로우를 어떻게 쓸지 결정하죠.
    가령 간단한 if-else 문을 생각해 봅시다.
    코딩 스타일을 통일하지 않고 if-else 문을 사용한다면,
    어떤 함수에서는 이렇게 사용했다가 
        if ( hours < 24 && minutes < 60 && seconds < 60) { return true; } 
        else { return false; }
    어떤 함수에서는 이렇게 사용할 수도 있겠죠
        if ( hours < 24 && minutes < 60 && seconds < 60) {
            return true;
        } else { 
            return false; 
        }
    하지만 이렇게 코딩 스타일을 통일하지 않으면 프로젝트가 계속해서 커져갈 때마다 가독성이
    떨어집니다. 저렇게 if-else 문의 모양새가 다른 것들이 10개, 100개, 1000개가 된다면 말이죠.
        
    그래서 이런 스타일로 통일하거나,

        if (hours < 24 && minutes < 60 && seconds < 60) {
            return true;
        } else {
            return false;
        }

    이런 스타일로 통일해야 합니다.

        if (hours < 24 && minutes < 60 && seconds < 60)
        {
            return true;
        }
        else
        {
            return false;
        }

    그럼 대표적인 코딩 스타일들을 비교해볼까요?
    (참고 : https://github.com/motine/cppstylelineup)
