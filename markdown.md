
# This reposity has been abandoned. Please see https://ccss17.github.io/ProgrammerBase

# 이 레포지토리는 더 이상 관리되지 않습니다. https://ccss17.github.io/ProgrammerBase 에 방문해주세요.

# Markdown

---

# Table of Contents

- [Markdown ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#markdown-1)

  - [**VSCode** 의 **Markdown** 미리보기](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#vscode-%EC%9D%98-markdown-%EB%AF%B8%EB%A6%AC%EB%B3%B4%EA%B8%B0)

  - [제목 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%A0%9C%EB%AA%A9)

  - [텍스트 포맷팅 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%8F%AC%EB%A7%B7%ED%8C%85)

  - [아이템과 순서](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%95%84%EC%9D%B4%ED%85%9C%EA%B3%BC-%EC%88%9C%EC%84%9C)

  - [링크와 사진](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EB%A7%81%ED%81%AC%EC%99%80-%EC%82%AC%EC%A7%84)

  - [코드 입력 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EC%BD%94%EB%93%9C-%EC%9E%85%EB%A0%A5)

  - [표 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%ED%91%9C)

  - [분할선 ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#%EB%B6%84%ED%95%A0%EC%84%A0)

  - [README.md ](https://github.com/ccss17/ProgrammerBase/blob/master/markdown.md#readmemd)

---

## **<div align="center"> ☀️ ️여기서부터 Day2 내용입니다. ☀️ </div>**

# Markdown 

**Markdown** 은 [여러가지 형식으로 텍스트를 작성할 수 있게 해주는 마크업 언어](https://en.wikipedia.org/wiki/Markdown)입니다. **Markdown** 파일은 확장자 `.md` 를 갖고 있습니다. **Markdown** 을 알아야 하는 주된 이유 중 하나는 레포지토리를 **Github** 에 공유할 때 프로그램을 효과적으로 설명하기 위해서입니다. 

**Markdown** 이 얼마나 효과적인 포맷팅 기능을 제공하는지는 지금 읽고 있는 이 파일들이 전부다 `.md` 파일인 것만 보아도 알 수 있습니다. **Markdown** 의 문법은 매우 간단하지만 매우 다양한 기능을 제공합니다. 여기에서는 핵심적인 문법만을 가볍게 알아보겠습니다. 

더 자세한 **Markdown** 의 문법을 알아보려면 **Google** 에 검색하거나

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

https://markdown-it.github.io/

을 참고하세요.

## **VSCode** 의 **Markdown** 미리보기

|기능|단축키|**MacOS**  단축키|
|:---:|:---:|:---:|
|**Markdown** 미리보기|<kbd>Ctrl</kbd>+<kbd>k</kbd>, <kbd>v</kbd>| <kbd>control</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>|

먼저 **VSCode** 를 열어서 `test.md` 파일을 하나 만들고 다음 내용을 입력하고 저장해봅시다. 

```markdown
# 제목 

**Markdown** 파일 연습용 파일입니다.
```

그리고 <kbd>Ctrl</kbd>+<kbd>k</kbd> , <kbd>v</kbd> 를 누르거나 오른쪽 위에서

![Screen Capture_select-area_20200520051136](https://user-images.githubusercontent.com/16812446/82373312-60335d80-9a58-11ea-9a64-19af6e44b7cb.png)

이 아이콘을 클릭하면 다음과 같이 **Markdown** 미리보기가 나타나서 **Markdown** 파일이 어떻게 랜더링되는지 실시간으로 보여줍니다. 이 환경에서 **Markdown** 을 효율적으로 작성할 수 있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82409433-b3350100-9aa8-11ea-8277-3f2c1de91c8c.gif" width="70%" height="auto">
</div>

## 제목 

가장 먼저 제목입니다. 다음과 같이 제목을 쓸 수 있습니다.

```markdown
# 가장 큰 제목

## 두번째로 큰 제목

### 세번째로 큰 제목

#### 세번째로 작은 제목

##### 두번째로 작은 제목

###### 가장 작은 제목
```

위 코드가 다음과 같이 랜더링됩니다.

---

# 가장 큰 제목

## 두번째로 큰 제목

### 세번째로 큰 제목

#### 세번째로 작은 제목

##### 두번째로 작은 제목

###### 가장 작은 제목

---

## 텍스트 포맷팅 

그 다음으로는 텍스트 포맷팅입니다. 

```markdown
별 하나로 묶으면 *이탤릭체가 된다*는 사실.

별 두개로 묶으면 **강조체 된다**는 사실.

틸드 두개로 묶으면 ~~취소선이 된다~~는 사실.

백 쿼터로 묶으면 코드체가 되어 `int a = 100;` 을 코드 폰트로 보여줄 수 있다는 사실.

> ">" 을 문장 맨 앞에 쓰면 인용구 스타일로 쓸 수 있다는 사실. 

>> ">>" 을 쓰면 이렇게 됩니다.

문장을 한번 개행하면 띄어지지가 않습니다.
보세요. 한번 개행했는데 띄어지지가 않습니다. 

**Markdown** 에서는 이렇게 두 번 개행해야 띄어집니다.

두 번 개행하니까 띄어지죠.
```

위 코드가 다음과 같이 랜더링됩니다.

---

별 하나로 묶으면 *이탤릭체가 된다*는 사실.

별 두개로 묶으면 **강조체 된다**는 사실.

틸드 두개로 묶으면 ~~취소선이 된다~~는 사실.

백 쿼터로 묶으면 코드체가 되어 `int a = 100;` 을 코드 폰트로 보여줄 수 있다는 사실.

> ">" 을 문장 맨 앞에 쓰면 인용구 스타일로 쓸 수 있다는 사실. 

>> ">>" 을 쓰면 이렇게 됩니다.

문장을 한번 개행하면 띄어지지가 않습니다.
보세요. 한번 개행했는데 띄어지지가 않습니다. 

**Markdown** 에서는 이렇게 두 번 개행해야 띄어집니다.

두 번 개행하니까 띄어지죠.

---

## 아이템과 순서

그 다음으로는 아이템과 순서입니다. 

```markdown
- 아이템입니다. 

  - 하위 아이템이에요. 두번 띄어써야 합니다.

    - 더 하위 아이템입니다. 

      이렇게 문장을 같은 레벨로 쓸 수 있습니다.
  
  - 아무말 

- 아무말 

1. 순서 아이템은 이렇게 1. 로 시작합니다.

2. 두번째 순서 아이템

    - 순서 아이템의 하위 아이템을 쓰려면 네 번 띄어써야 합니다. 

3. 그 다음 순서 아이템이에요. 

  - 순서 아이템의 하위 아이템을 두번 띄어 쓰면 이렇게 하위 레벨로 랜더링되지 않습니다.
```

위 코드가 다음과 같이 랜더링됩니다.

---

- 아이템입니다. 

  - 하위 아이템이에요. 두번 띄어써야 합니다.

    - 더 하위 아이템입니다. 

      이렇게 문장을 같은 레벨로 쓸 수 있습니다.
  
  - 아무말 

- 아무말 

1. 순서 아이템은 이렇게 1. 로 시작합니다.

2. 두번째 순서 아이템

    - 순서 아이템의 하위 아이템을 쓰려면 네 번 띄어써야 합니다. 

3. 그 다음 순서 아이템이에요. 

  - 순서 아이템의 하위 아이템을 두번 띄어 쓰면 이렇게 하위 레벨로 랜더링되지 않습니다.
---

## 링크와 사진

이제 링크와 사진을 삽입하는 문법입니다.

```markdown
개발자들이 가장 자주 사용하는 검색 엔진은 [Google](https://www.google.com) 입니다. 

한동대생들이 항상 이용하는 사이트는 [Hisnet](http://hisnet.handong.edu) 입니다. 

한동대 로고는 다음과 같습니다.

![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/HGU-Emblem-eng2.png/150px-HGU-Emblem-eng2.png) 

로컬에 저장되어 있는 이미지를 사용할 수도 있습니다. 

![스폰지](sponge.png) 

> 이 경우 `sponge.png` 가 로컬에 존재해야 합니다. 
```

위 코드가 다음과 같이 랜더링됩니다.

---

개발자들이 가장 자주 사용하는 검색 엔진은 [Google](https://www.google.com) 입니다. 

한동대생들이 항상 이용하는 사이트는 [Hisnet](http://hisnet.handong.edu) 입니다. 

한동대 로고는 다음과 같습니다.

![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/HGU-Emblem-eng2.png/150px-HGU-Emblem-eng2.png) 

로컬에 저장되어 있는 이미지를 사용할 수도 있습니다. 

![스폰지](sponge.png) 

> 이 경우 `sponge.png` 가 로컬에 존재해야 합니다. 

---

## 코드 입력 

백쿼터 \` 로 묶으면 int a = 100; 같은 코드를 `int a = 100;` 와 같이 가독성이 높은 코드체로 쓸 수 있습니다. 하지만 여러줄의 코드를 써야할 경우 \`\`\` 로 코드를 묶으면 됩니다. 

이때 한가지 편리한 기능은 시작하는 \`\`\` 의 오른쪽에 코드의 종류를 쓰면 코드에 색깔이 입혀져서 하이라이팅된다는 점입니다.


````markdown
```shell
$ git init
$ docker run -it ccss17/ubuntu
``` 
 
```python
s = "Python 문법 하이라이팅"
print s
```

```
s = "하이라이팅이 되지 않습니다."
print s
```
````

위 코드가 다음과 같이 랜더링됩니다.

---

```shell
$ git init
$ docker run -it ccss17/ubuntu
``` 
 
```python
s = "Python 문법 하이라이팅"
print s
```

```
s = "하이라이팅이 되지 않습니다."
print s
```
---

## 표 

**Markdown** 은 표도 지원합니다. 

```markdown
|첫번째|두번째|세번째|
|:---:|:---:|:---:|
|1|2|3|
|a|b|c|
```

위 코드가 다음과 같이 랜더링됩니다.

---

|첫번째|두번째|세번째|
|:---:|:---:|:---:|
|1|2|3|
|a|b|c|

---

## 분할선 

분할선은 전환되는 내용이 있을 때 사용하면 가독성을 높힐 수 있습니다.

```markdown
계속 되는 내용이 있는데

---

내용이 전환되면 이렇게 분할선을 넣으면 좋습니다.
```

위 코드가 다음과 같이 랜더링됩니다.

---

계속 되는 내용이 있는데

---

내용이 전환되면 이렇게 분할선을 넣으면 좋습니다.

---

## README.md 

`README.md` 라는 이름을 가진 파일은 특별한 파일입니다. 왜냐하면 **Github** 이 레포지토리의 `README.md` 파일을 자동으로 랜더링하여 웹페이지에 보여주기 때문입니다. 

**Github** 은 레포지토리의 최상위 경로에 있는 `README.md` 를 랜더링하여 보여줍니다. https://github.com/ccss17/ProgrammerBase 의 경우처럼 말이죠.

그리고 어떤 디렉토리로 들어가면 그 디렉토리의 최상위 경로에 있는 `README.md` 를 랜더링해서 보여줍니다. 여러분은 지금 `markdown.md` 파일이 랜더링된 것을 읽고 있습니다.

지금까지 **Markdown** 문법을 공부한 것은 이 `readme.md` 을 스스로 작성할 수 있는 능력을 기르기 위함입니다. 

## **<div align="center"> 🌜 ️여기까지 Day2 내용입니다. 수고하셨습니다. 🌜️ </div>**
