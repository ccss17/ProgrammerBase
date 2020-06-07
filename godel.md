# 조금은 철학적인 이야기 - 괴델의 불완전성 정리

---

# Table of Contents

- [컴퓨터의 역사 ](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EC%BB%B4%ED%93%A8%ED%84%B0%EC%9D%98-%EC%97%AD%EC%82%AC)

  - [배경과 용어](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%B0%B0%EA%B2%BD%EA%B3%BC-%EC%9A%A9%EC%96%B4)

    - [예시 : 기초 명제 논리학](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EC%98%88%EC%8B%9C--%EA%B8%B0%EC%B4%88-%EB%AA%85%EC%A0%9C-%EB%85%BC%EB%A6%AC%ED%95%99)

  - [다시 점검해보고 넘어가기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%8B%A4%EC%8B%9C-%EC%A0%90%EA%B2%80%ED%95%B4%EB%B3%B4%EA%B3%A0-%EB%84%98%EC%96%B4%EA%B0%80%EA%B8%B0)

- [괴델의 불완전성 정리 ](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EA%B4%B4%EB%8D%B8%EC%9D%98-%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC)

  - [괴델의 논문 《Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I》](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EA%B4%B4%EB%8D%B8%EC%9D%98-%EB%85%BC%EB%AC%B8-%C3%BCber-formal-unentscheidbare-s%C3%A4tze-der-principia-mathematica-und-verwandter-systeme-i)

  - [1. 괴델 수 붙이기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#1-%EA%B4%B4%EB%8D%B8-%EC%88%98-%EB%B6%99%EC%9D%B4%EA%B8%B0)

    - [1-(1) 기본 기호에 괴델수 붙이기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#1-1-%EA%B8%B0%EB%B3%B8-%EA%B8%B0%ED%98%B8%EC%97%90-%EA%B4%B4%EB%8D%B8%EC%88%98-%EB%B6%99%EC%9D%B4%EA%B8%B0)

    - [1-(2) 형식문에 괴델수 붙이기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#1-2-%ED%98%95%EC%8B%9D%EB%AC%B8%EC%97%90-%EA%B4%B4%EB%8D%B8%EC%88%98-%EB%B6%99%EC%9D%B4%EA%B8%B0)

    - [1-(3) 증명에 괴델수 붙이기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#1-3-%EC%A6%9D%EB%AA%85%EC%97%90-%EA%B4%B4%EB%8D%B8%EC%88%98-%EB%B6%99%EC%9D%B4%EA%B8%B0)

  - [2. 상위 수학명제를 수학 명제로 사상시키기](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#2-%EC%83%81%EC%9C%84-%EC%88%98%ED%95%99%EB%AA%85%EC%A0%9C%EB%A5%BC-%EC%88%98%ED%95%99-%EB%AA%85%EC%A0%9C%EB%A1%9C-%EC%82%AC%EC%83%81%EC%8B%9C%ED%82%A4%EA%B8%B0)

    - [증명함수](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EC%A6%9D%EB%AA%85%ED%95%A8%EC%88%98)

    - [대입함수](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%8C%80%EC%9E%85%ED%95%A8%EC%88%98)

  - [3. 핵심 논증](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-%ED%95%B5%EC%8B%AC-%EB%85%BC%EC%A6%9D)

    - [3-(1) 자기 자신이 증명될 수 없다고 주장하는 형식문 ![](https://math.now.sh/?from=G)](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-1-%EC%9E%90%EA%B8%B0-%EC%9E%90%EC%8B%A0%EC%9D%B4-%EC%A6%9D%EB%AA%85%EB%90%A0-%EC%88%98-%EC%97%86%EB%8B%A4%EA%B3%A0-%EC%A3%BC%EC%9E%A5%ED%95%98%EB%8A%94-%ED%98%95%EC%8B%9D%EB%AC%B8-)

    - [3-(2) **PM** 이 정합적 체계라면 형식문 ![](https://math.now.sh/?from=G) 는 **PM** 에 의하여 증명될 수 없다.](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-2-pm-%EC%9D%B4-%EC%A0%95%ED%95%A9%EC%A0%81-%EC%B2%B4%EA%B3%84%EB%9D%BC%EB%A9%B4-%ED%98%95%EC%8B%9D%EB%AC%B8--%EB%8A%94-pm-%EC%97%90-%EC%9D%98%ED%95%98%EC%97%AC-%EC%A6%9D%EB%AA%85%EB%90%A0-%EC%88%98-%EC%97%86%EB%8B%A4)

    - [3-(3) 형식문 ![](https://math.now.sh/?from=G) 는 증명될 수 없지만 참이다.](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-3-%ED%98%95%EC%8B%9D%EB%AC%B8--%EB%8A%94-%EC%A6%9D%EB%AA%85%EB%90%A0-%EC%88%98-%EC%97%86%EC%A7%80%EB%A7%8C-%EC%B0%B8%EC%9D%B4%EB%8B%A4)

    - [3-(4) 그러므로 **PM** 이 정합적 체계라면 **PM** 은 불완전체계이다. (제 1 불완전성 정리)](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-4-%EA%B7%B8%EB%9F%AC%EB%AF%80%EB%A1%9C-pm-%EC%9D%B4-%EC%A0%95%ED%95%A9%EC%A0%81-%EC%B2%B4%EA%B3%84%EB%9D%BC%EB%A9%B4-pm-%EC%9D%80-%EB%B6%88%EC%99%84%EC%A0%84%EC%B2%B4%EA%B3%84%EC%9D%B4%EB%8B%A4-%EC%A0%9C-1-%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC)

    - [3-(5) "**PM** 은 정합적 체계이다." 라는 주장은 **PM** 의 체계로는 증명할 수 없다. (제 2 불완전성 정리)](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#3-5-pm-%EC%9D%80-%EC%A0%95%ED%95%A9%EC%A0%81-%EC%B2%B4%EA%B3%84%EC%9D%B4%EB%8B%A4-%EB%9D%BC%EB%8A%94-%EC%A3%BC%EC%9E%A5%EC%9D%80-pm-%EC%9D%98-%EC%B2%B4%EA%B3%84%EB%A1%9C%EB%8A%94-%EC%A6%9D%EB%AA%85%ED%95%A0-%EC%88%98-%EC%97%86%EB%8B%A4-%EC%A0%9C-2-%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC)

  - [불완전성 정리의 의미 ](https://github.com/ccss17/ProgrammerBase/blob/master/godel.md#%EB%B6%88%EC%99%84%EC%A0%84%EC%84%B1-%EC%A0%95%EB%A6%AC%EC%9D%98-%EC%9D%98%EB%AF%B8)

---

# 컴퓨터의 역사 

이제 수학의 역사는 충분히 알아보았으니 본격적으로 컴퓨터의 역사를 알아보겠습니다. 지금까지 한 일은 단지 컴퓨터의 본질을 이해하기 위한 사전작업에 불과했습니다. 지금까지는 드라마(컴퓨터)의 예고편(수학)을 본 것에 불과 합니다. 

앞으로 괴델의 불완전성 정리를 알아볼 것인데, 불완전성 정리에 대한 이해는 컴퓨터의 본질을 이해할 수 있는 좋은 단서가 됩니다. 하지만 장담하건데 생각보다 막 어렵다거나 재미없다거나 하지 않아요. 정말 쉽고 재밌으니까 편하게 보셨으면 좋겠습니다.

## 배경과 용어

그에 앞서 배경과 용어를 다시 점검하고 넘어가겠습니다. 

힐베르트는 수학자들이 수학을 발전시켜온 과정을 보니까 수학이란 공리에 몇 개의 추론 규칙을 반복적으로 적용하는 것이 전부 다 인 것 같다는 생각을 했습니다. 그리고 그러한 추론 규칙만 찾아낸다면 수학자가 더 이상 고생할 필요가 없어질 것이라고 생각했다. 

20세기 초 수학계는 수학에서 자연 언어를 제거하고 수학을 완전히 형식적인 연역 체계로 구성하려고 노력했습니다. 수학적 사고를 순수한 기호 조작의 규칙에 의해 포착할 수 있다고 믿었기 때문입니다. 이 노력은 러셀과 화이트헤드의 『수학 원리』로 절정을 이루었습니다. 다음은 러셀이 수학을 완전한 형식적인 연역 체계로 구성한 『수학원리』에서 1+1=2 의 증명을 보인 것입니다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Principia_Mathematica_54-43.png/500px-Principia_Mathematica_54-43.png)

> 『수학 원리』 에서 1+1=2 증명

이제 앞으로 사용할 용어들을 다음과 같이 정리해보겠습니다.

- **기본 기호 : 연역 체계에서 사용할 유한 개의 기호들**

- **형식문 : 기본 기호가 조합되어 만들어지는 명제**

- **구성규칙 : 기본 기호가 조합되어 형식문을 이루는 방식**

- **추론규칙 : 어떤 형식문으로부터 다른 형식문에 연역되는 방식**

- **공리(원초 형식문) : 어떤 형식문으로부터도 연역되지 않았지만 올바르다고 받아들인 형식문**

- **정리 : 공리로부터 추론규칙에 의하여 연역된 형식문**

- **증명 : 공리로부터 정리를 연역하는 과정**

- **정합성(무모순성) : 연역 체계가 모순되는 형식문을 연역하지 않는다는 성질**

  - 참이면서 동시에 거짓인 형식문을 연역하지 않는다는 매우 중요한 성질입니다. 이 성질이 어찌나 중요한지 칸토어는 수학은 매우 자유롭고 창조적이나 오로지 무모순성이라는 성질에만 제약된다고 말했습니다. 또 모든 수학 기초론의 목표가 수학 체계의 정합성을 확립하는 것입니다. 

- **완전성 : 연역 체계의 모든 형식문이 공리로부터 연역될 수 있다는 성질**

- **정합적 체계 : 모순 되는 형식문을 도출하지 않는, 즉 형식문과 그 부정문을 도출하지 않는 체계**

- **부정합 체계 : 모순을 도출하는, 즉 형식문과 그 부정문을 도출하는 체계**

- **완전 체계 : 모든 형식문을 공리로부터 연역(증명)할 수 있는 체계**

- **불완전 체계 : 하나 이상의 형식문을 공리로부터 연역(증명)할 수 없는 체계**

### 예시 : 기초 명제 논리학

하지만 아직 용어의 의미가 알쏭달쏭 한 것 같습니다. 그래서 『수학 원리』의 작은 한 부분을 차지하는 **"기초 명제 논리학"** 이라는 **형식적 연역 체계** 를 예를 들어서 용어에 대한 이해를 해보겠습니다. 

> 이산수학을 수강하신 분들은 익숙할 것 같습니다. 

다음의 과정으로 **"기초 명제 논리학"** 은 완전히 **형식화** 된 **형식적 연역 체계**가 됩니다.

1. 연역 체계에서 사용할 **기본 기호**의 채택하기 : 기초 명제 논리학의 기본 기호는 **변항 기호(문장 변항)** 와 **상항 기호**로 구성됩니다.

    - **변항 기호(문장 변항)** 는 형식문이 대입될 수 있는 변항으로써 알파벳 소문자 ![](https://math.now.sh/?from=p,q,r) 등으로 나타냅니다.

    - **상항 기호**는 "아닌" 을 나타내는 ![](https://math.now.sh/?from=\sim) , "또는" 을 나타내는 ![](https://math.now.sh/?from=\lor) , "그리고" 를 나타내는 ![](https://math.now.sh/?from=\land) , "만일 ~이면 ~이다" 를 나타내는 ![](https://math.now.sh/?from=\to) 으로 구성됩니다. 

2. 기본 기호들의 어떤 조합으로 형식문이 인정되는지 정하는 **구성 규칙** 만들기 : 기초 명제 논리학의 구성 규칙은 다음 두 가지입니다. 

    - **개개의 문장 변항**을 형식문으로 간주합니다.
    
    - ![](https://math.now.sh/?from=S_1,S_2) 가 형식문이면 **상항기호로 조합되는 ![](https://math.now.sh/?from=\sim{S_1},S_{1}\lor{S_{2}},S_1\to{S_2},S_1\land{S_2}) 도 형식문**입니다.

3. 어떤 형식문으로부터 다른 형식문이 연역되는지 정하는 **변형 규칙** 만들기 : 기초 명제 논리학의 변형 규칙은 **대입규칙**과 **분리규칙**으로 구성됩니다.

    - **대입규칙**은 문장 변항을 포함하고 있는 형식문에 어떤 형식문이라도 대입하여 연역할 수 있다는 연역 규칙입니다.

    - **분리규칙**은 ![](https://math.now.sh/?from=p,p\to{q}) 가 참이라면 ![](https://math.now.sh/?from=q) 를 연역할 수 있다는 규칙입니다. 

4. 어떤 형식문을 **공리**, 즉 원초 형식문으로 채택하기 : 기초 명제 논리학은 다음 네 가지 자명한 형식문을 증명없이 받아들입니다. 

    - ![](https://math.now.sh/?from=(p\lor{}p)\to{}p) 
    
      - p 이거나 p 이면 p 이다.

    - ![](https://math.now.sh/?from=p\to(p\lor{}q)) 
    
      - p 이면 p 이거나 q 이다.

    - ![](https://math.now.sh/?from=(p\lor{}q)\to(q\lor{}p)) 
    
      - p 이거나 q 이면 q 이거나 p 이다.

    - ![](https://math.now.sh/?from=(p\to{}q)\to((r\lor{}p)\to(r\lor{}q))) 
    
      - "p 이면 q 이다." 이면 "(r 또는 p) 이면 (r 또는 q) 이다." 이다.

이로써 **"기초 명제 논리학"** 은 무한히 많은 형식문들을 연역해낼 수 있습니다. 가령 너무나도 자명해보이는 추론 규칙과 공리로부터 전혀 자명하지 않은 형식문 

<div align="center">
<img src="https://math.now.sh/?from=((p\to{}q)\to((r\to{}s)\to{}t))\to((u\to((r\to{}s)\to{}t))\to((p\to{}u)\to(s\to{}t)))" width="70%" height="auto">
</div>

을 연역해낼 수 있습니다. 

이제 **이 연역체계가 정합적 체계인지 모순을 도출하는 체계인지**, 그리고 **완전체계인지 불완전체계인지** 살펴보겠습니다. 

1. 위 네 가지 공리로부터 정리 ![](https://math.now.sh/?from=p\to{}(\sim{}p\to{}q)) 를 연역할 수 있다. 

2. 이 공리 체계에 정합성이 없다고, 즉 모순을 도출한다고 가정하면 이 공리 체계로부터 형식문 ![](https://math.now.sh/?from=S) 와 ![](https://math.now.sh/?from=\sim{}S) 가 동시에 연역된다.

3. 그렇다면 형식문 ![](https://math.now.sh/?from=p\to{}(\sim{}p\to{}q)) 의 변항 ![](https://math.now.sh/?from=p) 에 ![](https://math.now.sh/?from=S) 를 대입하여 ![](https://math.now.sh/?from=S\to{}(\sim{}S\to{}q)) 를 연역(**대입규칙**)할 수 있다. 

4. 이때 ![](https://math.now.sh/?from=S) 가 증명될 수 있으므로 **분리규칙에 의하여** ![](https://math.now.sh/?from=\sim{}S\to{}q) 가 연역된다. 

5. 그런데 ![](https://math.now.sh/?from=\sim{}S) 도 증명될 수 있으므로 최종적으로 문장변항 ![](https://math.now.sh/?from=q) 가 연역(증명)된다. 

6. 이 변항에는 존재하는 모든 형식문이 대입될 수 있으므로 존재하는 모든 형식문이 증명가능한 정리가 된다. 심지어 공리도 정리가 된다.

7. 이것은 **부정합 체계에서는 모든 형식문이 증명 가능하다**는 것이다.

8. 그러므로 **공리 체계의 정합성의 증명은 공리로부터 연역되지 않는 형식문이 있다는 것을 보이는 것**이다.

이렇게 정합성이 없는 체계에서는 "나는 한동대생이다." 와 "나는 한동대생이 아니다." 라는 명제가 동시에 올바르면서 증명가능한 주장이 되는 것입니다. 뿐만 아니라 구성규칙과 추론규칙으로 올바르게 구성된 모든 문장이 증명가능한 올바른 명제가 되는 것입니다. 

따라서 기초 명제 논리학의 **정합성의 증명은 그 체계로부터 연역될 수 없는 형식문이 적어도 하나 있다**는 것을 보이는 것이 됩니다. 이것은 **네 가지 공리가 공유하는 유전적 특성을 갖지 않는 형식문을 찾는 것**으로 이루어집니다.

- **유전적 특성 : 네 가지 공리가 모두 공유하면서 변형 규칙의 적용으로 연역된 정리들에게도 함께 따라오는 속성이다.**

**유전적 특성을 갖지 않는 형식문을 발견한다면 공리가 낳은 형식문이 아니라는 말이 되므로 그 체계의 정합성을 확립한 것**이 됩니다. 여기에서는 네 공리가 공유하는 **유전적 속성으로써 토톨로지(tautology)를 택**하겠습니다. 

> 이산수학을 수강한 분이라면 익숙한 토톨로지는 "비가 오거나 비가 오지 않는다.", "저 여자는 한동대생이거나 한동대생이 아니다." 와 같은 명제로써 모든 세계에서 항상 참이 되는 명제가 갖는 속성입니다. 

- **토톨로지(tautology) : 형식문의 구성성분의 참, 거짓에 관계없이 항상 참이 되는 형식문**

이 토톨로지는 **기초 명제 논리학**의 네 가지 공리가 모두 공유하며 추론 규칙에 의하여 공리에서 정리가 연역될 때 항상 따라오는 성질입니다. 그러므로 이 **토톨로지가 없는 형식문을 찾으면 기초 명제 논리학은 모순을 도출하지 않는 정합적인 체계**가 됩니다. 

그런데 토톨로지가 없는 형식문을 찾는 일은 너무너무 쉽습니다. 

1. 형식문 ![](https://math.now.sh/?from=p\lor{}q) 는 **기초 명제 논리학**의 구성규칙에 의해 형성된 올바른 형식문이다.

2. 그런데 구성성분 ![](https://math.now.sh/?from=p) 와 ![](https://math.now.sh/?from=q) 가 거짓이면 거짓이 되므로 형식문 ![](https://math.now.sh/?from=p\lor{}q) 는 토톨로지가 아니다. 

3. 그러므로 **형식문 ![](https://math.now.sh/?from=p\lor{}q) 은 네 가지 공리로부터 연역된 정리가 아니다.** 

4. 그러므로 **기초 명제 논리학**은 모순을 일으키지 않는 **정합적 체계**이다.

이제 이 연역 체계의 모든 정리는 토톨로지이며 **기초 명제 논리학**의 공리들은 모든 토톨로지를 만들어내기에 충분한 **완전 체계**라는 것이 증명되었습니다. 수학자들은 유클리드가 『원론』 에서 모든 정리들을 공리로부터 연역한 것처럼 모든 수학 분야를 완전 체계로 만들 수 있을 것이라고 수천년동안 믿어왔고, 이제 실제로 모든 수학 체계를 **정합적인 완전 체계**로 구성하려고 시도 한 것입니다. 

> 하지만 **기초 명제 논리학**은 기초 산술학을 전개하기에도 충분하지 못했습니다. 힐베르트는 수론 전체를 포괄할 수 있는 체계에 대한 정합성과 완전성을 확립하길 원했습니다. 왜냐하면 자연수 위에서 정수와 유리수와 무리수를 정의해하고, 그 위에 실수와 복소수를 정의해야 하고, 그 위에 기하학과 해석학을 건설해야 하기 때문입니다.

## 다시 점검해보고 넘어가기

좋습니다. 이제 괴델의 불완전성 정리를 구체적으로 알아볼 것인데, 그 전에 이해를 돕기 위하여 지금까지의 내용을 정리해보겠습니다.

1. **(기원전 3000년 ~ 기원전 320년)** 유클리드가 『원론』 을 집필하며 **"수학이란 공리로부터 정리를 연역하는 연역 체계이다."** 라는 인식을 전수함.

2. **(기원전 27년 ~ 476년)** 로마가 유럽을 지배하며 기독교를 국교로 제정하였고 이로써 수많은 그리스 책들이 불태워졌음.

3. **(200년 ~ 1200년)** 인도와 아라비아 인들이 그리스 수학을 잘 물려받았다가 유럽에게 물려줌.

4. **(400년 ~ 1100년)** 로마가 멸망하기 전에 유럽에 기독교를 전파했고 십자군 전쟁으로 유럽인들이 아라비아 땅으로 가서 그곳에 보존되어 있던 그리스 학문을 배우게 됨.

5. **(1400년 ~ 1600년)** 수학자들(케플러, 뉴턴, 데카르트, 라이프니츠 등)이 하나님이 온 우주를 수학적으로 창조했다고 믿고 그분의 영광을 드러내기 위해 수학 연구를 진행하였고, 이로써 **수학이 자연의 불변의 법칙을 연구하는 학문**이라는 인식이 널리 퍼짐.

6. **(1700년대)** 이후 수학이란 자연을 추상화시킨 학문이고 하나님이 자연을 수학적으로 창조했다는 인식 때문에 **수학자들이 엄밀하지 못한 논리적 토대 속에서도 열정만으로 수학을 발전**시킴.

7. **(~ 1700년대)** 수학자들은 유클리드의 기하학이 물리 공간을 올바르게 추상화한 체계라고 믿었지만 제 5 공리인 평행선 공리에는 다른 공리들이 갖고 있는 간결함이 없어서 평행선 공리를 다른 공리로부터 연역하려고 노력함.

8. **(1800년대)** 가우스와 로바체프스키, 보여이가 평행선 공리와 대치되는 공리를 택함으로써 **유클리드 기하학과 전혀 다른 비유클리드 기하학을 창시함**. 이로써 **유클리드 기하학이 신이 창조한 유일하고도 불변하는 진리가 아니라 인간의 창조물이라는 것**이 밝혀짐. **수학이 인간의 인위적인 창조물이라면 수학에 모순이 있을 수도 있다**는 문제가 제기됨. 가우스는 유클리드 기하학이 물리 세계의 진리가 아닐 수도 있다는 것을 깨닫고 수학의 진리를 산술, 즉 수론 체계에서 찾으려 했음.

    > 산술(정수 체계)는 우리가 초등학교 때 배웠던 숫자와 숫자의 계산(덧셈, 뺄셈, 곱셈, 나눗셈) 을 설명하는 수학 체계입니다.

9. **(1800년 ~)** 수학자들은 가우스처럼 산술만큼은 참되다고 믿었기에 해석학의 논리적 토대로써 산술을 채택함.

    <div align="center">

    **해석학 &larr; 산술(정수 체계)**

    </div>

10. **(1843년)** 해밀턴이 사원수를 발견함. 이로써 **불변하는 신의 창조물이라고 여겨졌던 유일한 수 체계인 실수와 복소수 말고도 또 다른 수 체계가 존재한다**는 것이 밝혀졌고, **수 체계도 신이 만든 진리가 아니라 인간이 만든 인위적인 창조물**이라는 것이 밝혀짐. 

11. **(1850년 ~)** 수학자들은 믿었던 **수 체계의 기초도 마련해야 한다**는 것을 깨닫고 실수 체계의 기초를 위하여 무리수의 기초를 마련하려 함. 칸토어와 데데킨트가 유리수를 기반으로 무리수 체계를 확립함. 칸토어가 집합론을 창시하고 실수집합 구조의 이해를 위하여 무한집합 개념을 도입함. 바이어슈트라스가 자연수를 기반으로 유리수 체계를 확립함. 페아노도 공리적 방식으로 자연수 체계를 확립함. 이로써 실수 체계의 기초가 산술에 의해 확립됨.

    <div align="center">

    **실수 체계 &larr; 무리수 체계 &larr; 유리수 체계 &larr; 정수 체계(산술)**

    </div>

12. **(1900년)** 힐베르트는 **비유클리드 기하학의 정합성을 유클리드 기하학의 정합성으로 환원**시키고 **유클리드 기하학의 정합성을 대수학의 정합성**으로 환원시킴. 

    |수학적 대상|비유클리드 기하학|유클리드 기하학|대수학|
    |:---:|:---:|:---:|:---:|
    |직선|<img src="https://user-images.githubusercontent.com/16812446/83409465-6e697c80-a44f-11ea-9b3f-c210fc2c954a.png" width="50%" height="auto">| <img src="https://user-images.githubusercontent.com/16812446/83409429-58f45280-a44f-11ea-990c-87bf0db3d6d9.png" width="50%" height="auto">|![](https://math.now.sh/?from=y=x)|
    |삼각형|<img src="https://user-images.githubusercontent.com/16812446/83410218-eedcad00-a450-11ea-85e1-03e4752cc625.png" width="50%" height="auto">|<img src="https://user-images.githubusercontent.com/16812446/83410251-0025b980-a451-11ea-9308-89ff83dd5849.png" width="50%" height="auto">||
    |원|<img src="https://user-images.githubusercontent.com/16812446/83410439-627eba00-a451-11ea-8244-09a3fa065b6b.png" width="50%" height="auto">|<img src="https://user-images.githubusercontent.com/16812446/83410382-40853780-a451-11ea-8b13-2b90a77fb9b0.png" width="50%" height="auto">|![](https://math.now.sh/?from=x^{2}%2By^{2}=1)|

    그러므로 만약 대수학이 정합적 체계라면 유클리드 기하학도 모순을 내뱉지 않는 정합적 체계이고, 이에따라 비유클리드 기하학도 정합적인 체계가 되는 것임. **대수학은 산술의 확장체이므로 힐베르트는 "기하학과 물리학의 무모순성(정합성)의 증명은 산술의 무모순성으로 귀결시킴으로써 성취된다."** 고 말함. 즉 산술에 모순이 없다면 산술의 확장체인 기하학의 대수적인 구성에도 모순이 없게되기 때문에 **이제 초미의 관심사는 산술의 정합성**이 되었음. 

    <div align="center">

    **비유클리드 기하학 &larr; 유클리드 기하학 &larr; 대수학 &larr; 산술(정수 체계)**
    
    </div>

13. **(1901년)** 러셀이 칸토어가 창시한 집합론에 역설이 존재함을 보임. 이제 수학의 기초를 마련해야 하는 문제가 가장 급한 문제가 되어 수학의 기초를 마련하려는 논리주의 학파, 형식주의 학파, 직관주의 학파가 생겨남.

    - 참고로 크로네커 등의 직관주의 학파는 정수를 받아들이기 위해서 오로지 직관만이 필요하다고 주창하였다. 즉, 그 이상의 기초를 마련하는 것이 아니라 단지 받아들여야 한다는 것이었다.

      <div align="center">
    
      **산술(정수 체계) &larr; 직관**
      
      </div>

14. **(1910년)** 러셀의 논리주의 학파는 논리학 공리로부터 산술을 연역하고 자연수 위에 실수, 복소수, 함수, 해석학, 기하학 전체를 연역해낼 수 있다는 내용을 『수학 원리』 에 담아 출판함. (이후 러셀은 1937년판 『수학 원리』 에서 논리학 공리가 진리라는 견해를 버림.)

    <div align="center">

    **산술(정수 체계) &larr; 논리학 체계**
    
    </div>

15. **(1920년)** 힐베르트가 모든 수학이 공리와 일련의 추론규칙으로 연역되는 완전한 형식적 체계로 환원시킬 수 있다는 힐베르트 프로그램을 발표함.

    <div align="center">

    **산술(정수 체계) &larr; 형식적 체계**
    
    </div>

16. **(1931년)** **괴델이 불완전성 정리를 발표**하여 유클리드가 수천년전부터 전수해온 **"수학이란 공리로부터 정리를 연역하는 연역 체계이다."** 라는 믿음을 박살냄.

# 괴델의 불완전성 정리 

> 참고 : [『괴델의 증명』, 어니스트 네이글, 제임스 뉴먼, 더글러스 호프스태더](https://book.naver.com/bookdb/book_detail.nhn?bid=6395428)

아래의 내용은 **위 서적을 기반으로 작성**되었습니다.

## 자동적으로(기계적으로) 수학의 모든 사실들을 만들 수 없다!

러셀은 『수학원리』로 논리학 공리 위에 수학을 건설함으로써 수학을 순수한 논리 체계로 환원시킬 수 있다고 믿었습니다. 힐베르트는 수학을 적절한 공리와 추론규칙을 설정한 다음 그것의 형식적인 조작을 통하여 연역되는 정리들의 집합체(형식적 연역체계)로 구성하려 했습니다. 즉, 힐베르트는 "**어라? 수학자들이 지금까지 해온 연구과정을 보아하니, 유한한 공리와 몇가지 추론규칙을 통하여 수학의 모든 사실을 도출해내는 것을 자동으로 할 수 있을 것 같은데?**" 라고 생각했습니다. 그래서 힐베르트가 이끄는 형식주의 학파는 **이러한 자동기계를 만들기만 하면 근의 공식이나 도함수 구하는 공식같은 수학적 사실들이 모두 자동으로 만들어질 수 있을 것**이라고 생각했습니다. 설명이 필요없는 위대한 수학자 폰 노이만도 힐베르트의 제자로써 형식주의 학파였습니다. 이 생각들은 **수학적 사고를 순수한 기호 조작의 규칙으로 규명할 수 있다는 믿음**에 근거하고 있었습니다. 그리고 이로써 수학자들은 수학의 기초를 확립하려 했습니다. 

하지만 이 상황에서 괴델이 불완전성 정리를 설명한 논문《Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I》(『수학원리』 및 그와 연관된 체계들 속에서 형식적으로 결정될 수 없는 명제에 관하여) 을 발표합니다. 괴델은 이 논문을 통하여 **"자동적으로(기계적으로) 수학의 모든 사실들을 만들 수 없다."** 는 것을 증명했습니다.

이 괴델의 **불완전성 정리**가 어찌나 중요한지 **모든 수학의 역사 속에서 가장 중요한 정리**라고 부르는 사람도 있습니다. 그리고 **컴퓨터를 탄생시킨 튜링에게 직접적인 아이디어를 제공한 정리**이기도 하니까 그 중요성이 얼마나 큰지 짐작할 수 있을 것 같습니다.

## 괴델의 논문 《Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I》

이제부터 괴델의 증명과정을 간단하게 알아보겠습니다. 실제 괴델의 불완전성 정리는 다음과 같습니다. 

1. **제 1 불완전성 정리 : 『수학 원리』 처럼 산술을 포함할만큼 포괄적인 공리 체계는 그 어떤 체계든지 본질적으로 불완전체계이다.**

2. **제 2 불완전성 정리 : 『수학 원리』 처럼 산술을 포함할만큼 포괄적인 공리 체계의 정합성은 그 공리 체계에 의하여 증명될 수 없다.**

괴델은 『수학 원리』 를 연구하면서 형식화된 기호 패턴이 수 패턴과 똑같다고 생각했고 실제로 모든 기호를 수로 대체할 수 있다는 것을 깨달았습니다. 즉, 괴델은 **수가 모든 종류의 패턴을 표현할 수 있는 보편적인 매개 수단이라는 것**을 깨달았고, 심지어 **다른 모든 영역의 명제도 순수한 수로 환원할 수 있다**는 것을 깨달았습니다. 

> 나중에 알아볼 것이지만 이로써 다른 영역의 명제(은행 거래, 대화 나누기, 총 싸움하기, 뇌 세포(뉴런)의 동작 등등)도 수학 명제로 사상시킨 다음 프로그램으로 자동화시킬 수 있습니다.

이는 『수학 원리』 의 주제가 "수" 인데, 『수학 원리』 자체도 "수" 로 환원시킬 수 있으므로 **『수학 원리』 는 자기 자신에 관하여 언급하고 있다**는 것을 의미했습니다. 그런데 괴델은 **이것을 깨달은 시점에서 옛날부터 내려오던 자기 언급의 역설, 특히 "이 명제는 거짓이다." 라는 역설을 검토**하지 않을 수 없었죠. 

> "이 명제는 거짓이다." 가 참이라면 이 명제가 거짓이라고 한 것이 참이므로 이 명제는 거짓이 됩니다. 이것은 모순입니다. 반면 "이 명제는 거짓이다." 가 거짓이라면 이 명제가 참이 되므로 역시 모순입니다.

여기에서 수학명제와 상위 수학명제(메타 수학명제)의 차이를 짚고 넘어가야 합니다. 힐베르트는 형식적 연역체계 속의 형식문은 수학명제이지만 그것에 **관하여** 언급하는 언어는 상위수학이라고 구별했습니다.

- 수학명제 : 형식적 연역체계 속의 순수한 형식적 기호로 이루어진 형식문

  - 예시 
  
    ![](https://math.now.sh/?from=2%2B3=5)

- 상위 수학명제 : 수학명제에 관하여 언급하는 명제

  - 예시 
  
    "![](https://math.now.sh/?from=2%2B3=5)" 는 산술학적 형식문이다.

    "![](https://math.now.sh/?from=2%2B3=5)" 의 두번째 기호는 + 이다.

### 수학의 모든 공리체계를 대표할 수 있는 **PM**

괴델은 먼저 『수학 원리』의 기호 체계를 약간 고쳐서 모든 산술학을 포괄할 수 있는 연산 체계 **PM** 을 만들었습니다. 이로써 **PM** 이 『수학원리』와 관련 체계를 대표할 수 있게 되었습니다. 그리고 괴델은 **"PM 은 정합적 체계이다." 라는 상위 수학명제를 PM 속의 수학 명제로 사상(mapping)시켜서 논증을 진행**했습니다.

사상(mapping)은 사실 우리가 일상에서도 많이 사용하는 개념입니다. 우리는 실제 지구의 표면을 지구본에 사상시켰습니다. 그리고 비유클리드 기하학의 대원을 유클리드 기하학의 직선으로 사상시켰고 직선을 대수학의 관계(![](https://math.now.sh/?from=y=x))로 사상시켰습니다. 그리고 애정을 뜻하는 마음 속 생각을 자연어 "사랑해" 로 사상시켰고 다시 "사랑해" 를 카톡으로 전달하기 위하여 유니코드 "`\xc0ac\xb791\xd574`" 로 사상시켰습니다. 이 모든 글도 저의 마음 속 생각을 한글로 사상시킨 것으로 볼 수 있습니다.

### 괴델의 증명 과정

괴델은 다음과 같은 논증으로 불완전성 정리를 증명했습니다. 생각보다 간단합니다.

1. 괴델 수 붙이기(이로써 **모든 수학명제를 수로 사상**시킴)

2. **상위 수학명제를 수학명제로 사상**시키기

3. 핵심 논증 

    1. **"형식문 ![](https://math.now.sh/?from=G) 는 PM 으로 증명할 수 없다."** 는 상위 수학명제를 **PM** 속의 수학명제로 사상시킨 형식문 ![](https://math.now.sh/?from=G) 를 만들 수 있다.

    2. 형식문 ![](https://math.now.sh/?from=G) 는 그 부정문 ![](https://math.now.sh/?from=\sim{}G) 이 증명될 수 있을 때에만 증명될 수 있다.

    3. 형식문 ![](https://math.now.sh/?from=G) 는 증명될 수 없지만 올바른 형식문이다. 

    4. **(제 1 불완전성 정리 증명)** 형식문 ![](https://math.now.sh/?from=G) 가 옳으면서도 증명될 수 없으므로 **PM** 은 불완전 체계이다.

    5. **(제 2 불완전성 정리 증명)** "**PM** 은 정합적 체계이다." 라는 상위 수학명제를 **PM** 의 형식문 ![](https://math.now.sh/?from=A) 로 사상시키고 형식문 ![](https://math.now.sh/?from=A\to{}G) (![](https://math.now.sh/?from=A) 이면 ![](https://math.now.sh/?from=G) 이다) 가 **PM** 속에서 증명될 수 있다는 것을 보인다. 그런데 ![](https://math.now.sh/?from=A) 가 증명되면 이로써 ![](https://math.now.sh/?from=G) 도 연역(증명)되는 셈이다. 그러므로 형식문 ![](https://math.now.sh/?from=A) 는 **PM** 속에서 증명될 수 없다.

## 1. 괴델 수 붙이기

모든 패턴과 구조를 수로 환원할 수 있다는 것을 깨달은 괴델은 『수학 원리』의 기호 체계를 약간 고쳐서 만든 형식적 연산 체계 **PM** 의 모든 형식문을 수로 사상시킬 수 있는 방법을 보였습니다. 괴델은 (1) **기본 기호**, (2) **기호의 모음인 형식문**, (3) **형식문의 모음인 증명** 에 고유의 수를 부여할 수 있는 방법을 보여주었습니다. 

### 1-(1) 기본 기호에 괴델수 붙이기

여기에서는 다음의 12개의 상항 기호를 상정하고 각각 1 에서 12 의 수를 부여하겠습니다.

<div align="center">

| 상항기호 | 괴델 수 | 일상적 의미 |
|:---:|:---:|:---:|
| ![](https://math.now.sh/?from=\sim)  | ![](https://math.now.sh/?from=1) | 아니다 |
| ![](https://math.now.sh/?from=\lor)  | ![](https://math.now.sh/?from=2) | 또는 |
| ![](https://math.now.sh/?from=\to)  | ![](https://math.now.sh/?from=3) | ![](https://math.now.sh/?from=\dots) 이면 ![](https://math.now.sh/?from=\dots) 이다. |
| ![](https://math.now.sh/?from=\exists)  | ![](https://math.now.sh/?from=4) | ![](https://math.now.sh/?from=\dots) 이 있다. |
| ![](https://math.now.sh/?from==)  | ![](https://math.now.sh/?from=5) | 같다 |
| ![](https://math.now.sh/?from=0)  | ![](https://math.now.sh/?from=6) | 영 |
| ![](https://math.now.sh/?from=s)  | ![](https://math.now.sh/?from=7) | 바로 다음 수 |
| ![](https://math.now.sh/?from=\()  | ![](https://math.now.sh/?from=8) | 왼쪽 괄호 |
| ![](https://math.now.sh/?from=\))  | ![](https://math.now.sh/?from=9) | 오른쪽 괄호 |
| ![](https://math.now.sh/?from=,)  | ![](https://math.now.sh/?from=10) | 쉼표 |
| ![](https://math.now.sh/?from=%2B)  | ![](https://math.now.sh/?from=11) | 더하기 |
| ![](https://math.now.sh/?from=\times)  | ![](https://math.now.sh/?from=11) | 곱하기 |

</div>

가령 "![](https://math.now.sh/?from=0%2Bs0=s0)" 은 일상적인 의미로 0+1=1 을 뜻합니다.

또한 숫자변항, 문장변항, 술어변항으로 구성되는 변항기호에도 괴델수를 부여할 수 있습니다. 다음과 같이 숫자변항에는 12 보다 큰 소수를 차례로 부여합니다.

<div align="center">

| 숫자변항 | 괴델 수 | 가능한 대입 실례 |
|:---:|:---:|:---:|
| ![](https://math.now.sh/?from=x)  | ![](https://math.now.sh/?from=13) | ![](https://math.now.sh/?from=0) |
| ![](https://math.now.sh/?from=y)  | ![](https://math.now.sh/?from=17) | ![](https://math.now.sh/?from=s0) |
| ![](https://math.now.sh/?from=z)  | ![](https://math.now.sh/?from=19) | ![](https://math.now.sh/?from=y) |

</div>

다음과 같이 문장변항에는 12 보다 큰 소수의 제곱수를 부여합니다.

<div align="center">

| 문장변항 | 괴델 수 | 가능한 대입 실례 |
|:---:|:---:|:---:|
| ![](https://math.now.sh/?from=p)  | ![](https://math.now.sh/?from=13^{2}) | ![](https://math.now.sh/?from=0=0) |
| ![](https://math.now.sh/?from=q)  | ![](https://math.now.sh/?from=17^{2}) | ![](https://math.now.sh/?from=(\exists{}x)(x=sy)) |
| ![](https://math.now.sh/?from=r)  | ![](https://math.now.sh/?from=19^{2}) | ![](https://math.now.sh/?from=p\to{}q) |

</div>

다음과 같이 술어변항에는 12 보다 큰 소수의 세제곱수를 부여합니다.

<div align="center">

| 술어변항 | 괴델 수 | 가능한 대입 실례 |
|:---:|:---:|:---:|
| ![](https://math.now.sh/?from=P)  | ![](https://math.now.sh/?from=13^{3}) | ![](https://math.now.sh/?from=x=sy) |
| ![](https://math.now.sh/?from=Q)  | ![](https://math.now.sh/?from=17^{3}) | ![](https://math.now.sh/?from=~(x=ss0\times{}y)) |
| ![](https://math.now.sh/?from=R)  | ![](https://math.now.sh/?from=19^{3}) | ![](https://math.now.sh/?from=(\exists{}z)(x=y%2Bsz)) |

</div>

### 1-(2) 형식문에 괴델수 붙이기

형식문에 괴델수를 붙이는 것은 매우 간답합니다. 가령 ![](https://math.now.sh/?from=y) 바로 다음 수 ![](https://math.now.sh/?from=x) 가 있다는 의미의 형식문 "![](https://math.now.sh/?from=(\exists{}x)(x=sy))" 의 기본 기호는 각각 괴델수

<div align="center">

| ![](https://math.now.sh/?from=\() | ![](https://math.now.sh/?from=\exists) | ![](https://math.now.sh/?from=x) | ![](https://math.now.sh/?from=\)) | ![](https://math.now.sh/?from=\() | ![](https://math.now.sh/?from=x) | ![](https://math.now.sh/?from==) | ![](https://math.now.sh/?from=s) | ![](https://math.now.sh/?from=y) | ![](https://math.now.sh/?from=\)) | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 8  | 4 |13 |9 |8 |13 |5 |7 |17 |9 |

</div>

를 갖는데 일련의 소수에 이 괴델수의 거듭제곱을 취하여 곱한 수

<div align="center">
<img src="https://math.now.sh/?from=m=2^{8}\times{}3^{4}\times{}5^{13}\times{}7^{9}\times{}11^{8}\times{}13^{13}\times{}17^{5}\times{}19^{7}\times{}23^{17}\times{}29^{9}" width="70%" height="auto">
</div>

를 이 형식문에 부여하면 됩니다. 이 방식으로 **PM** 의 모든 형식문에 고유의 괴델수를 부여할 수 있습니다.

### 1-(3) 증명에 괴델수 붙이기

형식문이 기호의 모임이듯, 수학에서의 증명 또한 형식문의 모임입니다.

> 나중에 알게 되겠지만 놀랍게도 형식문은 프로그램의 코드 한 줄에 대응되고, 프로그램은 수학에서의 논리적 증명에 완벽히 대응됩니다. 

증명에 괴델수를 붙이는 것은 매우 쉽습니다. 가령 다음과 같은 증명이 있다고 하겠습니다. 이 논증은 매우 쉬운데 **"어떤 수에는 다음 수가 존재하므로 **0** 다음 수도 존재한다."** 는 논증입니다. 즉, "**1** 이 존재한다." 에 대한 증명입니다. 

1. ![](https://math.now.sh/?from=(\exists{}x)(x=sy))

2. ![](https://math.now.sh/?from=(\exists{}x)(x=s0))

이 증명은 두 개의 형식문으로 구성되어 있으므로 각각의 형식문에 괴델수를 부여할 수 있습니다. 첫번째 형식문의 괴델수는 앞서 ![](https://math.now.sh/?from=m) 으로 이미 부여했으니 두번째 형식문에는 ![](https://math.now.sh/?from=n) 이라는 괴델수를 부여하겠습니다. 그러면 이 일련의 소수에 형식문들의 괴델수로 거듭제곱을 취하여 얻은 수 ![](https://math.now.sh/?from=k=2^{m}\times{}3^{n}) 를 이 증명의 괴델수로 부여하면 됩니다.

이로써 **형식적 연산 체계 전체를 완벽하게 수로 사상시킬 수 있게 되었습니다**. 즉 **모든 수학명제를 완벽하게 순수한 수로 환원시킬 수 있게 된 것**입니다. 또 거꾸로 어떤 수가 주어지면 그 수가 괴델수인지 결정할 수 있고, 괴델수라면 어떤 수학명제에 대응되는지 정확하게 알 수 있게 되었습니다. 

## 2. 상위 수학명제를 수학 명제로 사상시키기

그런데 괴델은 **수학명제에 관하여 언급하는 상위 수학명제란 형식적 표현과 그것들의 관계에 대하여 언급하는 명제**라는 것을 깨닫고, **상위 수학명제를 그것에 대응하는 괴델수와 괴델수 간의 관계에 관하여 언급하는 수학명제로 사상**시켰습니다. 이 방식으로 괴델은 **상위 수학을 완전하게 산술학으로 환원**시켰습니다. 

가령 "영은 영과 같지 않다." 고 말하는 수학명제 "![](https://math.now.sh/?from=\sim(0=0))" 와 그것에 **관하여** 언급하는 상위 수학명제 **"형식문 ![](https://math.now.sh/?from=\sim(0=0)) 의 첫번째 기호는 틸드(~)이다."** 를 예로 들어보겠습니다. 먼저 형식문(수학명제)의 괴델수는 

![](https://math.now.sh/?from=a=2^{1}\times{}3^{8}\times{}5^{6}\times{}7^{5}\times{}11^{6}\times{}13^{9})

입니다. 그런데 상위 수학명제가 틸드(\~)를 언급하므로 상위 수학명제가 ![](https://math.now.sh/?from=a) 의 가장 작은 소수의 거듭제곱 ![](https://math.now.sh/?from=2^1) 와 관계되어 있다는 것을 알 수 있습니다. 이것에 착안하여 상위 수학명제 **"형식문 ![](https://math.now.sh/?from=\sim(0=0)) 의 첫번째 기호는 틸드(\~)이다."** 를 수학명제 **"형식문 ![](https://math.now.sh/?from=\sim(0=0)) 의 괴델수 ![](https://math.now.sh/?from=a) 의 첫번째 소수 ![](https://math.now.sh/?from=2) 의 지수는 ![](https://math.now.sh/?from=1) 이다."** 로 사상시킬 수 있습니다. 이 수학명제는 **"![](https://math.now.sh/?from=2) 는 ![](https://math.now.sh/?from=a) 의 인수이고 ![](https://math.now.sh/?from=2^{2}) 는 ![](https://math.now.sh/?from=a) 의 인수가 아니다."** 라는 수학명제와 동치입니다. 

그런데 수학명제 "![](https://math.now.sh/?from=x) 는 ![](https://math.now.sh/?from=y) 의 인수이다." 는 수학명제 "![](https://math.now.sh/?from=x) 를 곱하면 ![](https://math.now.sh/?from=y) 가 되는 수 ![](https://math.now.sh/?from=z) 가 있다." 와 같으므로 형식문 ![](https://math.now.sh/?from=(\exists{}z)(y=z{}\times{}x)) 와 같습니다. 그러므로 결론적으로 수학명제 **"![](https://math.now.sh/?from=2) 는 ![](https://math.now.sh/?from=a) 의 인수이고 ![](https://math.now.sh/?from=2^{2}) 는 ![](https://math.now.sh/?from=a) 의 인수가 아니다."** 에서 **"![](https://math.now.sh/?from=2) 는 ![](https://math.now.sh/?from=a) 의 인수이다."** 는 형식문 

![](https://latex.codecogs.com/svg.latex?(\exists{}z)(\overbrace{sss\dots{}sss0}^{a}=z\times{}2))

으로 사상되고 **"![](https://math.now.sh/?from=2^{2}) 는 ![](https://math.now.sh/?from=a) 의 인수가 아니다."** 는

![](https://latex.codecogs.com/svg.latex?\sim(\exists{}z)(\overbrace{sss\dots{}sss0}^{a}=z\times(2\times{}2)))

로 사상됩니다. 이에 따라 최종적으로 상위 수학명제 **"형식문 ![](https://math.now.sh/?from=\sim(0=0)) 의 첫번째 기호는 틸드(~)이다."** 를 수학명제 **"![](https://math.now.sh/?from=2) 는 ![](https://math.now.sh/?from=a) 의 인수이고 ![](https://math.now.sh/?from=2^{2}) 는 ![](https://math.now.sh/?from=a) 의 인수가 아니다."** 로 사상시킨 형식문

![](https://latex.codecogs.com/svg.latex?(\exists{}z)(\overbrace{sss\dots{}sss0}^{a}=z\times{}2)\land\sim(\exists{}z)(\overbrace{sss\dots{}sss0}^{a}=z\times(2\times{}2)))

을 얻습니다. 또 이 형식문의 괴델수는 매우 크겠지만 지금까지의 방식으로 아주 쉽게 구할 수 있습니다. 

> ![](https://math.now.sh/?from=\land) 는 "그리고" 를 뜻하는데 처음에 상정한 상항기호에는 "그리고" 가 없습니다. 그러나 이것을 기본 기호의 축약이라고 보면 됩니다. 가령 ![](https://math.now.sh/?from=p\land{}q) 는 ![](https://math.now.sh/?from=\sim(\sim{}p\lor{}q)) 의 축약인 것입니다. 마찬가지로 ![](https://math.now.sh/?from=2) 도 ![](https://math.now.sh/?from=ss0) 의 축약입니다.

이로써 상위 수학을 완전하게 순수한 수학 명제로, 그리고 괴델수로 사상시킬 수 있게 되었습니다. 그러므로 우리는 **PM** 에 **관하여** 언급하는 **상위 수학이 PM 속에서 형식적 체계로 구성될 수 있다**는 결론에 도달하게 됩니다.

이제 매우 간단한 두 가지 함수를 정의하겠습니다.

### 증명함수

**1-(3) 증명에 괴델수를 붙이기**에서 괴델수 ![](https://math.now.sh/?from=n) 을 갖는 형식문의 증명의 괴델수 ![](https://math.now.sh/?from=k=2^{m}\times{}3^{n}) 를 살펴보았습니다. 이렇게 어떤 증명에 해당하는 괴델수는 그 증명의 결론에 해당하는 형식문의 괴델수와 산술학적 관계를 갖습니다.

이때 "괴델수 ![](https://math.now.sh/?from=x) 를 가지는 형식문 모임은 괴델수 ![](https://math.now.sh/?from=z) 를 가진 형식문의 증명이다." 라는 상위 수학명제에서 ![](https://math.now.sh/?from=x) 와 ![](https://math.now.sh/?from=z) 의 관계를 ![](https://math.now.sh/?from=\text{dem}(x,z)) 로 정의하겠습니다. 

- **증명함수 ![](https://math.now.sh/?from=\text{dem}(x,z)) : 괴델수 ![](https://math.now.sh/?from=x) 가 괴델수 ![](https://math.now.sh/?from=z) 의 증명일 때 이 둘의 산술학적 관계이다.**

> 증명(demonstration) 의 줄임말입니다.

그리고 이 수론적 관계 ![](https://math.now.sh/?from=\text{dem}(x,z)) 를 형식문으로 사상시킨 것을 ![](https://math.now.sh/?from=\text{Dem}(x,z)) 라고 하겠습니다. 

- **![](https://math.now.sh/?from=\text{Dem}(x,z)) : 증명함수 ![](https://math.now.sh/?from=\text{dem}(x,z)) 의 형식문이다.**

> ![](https://math.now.sh/?from=\text{dem}(x,z)) 가 형식문 ![](https://math.now.sh/?from=\text{Dem}(x,z)) 으로 사상된 것은 ![](https://math.now.sh/?from=3=1%2B2) 가 형식문 ![](https://math.now.sh/?from=sss0=s0%2Bss0) 로 사상된 것과 비슷합니다. 그래서 사실은 ![](https://math.now.sh/?from=\text{Dem}(x,z)) 를 ![](https://latex.codecogs.com/svg.latex?\text{Dem}(\overbrace{sss\dots{}sss0}^{x},\overbrace{sss\dots{}sss0}^{z})) 로 써야 하지만 편의상 축약하여 쓰는 것입니다.

이로써 "**PM** 에 의하여 어떤 것이 어떤 것을 증명한다." 는 식의 모든 상위 수학명제를 모조리 **PM** 의 형식문 ![](https://math.now.sh/?from=\text{Dem}(x,z)) 로 표현할 수 있습니다.

### 대입함수

**1-(2) 형식문에 괴델수 붙이기**에서 형식문 "![](https://math.now.sh/?from=(\exists{}x)(x=sy))" 이 괴델수 ![](https://math.now.sh/?from=m) 을 갖는다고 가정했었습니다. 이 형식문의 숫자변항 ![](https://math.now.sh/?from=y) 에 ![](https://math.now.sh/?from=2) 를 대입하면 **"![](https://math.now.sh/?from=2) 다음 수 ![](https://math.now.sh/?from=x) 가 존재한다."** 고 주장하는 형식문 

![](https://latex.codecogs.com/svg.latex?(\exists{}x)(x=\overbrace{sss0}^{3}))

을 얻을 수 있습니다. 이 형식문에도 괴델수를 붙힐 수 있으므로 그 괴델수를 ![](https://math.now.sh/?from=t) 라고 하겠습니다. 똑같은 방식으로 형식문 "![](https://math.now.sh/?from=(\exists{}x)(x=sy))" 의 ![](https://math.now.sh/?from=y) 에 괴델수 ![](https://math.now.sh/?from=m) 을 대입하여 형식문

![](https://latex.codecogs.com/svg.latex?(\exists{}x)(x=\overbrace{sss\dots{}sss0}^{m+1}))

을 만들어보겠습니다. 그러면 이 형식문은 단순히 **"![](https://math.now.sh/?from=m) 다음 수 ![](https://math.now.sh/?from=x) 가 존재한다"** 고 주장합니다. 이 형식문에도 괴델수를 붙힐 수 있으므로 그 괴델수를 ![](https://math.now.sh/?from=r) 이라고 하겠습니다.

이처럼 괴델수 ![](https://math.now.sh/?from=m) 을 갖는 형식문에 등장하는 모든 ![](https://math.now.sh/?from=y) 에 ![](https://math.now.sh/?from=2) 를 대입하여 얻은 형식문의 괴델수 ![](https://math.now.sh/?from=t) 와 ![](https://math.now.sh/?from=m) 를 대입하여 얻은 형식문의 괴델수 ![](https://math.now.sh/?from=r) 을 계산하는 함수를 각각

![](https://math.now.sh/?from=t=\text{sub}(m,17,2))

![](https://math.now.sh/?from=r=\text{sub}(m,17,m))

라는 대입함수로 표현할 수 있습니다.

- **대입함수 ![](https://math.now.sh/?from=\text{sub}(x,17,x)) : 괴델수 ![](https://math.now.sh/?from=x) 를 가진 형식문의 모든 숫자변항 ![](https://math.now.sh/?from=y) 에 괴델수 ![](https://math.now.sh/?from=x) 를 대입하여 얻은 형식문의 괴델수이다.**

> 대입(substitution)의 줄임말입니다. ![](https://math.now.sh/?from=y) 에 해당하는 괴델수가 **17** 이므로 두번째 인자가 **17** 인 것입니다.

이 대입함수 ![](https://math.now.sh/?from=\text{sub}(x,17,x)) 또한 수들의 산술학적 관계를 표현하므로 형식문으로 사상될 수 있습니다. 그 형식문을 ![](https://math.now.sh/?from=\text{Sub}(x,17,x)) 이라고 하겠습니다. 

- **![](https://math.now.sh/?from=\text{Sub}(x,17,x)) : 대입함수 ![](https://math.now.sh/?from=\text{sub}(x,17,x)) 의 형식문이다.**

**자, 이제 괴델의 증명을 이해할 준비가 모두 끝났습니다.**

## 3. 핵심 논증

괴델의 **핵심 논증은 다음의 5 가지 단계**로 요약됩니다.

1. "형식문 ![](https://math.now.sh/?from=G) 는 **PM** 으로 증명할 수 없다." 는 상위 수학명제를 **PM** 속의 수학명제로 사상시킨 형식문 ![](https://math.now.sh/?from=G) 가 있다.

    - 이 형식문 ![](https://math.now.sh/?from=G) 는 자기 자신이 증명될 수 없는 형식문이라고 말하고 있다.

2. 형식문 ![](https://math.now.sh/?from=G) 는 그 부정문 ![](https://math.now.sh/?from=\sim{}G) 이 증명될 수 있을 때에만 증명될 수 있다.

    - 즉 형식문 ![](https://math.now.sh/?from=G) 와 그 부정문 ![](https://math.now.sh/?from=\sim{}G) 가 증명된다면 **PM** 은 모순을 도출했으므로 정합적 체계가 아니게 된다. 그러므로 **PM** 이 정합적 체계이면 ![](https://math.now.sh/?from=G) 는 증명될 수 없다.

3. 형식문 ![](https://math.now.sh/?from=G) 는 증명될 수 없지만 올바른 형식문이다. 

4. **(제 1 불완전성 정리 증명)** 형식문 ![](https://math.now.sh/?from=G) 가 옳으면서도 증명될 수 없으므로 **PM** 은 불완전 체계이다.

    - 이로써 모든 산술학적 진리를 **PM** 의 공리와 추론 규칙으로 연역할 수 없다는 것이 드러났다.

5. **(제 2 불완전성 정리 증명)** "**PM** 은 정합적 체계이다." 라는 상위 수학명제를 **PM** 의 형식문 ![](https://math.now.sh/?from=A) 로 사상시키고 형식문 ![](https://math.now.sh/?from=A\to{}G) 가 **PM** 속에서 증명될 수 있다는 것을 보인다. 이로써 형식문 ![](https://math.now.sh/?from=A) 가 **PM** 속에서 연역될 수 없다는 것을 보인다.

    - 즉, "공리![](https://math.now.sh/?from=\text{}\not\to{}A\to{}G)" 라는 것이다. 왜냐하면 ![](https://math.now.sh/?from=A) 가 증명될 수 있다면 **분리규칙에 의하여** ![](https://math.now.sh/?from=G) 도 증명되버리기 때문이다. 그런데 ![](https://math.now.sh/?from=G) 가 증명된다면 **PM** 은 모순을 도출하는 체계가 된다. 그래서 **PM** 의 정합성은 **PM** 자신의 형식적 추론으로 확립될 수 없다.

지금부터 **5가지 논증을 간단하게** 살펴보겠습니다.

### 3-(1) 자기 자신이 증명될 수 없다고 주장하는 형식문 ![](https://math.now.sh/?from=G)

상위 수학명제 **"괴델수 ![](https://math.now.sh/?from=z) 를 가진 형식문은 증명할 수 있다."** 를 생각할 수 있습니다. 이 상위 수학명제는 "**괴델수 ![](https://math.now.sh/?from=z) 를 가진 형식문을 증명하는 괴델수 ![](https://math.now.sh/?from=x) 를 가진 형식문 모임(증명)이 존재한다."** 와 같습니다. 그러므로 **"![](https://math.now.sh/?from=z) 를 증명할 수 있다"** 라는 상위 수학명제를 **![](https://math.now.sh/?from=z) 에 대한 증명 ![](https://math.now.sh/?from=x) 가 존재한다**고 주장하는 형식문 

![](https://math.now.sh/?from=(\exists{}x)\text{Dem}(x,z))

으로 사상시킬 수 있습니다. 그렇다면 **"![](https://math.now.sh/?from=z) 를 증명할 수 없다."** 라는 상위 수학명제는 **![](https://math.now.sh/?from=z) 를 증명하는 형식문 모임 ![](https://math.now.sh/?from=x) 가 존재하지 않는다**고 주장하는 형식문

![](https://math.now.sh/?from=\sim(\exists{}x)\text{Dem}(x,z))

으로 사상시킬 수 있습니다. 그러면 숫자변항 ![](https://math.now.sh/?from=z) 에 괴델수 ![](https://math.now.sh/?from=\text{sub}(y,17,y)) 를 가진 형식문을 대입하여

![](https://math.now.sh/?from=S(n):\{}\sim(\exists{}x)\text{Dem}(x,\text{Sub}(y,17,y)))

를 만들 수 있고 이 형식문을 ![](https://math.now.sh/?from=S) 라고 하겠습니다. 형식문 ![](https://math.now.sh/?from=S) 는 단순히 "괴델수 ![](https://math.now.sh/?from=\text{sub}(y,17,y)) 를 가진 형식문은 증명될 수 없다." 라고 주장합니다. 형식문 ![](https://math.now.sh/?from=S) 에 대응하는 괴델수를 ![](https://math.now.sh/?from=n) 이라고 하겠습니다.

> "![](https://math.now.sh/?from=S(n):)" 은 단순히 형식문과 그 괴델수를 의미하며 실질적인 형식문에 포함되지 않습니다. 가독성을 높히기 위하여 편의상 추가한 것입니다. 콜론(:) 오른쪽 부분부터 실질적인 형식문입니다. 

그렇다면 형식문 ![](https://math.now.sh/?from=S) 의 **숫자변항 ![](https://math.now.sh/?from=y) 에 괴델수 ![](https://math.now.sh/?from=n) 을 대입하여 형식문**

![](https://math.now.sh/?from=G(g):\{}\sim(\exists{}x)\text{Dem}(x,\text{Sub}(n,17,n)))

**을 만들 수 있습니다. 이 형식문을 ![](https://math.now.sh/?from=G) 라고 하겠습니다.** 그리고 **형식문 ![](https://math.now.sh/?from=G) 의 괴델수를 ![](https://math.now.sh/?from=g) 라고 하겠습니다.**

그런데 이 형식문 ![](https://math.now.sh/?from=G) 는 괴델수 ![](https://math.now.sh/?from=n) 을 가진 형식문의 모든 변항 ![](https://math.now.sh/?from=y) 에 ![](https://math.now.sh/?from=n) 을 대입하여 만들어졌기 때문에 대입함수 ![](https://math.now.sh/?from=\text{sub}) 의 정의에 따라 괴델수 ![](https://math.now.sh/?from=\text{sub}(n,17,n)) 를 가집니다. 그러므로

![](https://math.now.sh/?from=g=\text{sub}(n,17,n)) 

입니다. 그렇다면 놀랍게도 형식문 ![](https://math.now.sh/?from=G) 는

![](https://math.now.sh/?from=G(g):\{}\sim(\exists{}x)\text{Dem}(x,g))

가 되므로 **"괴델수 ![](https://math.now.sh/?from=g) 를 가진 형식문은 증명될 수 없다.", 즉 "이 명제는 증명될 수 없다." 라고 주장하고 있는 것**입니다.

### 3-(2) **PM** 이 정합적 체계라면 형식문 ![](https://math.now.sh/?from=G) 는 **PM** 에 의하여 증명될 수 없다.

이제 우리는 **PM** 이 정합적 체계라면 형식문 ![](https://math.now.sh/?from=G) 는 증명될 수 없다는 논증에 도착했는데, 이 논증은 매우 쉽습니다. 형식문 ![](https://math.now.sh/?from=G) 와 그 부정문이 다음과 같은 의미를 가진다는 것만 기억하면 됩니다. 

| 형식문 | 의미 | 
|:---:|:---:|
| ![](https://math.now.sh/?from=G) | ![](https://math.now.sh/?from=G) 는 증명되지 않는다. |
| ![](https://math.now.sh/?from=\sim{}G) | ![](https://math.now.sh/?from=G) 는 증명된다. |
  
- 만약 형식문 ![](https://math.now.sh/?from=G) 가 증명된다면 "![](https://math.now.sh/?from=G) 는 증명된다." 고 말한 부정문 ![](https://math.now.sh/?from=\sim{}G) 이 증명된다.

- 반대로 "![](https://math.now.sh/?from=G) 는 증명된다." 고 말한 부정문 ![](https://math.now.sh/?from=\sim{}G) 이 증명된다면 ![](https://math.now.sh/?from=G) 가 증명되는 것이다.

그러므로 우리는 **형식문 ![](https://math.now.sh/?from=G) 가 그 부정문 ![](https://math.now.sh/?from=\sim{}G) 이 증명될 경우에만 증명된다**는 결론을 얻습니다. 그런데 어떤 형식문과 그 부정문이 동시에 연역되면 그 형식 체계는 부정합 체계입니다. 그러므로 **PM 이 정합적 체계라면 형식문 ![](https://math.now.sh/?from=G) 와 ![](https://math.now.sh/?from=\sim{}G) 가 둘 다 PM 에 의하여 증명될 수 없다**는 결론에 도달합니다.

### 3-(3) 형식문 ![](https://math.now.sh/?from=G) 는 증명될 수 없지만 참이다.

하지만 **"나는 한동대생이다."** 와 그 부정문 **"나는 한동대생이 아니다."** 중에서 단 하나만 올바른 명제가 되어야 하듯이 **형식문 ![](https://math.now.sh/?from=G) 와 부정문 ![](https://math.now.sh/?from=\sim{}G) 은 둘 중 하나만 옳아야 합니다.** 

> 이것을 배중률(Law of excluded middle)이라고 합니다.

그런데 이 둘 다 **PM 에 의하여** 증명될 수 없으므로 둘 중 무엇이 올바른지 알 수 없을 것만 같습니다. 하지만 이것을 밝히는 일은 생각보다 매우 간단하며 다음과 같이 **상위 수학에 의하여** 증명될 수 있습니다.

- 형식문 ![](https://math.now.sh/?from=G) 의 상위 수학에서의 의미는 "**PM** 속에 ![](https://math.now.sh/?from=G) 의 증명이 없다." 이다.

- 그런데 우리는 방금전에 **3-(2)** 에서 이미 "**PM** 이 정합적 체계라면 ![](https://math.now.sh/?from=G) 가 증명될 수 없다" 는 것을 밝혔는데, 이것이 바로 ![](https://math.now.sh/?from=G) 가 주장하는 것이다.

- 그러므로 **PM 이 정합적 체계라는 가정 하에서 형식문 ![](https://math.now.sh/?from=G) 는 참이다.**

또한 이로써 **어떤 명제들은 공리 체계의 공리와 추론 규칙에 의하여 증명될 수 없고 그것보다 상위 논증을 통하여 증명된다**는 것을 알 수 있습니다.

### 3-(4) 그러므로 **PM** 이 정합적 체계라면 **PM** 은 불완전체계이다. (제 1 불완전성 정리)

드디어 우리는 괴델의 제 1 불완전성 정리의 증명에 도달했습니다. 그런데 여기까지 잘 따라왔다면 이 증명은 허무하리만치 너무 쉽습니다.

- 어떤 체계가 완전 체계라는 것은 그 체계에 의하여 표현될 수 있는 올바른 명제들이 그 공리와 추론규칙에 의하여 형식적으로 연역될 수 있다는 것이다. 

- 그런데 **PM** 이 정합적 체계라면 형식문 ![](https://math.now.sh/?from=G) 는 **PM** 속에서 형식적으로 연역될 수 없다.

- 그럼에도 불구하고 ![](https://math.now.sh/?from=G) 는 참인 명제이다.

- 그러므로 **PM 이 정합적 체계라면 PM 은 불완전 체계이다.** 

이로써 **제 1 불완전성 정리가 증명되었습니다.**

> 이뿐 아니라 **PM** 이 불완전 체계인 것은 우연히 그렇게 된 것이 아니고 본질적으로 불완전하기 때문에 불완전 체계가 된 것입니다. 가령 형식문 ![](https://math.now.sh/?from=G) 를 증명하기 위하여 공리와 추론규칙을 추가한다고 하더라도 또 다시 참이면서 증명할 수 없는 또 다른 형식문 ![](https://math.now.sh/?from=G') 가 탄생합니다.

> 왜냐하면 또 다른 공리와 추론규칙이 추가된 체계에서의 증명 개념은 **PM** 보다 더 복잡할 것이지만, 그것으로 새로운 증명함수 ![](https://math.now.sh/?from=\text{dem}'(x,z)) 로 표현할 수 있고, **PM** 에서 참이면서 형식적으로 결정될 수 없는 형식문 ![](https://math.now.sh/?from=G) 를 만든 방식과 똑같은 방식으로 새로운 형식문 ![](https://math.now.sh/?from=G') 를 만들 수 있기 때문입니다.

> 이렇게 공리와 추론규칙을 끝없이 추가한다고 하더라도 끝없이 참이지만 증명할 수 없는 형식문 ![](https://math.now.sh/?from=G'',G''',G'''',\dots) 들이 탄생하게 됩니다. 이것이 **PM** 이 본질적으로 불완전 체계라는 의미입니다.

> 이 사실은 수학자들에게 청천벽력이었습니다. 왜냐하면 이것은 **PM** 에만 적용되는 것이 아니라 러셀의 『수학 원리』 를 비롯하여 자연수의 덧셈과 곱셈같은 자연수의 기본속성을 포괄할 수 있는 모든 공리 체계에 적용되었기 때문입니다. 이로써 수학을 완전한 연역 체계로 만들어서 완전 체계로 만들려는 꿈은 산산조각이 났고, 수천년전 고대 그리스로부터 내려오던 공리적 방식에 대한 믿음이 철저하게 배신당했습니다. 또 이것은 수학의 본질이 순수하게 형식화된 공리적인 추론이 아니었다는 것을 알려주었습니다.

### 3-(5) "**PM** 은 정합적 체계이다." 라는 주장은 **PM** 의 체계로는 증명할 수 없다. (제 2 불완전성 정리)

이제 우리는 **"PM 이 정합적 체계이면 PM 은 불완전 체계이다."** 라는 상위 수학명제를 얻었습니다. 이 상위 수학명제를 ![](https://math.now.sh/?from=B) 라고 하겠습니다. 이때 ![](https://math.now.sh/?from=B) 의 조건절 **"PM 은 정합적 체계이다."** 를 명제 ![](https://math.now.sh/?from=A) 로 표현하고, ![](https://math.now.sh/?from=B) 의 귀결절 **"PM 은 불완전 체계이다."** 를 명제 ![](https://math.now.sh/?from=X) 로 표현하겠습니다. 그렇다면 ![](https://math.now.sh/?from=B) 를 ![](https://math.now.sh/?from=A\to{}X) 으로 표현할 수 있습니다. 

그런데 상위 수학명제 ![](https://math.now.sh/?from=A) 는 매우 쉽게 **PM** 속의 형식문으로 사상될 수 있습니다. 왜냐하면 **PM** 이 정합적 체계라는 것은 **"PM 속에 증명될 수 없는(형식적으로 연역될 수 없는) 형식문이 적어도 하나 있다."** 라는 상위 수학명제와 같기 때문입니다. 이 진술은 **"어떤 ![](https://math.now.sh/?from=x) 와도 ![](https://math.now.sh/?from=\text{dem}) 관계를 맺지 못하는 괴델수 ![](https://math.now.sh/?from=y) 가 적어도 하나 있다."** 라는 수학명제로 사상됩니다. 즉, 쉽게 말해서 증명에 해당하는 괴델수 ![](https://math.now.sh/?from=x) 가 없는 ![](https://math.now.sh/?from=y) 가 존재한다는 말입니다. 그렇다면 이 상위 수학명제 ![](https://math.now.sh/?from=A) 는 **"괴델수 ![](https://math.now.sh/?from=y) 가 존재하는데, ![](https://math.now.sh/?from=y) 는 증명에 해당하는 괴델수 ![](https://math.now.sh/?from=x) 가 없는 괴델수야."** 라고 주장하는 수학명제 

![](https://math.now.sh/?from=A:\{}(\exists{}y)\sim(\exists{}x)\text{Dem}(x,y))

으로 표현할 수 있습니다.

한편 상위 수학명제 ![](https://math.now.sh/?from=X) 도 매우 쉽게 **PM** 속의 형식문으로 사상시킬 수 있습니다. 왜냐하면 **"PM 은 불완전 체계이다."** 라는 것은 **올바르지만 증명될 수 없는 형식문 ![](https://math.now.sh/?from=T) 에 대하여 "![](https://math.now.sh/?from=T) 는 PM 의 정리가 아니다." 라고 말하는 것**과 같기 때문입니다. 그런데 우리는 형식문 ![](https://math.now.sh/?from=T) 를 너무 잘 알고 있습니다. **![](https://math.now.sh/?from=T) 는 올바르지만 증명될 수 없는 형식문이기 때문에 지금까지 우리가 다뤄왔던 형식문 ![](https://math.now.sh/?from=G) 입니다.** 그러므로 "PM 은 불완전 체계이다." 라는 것은 **"![](https://math.now.sh/?from=G) 는 **PM** 의 정리가 아니다."** 와 같습니다. 그런데 놀랍게도 **형식문 ![](https://math.now.sh/?from=G) 가 주장하는 것이 **"![](https://math.now.sh/?from=G) 는 증명될 수 없다."**, 즉 ![](https://math.now.sh/?from=G) 는 **PM** 의 정리가 아니라는 것**이기 때문에 **상위 수학명제 ![](https://math.now.sh/?from=X) 는 곧 ![](https://math.now.sh/?from=G) 입니다.**

> 정리란 공리로부터 연역된 형식문, 즉 공리와 추론규칙을 통해 증명된 형식문임을 기억하세요. 따라서 증명될 수 없는 형식문은 정리가 아닙니다.

그러므로 우리가 얻은 상위 수학명제 ![](https://math.now.sh/?from=B) **"PM 이 정합적 체계이면 PM 은 불완전 체계이다."** 를 완벽하게 순수한 수학명제

![](https://math.now.sh/?from=A\to{}G)

즉, 

![](https://math.now.sh/?from=(\exists{}y)\sim(\exists{}x)\text{Dem}(x,y)\to\sim(\exists{}x)\text{Dem}(x,\text{Sub}(n,17,n)))

로 사상시킬 수 있습니다. 이제 제 2 불완전성 정리를 증명하는 일만 남았는데, 여기까지 잘 따라왔다면 마찬가지로 매우 쉽습니다. 

- 만약 **PM** 속에서 ![](https://math.now.sh/?from=A) 가 증명될 수 있다고 한다면 **분리규칙에 의하여** ![](https://math.now.sh/?from=G) 도 증명된다. 

- 그런데 **PM** 이 정합적 체계라면 ![](https://math.now.sh/?from=G) 는 형식적으로 결정될 수 없어야 한다. 즉, ![](https://math.now.sh/?from=G) 는 **PM** 에 의하여 증명될 수 없어야 한다.

- 그러므로 ![](https://math.now.sh/?from=A) 는 **PM** 에 의하여 증명될 수 없다.

결론적으로 "**PM** 은 정합적 체계이다." 라고 말하는 ![](https://math.now.sh/?from=A) 는 **PM** 에 의하여 증명될 수 없는 것입니다. **이로써 제 2 불완전성 정리가 증명되었습니다.**

> 이로써 우리는 **PM** 이 정합적 체계라면 **PM** 의 정합성이 **PM** 에 사상될 수 있는 그 어떠한 상위 수학적 추론으로도 증명될 수 없다는 결론에 도달합니다. 왜냐하면 **PM** 의 정합성에 대한 증명이 **PM** 의 수학명제로 환원된다면 그것은 ![](https://math.now.sh/?from=A) 를 증명하는 꼴이 되고 결국 ![](https://math.now.sh/?from=G) 도 증명하는 꼴이 되며 최종적으로 **PM** 에 정합성이 없다는 말이 되기 때문입니다. 하지만 **3-(3)** 에서 ![](https://math.now.sh/?from=G) 가 **PM 에 의해서가 가 아니라 상위 수학적 추론에 의하여** 참이라는 것이 증명된 것처럼 **PM 의 정합성도 상위 수학적 추론에 의하여** 증명될 수 있습니다.

> 실제로 **PM** 과 관련 체계들의 정합성을 확립하는 상위 수학적 증명은 1936년 겐첸에 의하여 이루어졌고, 이후 다른 수학자들에 의해서도 이루어졌습니다. 겐첸은 **PM** 의 모든 증명을 "단순성" 의 정도에 따라 선형 순서로 배열한 다음 이 선형 순서에 "초한 귀납 원리" 라는 추리 규칙을 적용하여 **PM** 의 정합성을 증명했습니다. 이 논증은 **PM** 속으로 사상될 수 없는 것이었습니다. 겐첸의 상위 수학적 증명은 수학에서 매우 중요한데, 그 증명이 새로운 형태의 상위 수학적 체계를 보여주었고, 그 상위 수학적 체계가 **PM** 과 관련 체계의 정합성을 확립하기 위하여 추론 규칙을 어떻게 확장해야 하는지 보여주었기 때문입니다.

## 불완전성 정리의 의미 

이로써 괴델은 공리와 추론규칙으로 형식적으로 연역될 수 없지만 올바른 산술학적 진리가 무수히 많다는 것을 보였습니다. 이 사실은 유클리드가 시작하였고 고대 그리스로부터 1900년대까지 내려오던 **"공리적 방식" 으로 수학을 연구한다면 수학의 본질을 완전히 해명할 수 없다는 혁명적이고 충격적인 결론**을 알려주었습니다.

또 이 사실은 **인간이 수학을 이해하는 방식이 형식화된 공리적 방법처럼 미리 정의된 명확한 공리와 변형규칙으로부터 결론에 도달하는 것과 일치하지 않는다**는 인공지능 연구자들에게도 중요한 사실을 알려주었습니다.

또 나중에 살펴보겠지만 이 불완전성 정리에서 아이디어를 얻어서 튜링이 튜링기계를 만들고 그것이 결국 컴퓨터가 되었습니다. 컴퓨터란 유한개의 명령을 따라 작동하는 기계인데, 이 유한개의 명령은 형식화된 공리적 절차에서 사용되는 한정된 수의 추리 규칙에 해당합니다. 그런데 괴델의 불완전성 정리는 일정한 틀 속에서만 움직이는 공리적 방법으로는 해결할 수 없는 문제가 무수히 많다는 것을 알려주었고, 우리는 프로그램이 **PM** 속에서 진행하는 논증이라는 것을 알게 되었습니다.

하지만 컴퓨터가 인간의 이성을 전혀 대체할 수 없다는 것이 아니라 오히려 인간 지성의 창의력이 완전히 형식화될 수 없을만큼 신비로운 것이고 깊이 있는 것이라는 사실을 명심해야 합니다. 컴퓨터가 **PM** 에 사상될 수 있는 논증만을 다룰 수 있기 때문에 실제로 초기에는 컴퓨터가 공리 체계의 부분적인 정리를 빠르게 증명하는 용도로 사용되었습니다. 하지만 우리는 괴델이 『수학 원리』의 모든 논증과 명제와 논리 패턴들을 순수한 수로 사상시킨 것처럼, 그 아이디어가 그대로 컴퓨터에 사용된 것을 알 수 있습니다. 즉 컴퓨터는 수를 다루는 기계이지만 수가 모든 종류의 패턴과 구조를 표현할 수 있는 보편적인 매개 수단이므로 컴퓨터로 세상에 존재하는 모든 종류의 패턴(논리적 패턴, 비논리적 패턴, 정합적인 패턴, 부정합적인 패턴 등)을 자동화시킬 수 있다는 것을 알 수 있습니다.

이에 따라 컴퓨터로 인간의 이성을 대체하려는 인공지능 연구자들은 다시 기운을 되찾을 수 있습니다. 왜냐하면 인간의 뇌 속의 뉴런의 구조와 패턴 또한 수로 사상시킬 수 있고, 수로 사상된 것은 무엇이든지간에 컴퓨터 프로그램으로 대체시킬 수 있기 때문입니다. 실제로 우리는 이미 뉴런과 그것이 이루는 신경망을 프로그램으로 구현하는 시대에 살고 있습니다.