# 조금은 철학적인 이야기 - 튜링의 증명 

---

# Table of Contents

- [튜링의 증명](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%ED%8A%9C%EB%A7%81%EC%9D%98-%EC%A6%9D%EB%AA%85)

  - [배경](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%EB%B0%B0%EA%B2%BD)

  - [튜링의 논문 《On Computable Numbers, with an Application to the Entscheidungsproblem》](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%ED%8A%9C%EB%A7%81%EC%9D%98-%EB%85%BC%EB%AC%B8-on-computable-numbers-with-an-application-to-the-entscheidungsproblem)

  - [1. 튜링 기계](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#1-%ED%8A%9C%EB%A7%81-%EA%B8%B0%EA%B3%84)

  - [2. 보편만능기계](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#2-%EB%B3%B4%ED%8E%B8%EB%A7%8C%EB%8A%A5%EA%B8%B0%EA%B3%84)

    - [2-(1) 튜링기계를 텍스트로 사상시키기](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#2-1-%ED%8A%9C%EB%A7%81%EA%B8%B0%EA%B3%84%EB%A5%BC-%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%A1%9C-%EC%82%AC%EC%83%81%EC%8B%9C%ED%82%A4%EA%B8%B0)

    - [2-(2) 텍스트로 사상된 튜링기계를 입력받아 실행하는 작동규칙표](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#2-2-%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%A1%9C-%EC%82%AC%EC%83%81%EB%90%9C-%ED%8A%9C%EB%A7%81%EA%B8%B0%EA%B3%84%EB%A5%BC-%EC%9E%85%EB%A0%A5%EB%B0%9B%EC%95%84-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EC%9E%91%EB%8F%99%EA%B7%9C%EC%B9%99%ED%91%9C)

  - [3. 튜링의 증명](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#3-%ED%8A%9C%EB%A7%81%EC%9D%98-%EC%A6%9D%EB%AA%85)

    - [3-(1) 무한의 크기(대각선 논법)](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#3-1-%EB%AC%B4%ED%95%9C%EC%9D%98-%ED%81%AC%EA%B8%B0%EB%8C%80%EA%B0%81%EC%84%A0-%EB%85%BC%EB%B2%95)

      - [실수의 개수가 자연수의 개수보다 더 크다.](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%EC%8B%A4%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98%EA%B0%80-%EC%9E%90%EC%97%B0%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98%EB%B3%B4%EB%8B%A4-%EB%8D%94-%ED%81%AC%EB%8B%A4)

      - [자연수의 부분집합의 개수가 자연수의 개수보다 더 크다.](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%EC%9E%90%EC%97%B0%EC%88%98%EC%9D%98-%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9%EC%9D%98-%EA%B0%9C%EC%88%98%EA%B0%80-%EC%9E%90%EC%97%B0%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98%EB%B3%B4%EB%8B%A4-%EB%8D%94-%ED%81%AC%EB%8B%A4)

    - [3-(2) 튜링기계의 개수](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#3-2-%ED%8A%9C%EB%A7%81%EA%B8%B0%EA%B3%84%EC%9D%98-%EA%B0%9C%EC%88%98)

    - [3-(3) 보편만능기계로도 해결할 수 없는 정지문제](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#3-3-%EB%B3%B4%ED%8E%B8%EB%A7%8C%EB%8A%A5%EA%B8%B0%EA%B3%84%EB%A1%9C%EB%8F%84-%ED%95%B4%EA%B2%B0%ED%95%A0-%EC%88%98-%EC%97%86%EB%8A%94-%EC%A0%95%EC%A7%80%EB%AC%B8%EC%A0%9C)

  - [튜링의 증명의 의미](https://github.com/ccss17/ProgrammerBase/blob/master/turing.md#%ED%8A%9C%EB%A7%81%EC%9D%98-%EC%A6%9D%EB%AA%85%EC%9D%98-%EC%9D%98%EB%AF%B8)

---

# 튜링의 증명

> 참고 : [『컴퓨터과학이 여는 세계』, 이광근](https://book.naver.com/bookdb/book_detail.nhn?bid=9078133)

아래의 내용은 **위 서적을 기반으로 작성**되었습니다.

## 배경

1900년대 초 수학자들은 수학의 기초를 위하여 수학의 공리체계를 만들려고 했다는 것을 이미 언급했습니다. 그 중에서 힐베르트도 비유클리드 기하학, 유클리드 기하학, 해석학, 수론 등 모든 수학 체계의 정합성을 결정할 수 있는 규칙 체계를 만들려 했습니다. 힐베르트는 공리 체계가 다음 조건을 만족해야 한다고 말했습니다. 이것이 힐베르트의 프로그램입니다.

1. 정합성 : 어떤 명제가 증명되면 그 명제는 참이다. 그리고 그 명제의 부정문이 증명되서는 안된다.

2. 완전성 : 모든 명제는 참이나 거짓으로 증명되어야 한다.

3. 결정성 : 명제가 증명가능한지 확인하는 일반적인 과정이 존재해야 한다.

이것은 힐베르트가 적절한 공리와 추론규칙을 설정한 다음 그것의 형식적인 조작을 통하여 연역되는 정리들의 집합체(형식적 연역체계)로 수학을 구성한 것입니다. 즉, 힐베르트는 **유한한 공리와 몇가지 추론규칙을 통하여 수학의 모든 사실을 도출해내는 것을 자동으로 할 수 있도록** 만들고 싶었던 것입니다. 그래서 **이러한 자동기계를 만들기만 하면 근의 공식이나 도함수 구하는 공식같은 수학적 사실들이 모두 자동으로 만들어질 수 있을 것**이라고 생각했습니다. 이 생각들은 **수학적 사고를 순수한 기호 조작의 규칙으로 규명할 수 있다는 믿음**에 근거하고 있었습니다. 

하지만 이미 살펴보았듯이 괴델의 불완전성 정리로 인하여 자연수를 설명할 수 있을만큼 포괄적인 공리체계가 정합성(무모순성)을 가지면 그 체계는 반드시 불완전 체계라는 것이 밝혀졌습니다. 즉, **"자동적으로(기계적으로) 수학의 모든 사실들을 만들 수 없다."** 는 것을 증명했습니다. 이에 따라 힐베르트 프로그램의 첫번째, 두번째 규칙이 무의미해졌습니다. 

그런데 이때 앨런 튜링이 나타나 세번째 규칙 "결정성" 도 무의미하게 만들어버렸습니다. 튜링은 1935년 케임브리지 수학과를 졸업한 대학원생이었는데 이때 막스 뉴먼 교수가 개설한 괴델의 불완전성 정리 강의를 수강 중이었습니다. 뉴먼 교수는 힐베르트 프로그램 중 아직 부정되지 않은 세번째 조건을 소개했는데, 이때 튜링은 괴델의 증명에서 아이디어를 착안하여 불완전성 정리를 다시 증명할 수 있고 세번째 조건 "결정성" 또한 부정할 수 있겠다는 생각을 했습니다. 

몇 주 후, **튜링은 괴델이 증명한 "기계적인 방식(형식적인 방식)으로는 수학의 모든 사실을 만들어낼 수 없다." 를 독창적으로 다시 증명하고 세번째 조건 "결정성" 또한 부정하는 내용을 담은 논문 《On Computable Numbers, with an Application to the Entscheidungsproblem》(계산가능한 수에 대해서, 수리명제 자동생성 문제에 응용하면서) 를 런던 수리학회에 제출**했습니다.

## 튜링의 논문 《On Computable Numbers, with an Application to the Entscheidungsproblem》

튜링은 논문 《On Computable Numbers, with an Application to the Entscheidungsproblem》(계산가능한 수에 대해서, 수리명제 자동생성 문제에 응용하면서) 에서 먼저 매우 근본적인 것들을, 즉 "계산 가능한 것", "기계적인 것" 이 무엇인지 정의합니다.

- 계산 가능한 수 : **소수 부분을 유한한 자리까지 계산할 수 있는 실수**이다.

- 자동 기계 : **네모 칸으로 이루어진 테이프에 있는 기호를 읽어서 그 기호에 해당하는 "명령" 을 수행하는 기계**이다. 여기서 **"명령" 이란 본질적으로 "이것이면 저것을 하라"** 이다. "명령" 을 좀 더 구체적으로 말하면 **네모칸 이동, 네모칸 쓰기, 네모칸 읽기**에 불과하다.

튜링은 자신이 정의내린 정의내린 **"자동 기계" 의 범주에 상상할 수 있는 모든 자동 기계가 포함된다**고 충분히 설득합니다. 그리고 자신의 방식대로 정의한 자동 기계를 **튜링기계** 라고 부릅니다. 그리고 **튜링 기계를 텍스트로 사상시키는 방법**을 보이고 **텍스트로 사상된 기계를 읽어서 기계의 동작을 그대로 흉내내는 보편만능기계(컴퓨터)** 를 만들어서 보여줍니다. 그러므로 이 **보편만능기계는 기계적이고 자동적인 범주 내에 있는 모든 일을 수행할 수 있는 기계**입니다. 

이 보편만능기계를 사람들이 물리적으로 구현하여 오늘날의 컴퓨터가 된 것입니다. **기계를 텍스트로 표현(프로그램)하여 보편만능기계(컴퓨터)에 입력하면 보편만능기계가 텍스트로 사상된 기계의 동작을 그대로 흉내내** 줍니다. 그러니 사실 **여러분도 이미 수많은 튜링기계를 텍스트로 사상시켜 보았고(코딩) 그것을 보편만능기계(컴퓨터)에 입력시켜서 실행시켜보았던 것**입니다.

이 보편만능기계를 중심으로 튜링은 다음과 같은 논증으로 증명을 마무리했습니다.

1. **(튜링 기계의 정의)** 5 가지 부품을 정의한다. 이 5 가지 부품들로 만든 기계로 실행할 수 있는 것이 "기계적이 방식" 이다. 이 "기계적인 방식" 은 세상 모든 자동 기계를 포괄할 수 있을만큼 충분히 광범위하다.

2. **(보편만능기계의 정의)** 그런데 5 가지 부품으로 정의된 기계는 텍스트로 사상될 수 있다. 그리고 이 텍스트로 사상된 기계를 읽어서 그 기계의 동작을 그대로 흉내내는 보편만능기계를 만들 수 있다. 그러므로 이 시점에서 보편만능기계는 세상에 존재하는 모든 기계적인 동작과 자동화된 기능을 대표한다.

3. 그런데 **이 보편만능기계로도 해결할 수 없는 문제가 있으므로 기계적인 방식(형식적인 방식)으로는 수학의 모든 참인 명제를 이끌어내는 것은 불가능**하다.

## 1. 튜링 기계

튜링은 먼저 다음과 같은 5 가지 부품을 정의합니다.

![튜링기계](https://user-images.githubusercontent.com/16812446/83791074-2dce6500-a6d4-11ea-83e1-e7790ce8ba46.jpg)

1. **(1번 부품)** 무한히 많은 칸을 가진 테이프 (불변)

2. **(2번 부품)** 테이프에 기록되는 유한 개의 기호들 **(가변)**

3. **(3번 부품)** 테이프의 기호를 읽고 쓰는 입출력 장치 (불변)

4. **(4번 부품)** 입출력 장치의 상태를 나타내는 유한 개의 기호들 **(가변)**

5. **(5번 부품)** 기계의 작동 규칙표 **(가변)**

위 그림의 튜링기계가 테이프를 읽고 명령어를 실행하는 세 단계만 보이겠습니다.

- 현재 상태가 **A** 이고 테이프에서 읽은 기호가 **\*** 이므로 테이프에 **\*** 를 쓰고, 입출력 장치를 오른쪽 테이프로 한칸 옮기고, 다음 상태 **A** 가 된다.

- 현재 상태가 **A** 이고 읽은 기호가 **\$** 이므로 테이프에 **\$** 를 쓰고, 입출력 장치를 오른쪽 테이프로 한칸 옮기고, 다음 상태 **B** 가 된다. 

- 현재 상태가 **B** 이고 읽은 기호가 **\*** 이므로 테이프에 **\*** 를 쓰고, 입출력 장치를 왼쪽으로 한칸 옮기고, 다음 상태 **C** 가 된다.

튜링은 이 부품으로 구성된 기계로 0 과 1 을 반복해서 쓰는 기계, 사칙연산을 하는 기계 등 다양한 일을 할 수 있는 기계를 만들어 보여주었습니다. 그리고 **존재할 수 있는 모든 "자동 기계" 가 이렇게 만든 기계로 실행할 수 있는 것의 범주 내에 충분히 들어간다**고 설득합니다. 그리고 그는 **이 부품들로 만들어진 기계를 튜링 기계**라고 불렀습니다. 

## 2. 보편만능기계

그리고 튜링은 이 5 가지 부품들로 **어떤 특별한 튜링기계를 만들어서 보여주었는데, 그것이 바로 보편만능기계(universal machine)** 였습니다. 보편만능기계는 다음 두 가지 아이디어대로 설계됩니다.

1. **(2번/4번 부품 - 기호의 정의)** **모든 튜링기계를 일련의 기호로 표현할 수 있도록 보편만능기계의 기호를 정의**한다. 이로써 **모든 튜링기계가 보편만능기계의 기호를 기반으로 하는 텍스트로 사상될 수 있고**, 텍스트로 사상된 튜링기계는 보편만능기계의 테이프 입력으로 전달될 수 있다.

2. **(5번 부품 - 작동규칙표 정의)** 텍스트로 사상된 임의의 **튜링기계를 입력받아서 그 튜링기계의 동작을 그대로 따라할 수 있도록 보편만능기계의 작동규칙표를 정의**한다.

튜링이 이 튜링기계를 보편만능기계라고 부른 것은, **이 하나의 튜링기계로 존재하는 모든 튜링기계의 동작을 수행할 수 있었기 때문**이었습니다. 즉, 보편만능기계는 모든 기계적인 계산을 수행할 수 있는 기계인 것입니다.

이제 이 보편만능기계의 두 가지 아이디어가 실제로 어떻게 구현되는지 살펴보겠습니다.

### 2-(1) 튜링기계를 텍스트로 사상시키기

튜링은 보편만능기계의 유한 개의 기호를 정의하고, **모든 튜링기계를 보편만능기계의 기호로 테이프에 사상시키는 방법**을 보였습니다. **기호로 사상되어야 하는 튜링기계의 5 가지 부품**은 다음과 같습니다. 

1. 무한히 많은 칸을 가진 테이프 

2. 테이프에 기록되는 유한 개의 기호들

3. 테이프의 기호를 읽고 쓰는 입출력 장치 

4. 입출력 장치의 상태를 나타내는 유한 개의 기호들 

5. 기계의 작동 규칙표 

여기에서는 3 개의 테이프에 튜링기계의 5 가지 부품을 사상시켜보겠습니다.

- **테이프 1 : 1 번 부품과 3 번 부품**, 즉 테이프와 입출력 장치가 사상된다.

- **테이프 2 : 4 번 부품**, 즉 입출력 장치의 상태를 나타내는 기호가 사상된다.

- **테이프 3 : 5 번 부품**, 즉 작동규칙표가 사상된다.

**2 번 부품, 즉 유한 개의 상태 기호와 테이프 기호**는 무수히 많은 튜링기계마다 다양하겠지만, 그것들을 모두 각각 

<div align="center">

**S0, S1, S2, ...**

**T0, T1, T3, ...**
</div>

로 변환할 수 있기 때문에 이 **일반적인 기호를 사용하는 튜링기계 M 가 모든 튜링기계를 대표한다**고 하겠습니다.

#### 테이프 1 

**테이프 1 에는 튜링기계 M 의 테이프와 입출력 장치**가 사상됩니다. 사상되는 방법은 다음과 같습니다.

- 튜링기계 **M** 의 테이프의 하나의 네모칸에 2 개의 칸을 배정한다. 그러면 빈칸과 테이프 기호가 반복되어 나타난다. 

- **M** 의 입출력 장치가 현재 가르키고 있던 칸의 빈칸에만 위치기호 **\*** 를 표시한다.

이 방식대로하면 원래의 튜링기계 **M** 의 테이프가

<div align="center">

|**T0**|**T1**|**T3**|**...**|
|:---:|:---:|:---:|:---:|

</div>

였고, 입출력 장치가 **T0** 을 가르키고 있었다면 테이프 1 로 사상된 튜링기계는 

<div align="center">

|**\***|**T0**|□|**T1**|□|**T3**|**...**|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

가 됩니다. □ 는 비어있는 테이프 칸을 뜻합니다.

#### 테이프 2

**테이프 2 에는 튜링기계 **M** 의 현재상태기호(S0, S1, S2, ...)** 가 쓰여집니다. 그래서 튜링기계 **M** 의 현재상태가 **S0** 이었다면 테이프 2 는

<div align="center">

|S0|□|□|□|...|
|:---:|:---:|:---:|:---:|:---:|

</div>

가 됩니다. □ 는 비어있는 테이프 칸을 뜻합니다.

#### 테이프 3

**테이프 3 에는 5 번 부품, 즉 튜링기계 M 의 작동규칙표**가 사상됩니다. 튜링은 무수히 많은 튜링기계들이 무수히 많은 작동규칙표를 갖겠지만, 그 **모든 작동규칙표들을 유한한 기호로 표현할 수 있다**는 것을 보여주었습니다. 

여기에서는 고정된 기호 **S,T,>,<,||,0,1,2,3,4,5,6,7,8,9,X,\*** 를 사용하겠습니다. 이때 기호 **X** 는 각각의 규칙의 경계를 표시하는데 사용됩니다.

가령 튜링기계 **M** 의 작동규칙표가 

<div align="center">

|**S0**|**T0**|**T1**|**>**|**S1**|
|:---:|:---:|:---:|:---:|:---:|
|**S1**|**T2**|**T12**|**<**|**S0**|

</div>

와 같았다면, 규칙들을 **X** 로 구분하여 다음과 같은 텍스트로 사상시킬 수 있습니다.

<div align="center">

**XS0T0T1>S1XS1T2T12<S0X**
</div>

최종적으로 이 작동규칙표를 실제로 테이프 3 에 사상시키면 다음과 같습니다.

<div align="center">

|**X**|**S**|**0**|**T**|**0**|**T**|**1**|**>**|**S**|**1**|**T**|**2**|**T**|**1**|**2**|**<**|**S**|**0**|**X**|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

> 지금까지 설명의 간소화를 위하여 **T0** 같은 문자를 테이프 한 칸에 표시했는데, 실제로는 위와 같이 한 문자가 하나의 테이프 칸에 표시되어야 한다.

이 방식으로 **존재하는 모든 튜링기계의 작동규칙표를 고정된 기호 **S,T,>,<,||,0,1,2,3,4,5,6,7,8,9,X,\*** 를 기반으로 테이프 3 에 사상시킬 수 있습니다.**

### 2-(2) 텍스트로 사상된 튜링기계를 입력받아 실행하는 작동규칙표

이로써 **모든 튜링기계를 대표하는 튜링기계 **M** 가 성공적으로 테이프 1, 테이프 2, 테이프 3 에 사상**되었습니다. 이제 이 테이프를 입력받아서 원래의 튜링기계의 동작을 그대로 흉내내는 **보편만능기계의 작동규칙표를 설계**해보겠습니다. 그런데 이 작업은 생각보다 매우 쉬우며 다음과 같이 이루어집니다.

1. **테이프 2 에서 현재 상태 기호 ![](https://math.now.sh/?from=S_i) 를 읽는다.**

2. **테이프 1 에서 위치 기호(**\***) 를 찾아 그곳의 테이프 기호 ![](https://math.now.sh/?from=T_j) 를 읽는다.**

3. **현재 상태 기호 ![](https://math.now.sh/?from=S_i) 와 읽은 기호 ![](https://math.now.sh/?from=T_j) 에 해당하는 명령을 작동규칙표가 사상된 테이프 3 에서 찾아서 수행한다.**

이 작업을 반복하면 **테이프로 사상된 임의의 튜링기계를 입력받아서 그 동작을 그대로 똑같이 흉내낼 수 있습니다.**

> 그런데 튜링기계란 하나의 테이프를 갖고 있어야 하는데, 여기서 살펴본 방식대로라면 임의의 튜링기계가 3 개의 테이프로 사상되어 보편만능기계의 입력으로 들어옵니다. 이 문제를 해결하는 것은 매우 쉬우며 설명의 간소화를 위하여 미리 언급하지 않았습니다. 가령 한 가지 방법은 3 개의 테이프를 하나씩 번갈아가며 써서 하나의 테이프로 합치는 것입니다. 그래서 만약 테이프 1, 테이프 2, 테이프 3 이 각각 다음과 같았다면

<div align="center">

|![](https://math.now.sh/?from=U_1)|![](https://math.now.sh/?from=U_2)|![](https://math.now.sh/?from=U_3)|![](https://math.now.sh/?from=\dots)|
|:---:|:---:|:---:|:---:|
|![](https://math.now.sh/?from=V_1)|![](https://math.now.sh/?from=V_2)|![](https://math.now.sh/?from=V_3)|![](https://math.now.sh/?from=\dots)|
|![](https://math.now.sh/?from=W_1)|![](https://math.now.sh/?from=W_2)|![](https://math.now.sh/?from=W_3)|![](https://math.now.sh/?from=\dots)|

</div>

> 이렇게 하나의 테이프로 합칠 수 있습니다.

<div align="center">

|![](https://math.now.sh/?from=U_1)|![](https://math.now.sh/?from=V_1)|![](https://math.now.sh/?from=W_1)|![](https://math.now.sh/?from=U_2)|![](https://math.now.sh/?from=V_2)|![](https://math.now.sh/?from=W_2)|![](https://math.now.sh/?from=U_3)|![](https://math.now.sh/?from=V_3)|![](https://math.now.sh/?from=W_3)|![](https://math.now.sh/?from=\dots)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

> 그러면 각 테이프를 읽기 위하여 일정한 거리를 건너뛰어서 읽기만 하면 되는 것입니다.

그리고 이렇게 설계된 **보편만능기계가 컴퓨터의 본질이자 원시 모델인 것**입니다.

## 3. 튜링의 증명

이제 본격적인 튜링의 증명에 도달했습니다. 튜링의 증명을 이해하기 위해서는 먼저 무한의 크기를 이해해야 합니다.

### 3-(1) 무한의 크기(대각선 논법)

칸토어는 **실수의 개수가 자연수의 개수보다 훨씬 크다**는 것과 **자연수의 부분집합의 개수가 자연수의 개수보다 훨씬 더 크다**는 것을 증명했습니다. 칸토어는 **무한이 자연수만큼 있으면 셀 수 있을만큼 많다**고 표현했고 **무한이 실수만큼 있으면 셀 수 없을만큼 많다**고 표현했습니다.

> 아래의 칸토어의 증명을 대각선 논법이라고 하는데 이 증명이 너무 직관적이고 아름다워서 에르되시 팔은 이 증명이 "하나님이 갖고 있는 수학책에 있는 증명이다." 라고 말했습니다.

#### 실수의 개수가 자연수의 개수보다 더 크다.

실수의 개수가 자연수의 개수보다 훨씬 크다는 칸토어의 증명은 다음과 같습니다.

1. 먼저 실수집합 전체 대신 구간 ![](https://math.now.sh/?from=(0,1)) 을 상정하자. 그리고 자연수로 이 구간 ![](https://math.now.sh/?from=(0,1)) 에 존재하는 모든 실수에 다음과 같이 번호를 매길 수 있다고 하자. ![](https://math.now.sh/?from=R_i) 는 자연수 ![](https://math.now.sh/?from=i) 로 번호매겨진 실수를 뜻하고, ![](https://math.now.sh/?from=a_{ij}) 는 ![](https://math.now.sh/?from=0) 부터 ![](https://math.now.sh/?from=9) 사이의 자연수이다.

    ![](https://math.now.sh/?from=R_1=0.a_{11}a_{12}a_{13}a_{14}a_{15}\dots)

    ![](https://math.now.sh/?from=R_2=0.a_{21}a_{22}a_{23}a_{24}a_{25}\dots)

    ![](https://math.now.sh/?from=R_3=0.a_{31}a_{32}a_{33}a_{34}a_{35}\dots)

    ![](https://math.now.sh/?from=R_4=0.a_{41}a_{42}a_{43}a_{44}a_{45}\dots)

    ![](https://math.now.sh/?from=R_5=0.a_{51}a_{52}a_{53}a_{54}a_{55}\dots)

    ![](https://math.now.sh/?from=\vdots)

2. 이제 어떤 실수 ![](https://math.now.sh/?from=x=0.b_{1}b_{2}b_{3}b_{4}b_{5}\dots{}b_{i}\dots) 를 이렇게 만들어보자. 실수 ![](https://math.now.sh/?from=x) 의 소수 ![](https://math.now.sh/?from=i) 번째 자리수 ![](https://math.now.sh/?from=b_i) 를 위와 같은 실수에서 ![](https://math.now.sh/?from=a_{ii}) 가 ![](https://math.now.sh/?from=9) 보다 작은 자연수라면 ![](https://math.now.sh/?from=a_{ii}%2B1) 로 정하고, ![](https://math.now.sh/?from=9) 라면 ![](https://math.now.sh/?from=0) 으로 정하자.

3. 그렇다면 이 실수 ![](https://math.now.sh/?from=x) 는 자연수로 번호 매겨진 모든 실수 ![](https://math.now.sh/?from=R_i) 들과 ![](https://math.now.sh/?from=i) 번째 소수 자리수에서 반드시 다르다. 그러므로 이 실수 ![](https://math.now.sh/?from=x) 는 자연수로 번호 매겨진 모든 실수와 다르다.

4. 자연수로 모든 실수에 번호를 매겼다고 가정했지만, 그 이외의 실수 ![](https://math.now.sh/?from=x) 가 발견되었으므로 모든 자연수로 실수에 번호를 매길 수 없다. 

5. 그러므로 자연수의 개수보다 실수의 개수가 더 크다.

#### 자연수의 부분집합의 개수가 자연수의 개수보다 더 크다.

자연수의 개수보다 자연수의 부분집합의 개수가 훨씬 많다는 칸토어의 증명은 다음과 같습니다.

1. 만약 자연수의 부분집합이 자연수만큼 있다면 그 집합들 모두에 다음과 같이 자연수로 번호를 매길 수 있다.

    ![](https://math.now.sh/?from=N_1,N_2,N_3,\dots,N_i,\dots)

2. 그러면 자연수를 원소로 갖는 집합 ![](https://math.now.sh/?from=X) 를 이렇게 만들어보자. ![](https://math.now.sh/?from=N_1) 에 ![](https://math.now.sh/?from=1) 이 없다면 ![](https://math.now.sh/?from=X) 에 ![](https://math.now.sh/?from=1) 을 넣고, ![](https://math.now.sh/?from=N_2) 에 ![](https://math.now.sh/?from=2) 가 없다면 ![](https://math.now.sh/?from=X) 에 ![](https://math.now.sh/?from=2) 를 넣는다. 즉, 임의의 자연수 ![](https://math.now.sh/?from=i) 에 대하여 ![](https://math.now.sh/?from=N_i) 에 ![](https://math.now.sh/?from=i) 가 없다면 ![](https://math.now.sh/?from=X) 에 ![](https://math.now.sh/?from=i) 를 넣는다. 반면 ![](https://math.now.sh/?from=N_i) 에 ![](https://math.now.sh/?from=i) 가 있다면 ![](https://math.now.sh/?from=X) 에 ![](https://math.now.sh/?from=i) 를 넣지 않는다.

3. 그렇다면 ![](https://math.now.sh/?from=X) 는 자연수의 부분집합이지만 ![](https://math.now.sh/?from=N_1,N_2,N_3,\dots,N_i,\dots) 들과 다르다. 왜냐하면 임의의 자연수 ![](https://math.now.sh/?from=i) 에 대하여 ![](https://math.now.sh/?from=N_i) 에 ![](https://math.now.sh/?from=i) 가 없다면 ![](https://math.now.sh/?from=X) 에는 있고 ![](https://math.now.sh/?from=N_i) 에 ![](https://math.now.sh/?from=i) 가 있다면 ![](https://math.now.sh/?from=X) 에는 없기 때문이다. 그러므로 ![](https://math.now.sh/?from=X) 는 모든 ![](https://math.now.sh/?from=N_i) 들과 다르다.

4. 자연수의 부분집합 모두에 자연수로 번호를 매겼다고 가정했지만, 그 이외의 자연수의 부분집합 ![](https://math.now.sh/?from=X) 가 발견되었으므로 모든 자연수로 자연수의 부분집합에 번호를 매길 수 없다. 

5. 그러므로 자연수의 개수보다 자연수의 부분집합의 개수가 더 크다.

### 3-(2) 튜링기계의 개수

그렇다면 튜링기계의 개수는 셀 수 있을만큼(자연수만큼) 많을까요, 셀 수 없을만큼(실수만큼) 많을까요? 결론만 말하면 튜링기계의 개수는 셀 수 있을만큼(자연수만큼) 많습니다. 즉, 튜링기계의 개수는 자연수의 개수를 넘지 못합니다. 왜냐하면 튜링기계를 테이프로 사상시킬 수 있고, 그 테이프를 고유한 자연수로 사상시킬 수 있기 때문입니다.

우리는 튜링기계를 테이프로 사상시킬 때 유한한 기호 **S,T,>,<,||,0,1,2,3,4,5,6,7,8,9,X,\*** 를 사용했습니다. 그러므로 테이프를 자연수로 표현할 수 있는 한가지 방법은 다음과 같이 테이프를 17진수의 자연수로 사상시키는 것입니다.

<div align="center">

|0|1|![](https://math.now.sh/?from=\dots)|9|S|T|>|<|\|\||X|*|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|0|1|![](https://math.now.sh/?from=\dots)|9|10|11|12|13|14|15|16|

</div>

그러면 존재하는 모든 튜링기계를 고유의 자연수로 사상시킬 수 있습니다. 

- 가령 **XS1T2>\*** 와 같이 표현된 튜링기계가 있다고 하겠습니다. 그러면 이것을 17진수 자연수로 해석하여 고유의 자연수

  ![](https://math.now.sh/?from=15\times{}17^{6}%2B10\times{}17^{5}%2B1\times{}17^{4}%2B11\times{}17^{3}%2B2\times{}17^{2}%2B12\times{}17^{1}%2B16\times{}17^{0}=376400467)

  를 부여할 수 있습니다. 이렇게 존재하는 모든 튜링기계에 고유의 자연수를 부여할 수 있기 때문에 튜링기계의 개수는 자연수의 개수를 넘지 못합니다.

**이제 튜링의 증명을 이해할 모든 준비가 끝났습니다.**

### 3-(3) 보편만능기계로도 해결할 수 없는 정지문제

튜링의 증명의 목표는 모든 참인 명제를 기계적으로 만들 수 있는 튜링기계가 존재하지 않는다는 것을 보이는 것이었습니다. 튜링은 먼저 모든 참인 명제를 만들어낼 수 있는 튜링기계 ![](https://math.now.sh/?from=A) 가 존재한다고 가정하고 다음과 같은 논증을 펼쳤습니다.

1. 이 튜링기계 ![](https://math.now.sh/?from=A) 를 사용하여 어떤 튜링기계가 실행이 종료될지 종료되지 않고 실행이 영원히 계속될지 판단하는 튜링기계 ![](https://math.now.sh/?from=H) 를 만들 수 있다.

> ![](https://math.now.sh/?from=H) 는 정지문제(halting problem) 에서 따왔다.

2. 보편만능기계는 임의의 튜링기계를 입력받아 흉내낼 수 있으므로 튜링기계 ![](https://math.now.sh/?from=A) 를 입력시켜서 실행시키자.

3. 이때 어떤 튜링기계 ![](https://math.now.sh/?from=M) 을 보편만능기계 위에서 실행되고 있는 튜링기계 ![](https://math.now.sh/?from=A) 의 입력으로 넣자.

4. 그러면 ![](https://math.now.sh/?from=A) 는 모든 참인 명제를 만들어낸다고 가정했으므로 언젠가 "튜링기계 ![](https://math.now.sh/?from=M) 은 멈춘다." 또는 "튜링기계 ![](https://math.now.sh/?from=M) 은 멈추지 않는다." 라는 명제를 도출할 것이다.

5. 이것은 곧 튜링기계 ![](https://math.now.sh/?from=H) 의 기능이므로 우리는 **"튜링기계 ![](https://math.now.sh/?from=A) 가 존재한다면 튜링기계 ![](https://math.now.sh/?from=H) 도 존재한다."** 는 결론을 얻는다.

그런데 튜링기계 ![](https://math.now.sh/?from=H) 가 존재한다면 튜링기계의 개수가 자연수의 개수보다 많아집니다. 이에따라 튜링기계 ![](https://math.now.sh/?from=H) 는 존재할 수 없고 결국 튜링기계 ![](https://math.now.sh/?from=A) 도 존재해서는 안됩니다. 다음의 논증을 보겠습니다. 무한의 크기를 증명할 때 사용되었던 대각선 논법이 사용됩니다.

1. 튜링기계의 개수는 자연수의 개수보다 많지 않다는 것을 우리는 이미 알고 있다. 그러므로 모든 튜링기계에 자연수로 번호 ![](https://math.now.sh/?from=M_1,M_2,\dots,M_i,\dots) 를 붙힐 수 있다.

2. 그리고 어떤 튜링기계에 입력되는 테이프도 유한개의 기호로 이루어져있으므로 자연수로 사상될 수 있으며, 이에따라 입력 또한 자연수의 개수보다 많지 않다. 따라서 튜링기계에 입력될 수 있는 모든 입력에도 자연수로 번호 ![](https://math.now.sh/?from=I_1,I_2,I_3,\dots,I_i,\dots) 를 부여할 수 있다.

3. 그런데 ![](https://math.now.sh/?from=H) 가 존재한다면 모든 입력에 대한 모든 튜링기계를 ![](https://math.now.sh/?from=H) 에 입력시켜서 멈출지, 멈추지 않을지 판단한 결과를 다음과 같은 표로 만들 수 있다. ![](https://math.now.sh/?from=1) 이면 실행이 끝난다는 것이고, ![](https://math.now.sh/?from=0) 이면 끝나지 않는다는 것이다.

    ||![](https://math.now.sh/?from=I_{1})|![](https://math.now.sh/?from=I_{2})|![](https://math.now.sh/?from=I_{3})|![](https://math.now.sh/?from=\dots)|![](https://math.now.sh/?from=I_{i})|![](https://math.now.sh/?from=\dots)|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    |![](https://math.now.sh/?from=M_{1})|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=\dots)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=\dots)|
    |![](https://math.now.sh/?from=M_{2})|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=\dots)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=\dots)|
    |![](https://math.now.sh/?from=M_{3})|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=\dots)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=\dots)|
    |![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\ddots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|
    |![](https://math.now.sh/?from=M_{i})|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=1)|![](https://math.now.sh/?from=\dots)|![](https://math.now.sh/?from=0)|![](https://math.now.sh/?from=\dots)|
    |![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\vdots)|![](https://math.now.sh/?from=\ddots)|

    위 표에 따르면 튜링기계 ![](https://math.now.sh/?from=M_i) 에 입력 ![](https://math.now.sh/?from=I_i) 를 입력시켜서 실행한 결과가 ![](https://math.now.sh/?from=0) 인데 이것은 ![](https://math.now.sh/?from=H) 가 입력 ![](https://math.now.sh/?from=I_i) 를 받은 기계 ![](https://math.now.sh/?from=M_i) 의 실행이 끝나지 않는다고 판단한 것이다.

4. 그런데 이제 이렇게 튜링기계 ![](https://math.now.sh/?from=B) 를 만들어보자. ![](https://math.now.sh/?from=B) 는 위 표의 입력 ![](https://math.now.sh/?from=I_k) 와 기계 ![](https://math.now.sh/?from=M_k) 를 입력으로 받아서 ![](https://math.now.sh/?from=H) 의 결과가 ![](https://math.now.sh/?from=0) 이면 ![](https://math.now.sh/?from=1) 을 출력하고, ![](https://math.now.sh/?from=H) 의 결과가 ![](https://math.now.sh/?from=1) 이면 입력 ![](https://math.now.sh/?from=I_k) 를 ![](https://math.now.sh/?from=M_k) 에 넣고 실행한 결과에 ![](https://math.now.sh/?from=1) 을 더한 것을 출력한다. 

    - 그러므로 ![](https://math.now.sh/?from=A) 가 존재한다면 ![](https://math.now.sh/?from=H) 가 존재하고, ![](https://math.now.sh/?from=H) 가 존재한다면 ![](https://math.now.sh/?from=B) 가 존재한다는 결론(![](https://math.now.sh/?from=A\to{}H\to{}B))을 얻는다.

5. ![](https://math.now.sh/?from=B) 도 5 가지 부품으로 정의된 엄연한 튜링기계이다. 그럼에도 불구하고 ![](https://math.now.sh/?from=B) 는 위 표에 나타난 존재하는 모든 튜링기계와 다르다. 왜냐하면 ![](https://math.now.sh/?from=k) 번째 입력 ![](https://math.now.sh/?from=I_k) 에 대하여 ![](https://math.now.sh/?from=k) 번째 기계 ![](https://math.now.sh/?from=M_k) 와 다르게 작동하기 때문이다.

6. 존재하는 모든 튜링기계에 자연수로 번호 ![](https://math.now.sh/?from=M_1,M_2,\dots,M_i,\dots) 를 부여했는데도 그 이외의 튜링기계 ![](https://math.now.sh/?from=B) 가 발견되었다. 튜링기계의 개수는 자연수를 넘지 못하므로 이것은 모순이다.

7. 그러므로 튜링기계 ![](https://math.now.sh/?from=B) 는 존재해서는 안된다. 이에따라 ![](https://math.now.sh/?from=B) 를 있게한 튜링기계 ![](https://math.now.sh/?from=H) 도 존재하지 않는다. 또한 최종적으로 ![](https://math.now.sh/?from=H) 를 있게한 튜링기계 ![](https://math.now.sh/?from=A) 도 존재하지 않는다.

이로써 우리는 **모든 참인 명제를 만들어내는 튜링기계 ![](https://math.now.sh/?from=A) 는 존재할 수 없다**는 결론에 도달했습니다. **이로써 튜링의 증명이 완료되었습니다.**

## 튜링의 증명의 의미

튜링은 괴델이 불완전성 정리에서 상위 수학명제를 순수학 수학명제로 사상시키는 것에서 아이디어를 착안하여 임의의 튜링기계(상위 수학명제)를 순수한 테이프(수학명제)로 사상시켰고 그 테이프에 고유의 자연수(괴델수)를 부여할 수 있다는 것을 깨달은 것 같습니다. 이 관점에서 바라본다면 모든 튜링기계는 **PM** 속으로 사상될 수 있는 상위 수학명제이고, 테이프로 사상된 튜링기계(프로그램의 소스코드)는 **PM** 속의 형식문 모임(증명)과 같습니다. 

|괴델의 불완전성 정리|튜링의 증명|컴퓨터|
|:---:|:---:|:---:|
|상위 수학명제|튜링기계|하드웨어와 프로그램|
|수학명제|테이프로 사상된 튜링기계|
|괴델수|테이프에 부여된 고유의 자연수|
|힐베르트 프로그램|튜링기계 ![](https://math.now.sh/?from=A)|
|세번째 조건 결정성(명제가 증명가능한지 확인하는 알고리즘이 존재한다)|튜링기계 ![](https://math.now.sh/?from=H)|

튜링기계의 1 번 부품 테이프는 컴퓨터의 **RAM** 으로, 3 번 부품 테이프 입출력 장치는 **RAM** 입출력 장치로, 5 번 부품(보편만능기계) 의 작동규칙표는 컴퓨터의 **CPU** 로 구현되었습니다. 이것으로 우리는 컴퓨터가 튜링기계의 특수한 경우의 보편만능기계의 물리적 구현체이므로 컴퓨터는 튜링기계의 범주내에 속한다는 것을 알 수 있습니다. 컴퓨터가 모든 참인 명제를 만들어낼 수 없고, 세상에 존재하는 모든 문제를 자동적으로 해결할 수 없다는 것을 뜻합니다.

이로써 컴퓨터(하드웨어)란 튜링기계의 특수한 경우인 보편만능기계를 물리적으로 구현한 것이고, 컴퓨터에 입력되는 프로그램은 보편만능기계에 입력되는 모든 튜링기계라는 것을 알 수 있습니다. 보편만능기계를 비단 물리적으로 구현해야만 하는 것이 아니고 소프트웨어로 구현할 수도 있기 때문에 **Windows** 시스템에서 **Ubuntu Linux** 같은 가상머신을 설치하여 또 다른 보편만능기계를 실행시킬 수 있는 것입니다.

하지만 튜링기계를 능가하는 기계가 존재하는가에 대한 의문은 아직 풀리지 않았습니다. 지금의 컴퓨터는 튜링의 정의일 뿐입니다. 따라서 튜링 기계를 능가하는 컴퓨터의 탄생은 아직 오지 않았을지도 모릅니다.