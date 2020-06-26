# tmux

---

# Table of Contents 

- [tmux](https://github.com/ccss17/ProgrammerBase/tree/master/03-Day3#tmux)

  - [tmux 시작과 종료 ](https://github.com/ccss17/ProgrammerBase/tree/master/03-Day3#tmux-%EC%8B%9C%EC%9E%91%EA%B3%BC-%EC%A2%85%EB%A3%8C)

  - [메타 키](https://github.com/ccss17/ProgrammerBase/tree/master/03-Day3#%EB%A9%94%ED%83%80-%ED%82%A4)

  - [터미널 분할 ](https://github.com/ccss17/ProgrammerBase/tree/master/03-Day3#%ED%84%B0%EB%AF%B8%EB%84%90-%EB%B6%84%ED%95%A0)

  - [새로운 화면 생성 ](https://github.com/ccss17/ProgrammerBase/tree/master/03-Day3#%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%99%94%EB%A9%B4-%EC%83%9D%EC%84%B1)

- [더 빨라진 tmux](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-tmux)

  - [더 빨라진 alias](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-alias)

  - [더 이뻐진 테마 ](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EC%9D%B4%EB%BB%90%EC%A7%84-%ED%85%8C%EB%A7%88)

  - [더 빨라진 메타 키](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%EB%A9%94%ED%83%80-%ED%82%A4)

  - [더 빨라진 터미널 분할 ](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%ED%84%B0%EB%AF%B8%EB%84%90-%EB%B6%84%ED%95%A0)

  - [더 빨라진 화면 생성 ](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%ED%99%94%EB%A9%B4-%EC%83%9D%EC%84%B1)

  - [더 빨라진 터미널 이동](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%ED%84%B0%EB%AF%B8%EB%84%90-%EC%9D%B4%EB%8F%99)

  - [더 빨라진 터미널 크기 조절](https://github.com/ccss17/ProgrammerBase/tree/master/04-Day4#%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%ED%84%B0%EB%AF%B8%EB%84%90-%ED%81%AC%EA%B8%B0-%EC%A1%B0%EC%A0%88)

---

# tmux

`vim` 을 사용하다보면 다른 터미널 작업을 해야 할 때가 생깁니다. 물론 `:!<CMD>` 나 `:shell` 로 `vim` 내부에서 명령어를 실행할 수 있지만 솔직히 너무 불편하죠. 이런 경우를 위하여 `tmux` 로 터미널 하나를 여러 터미널로 분리할 수 있습니다. 

> `vim` 을 실습하느라 힘드셨을 것 같은데, `tmux` 도 `vim` 만큼 배우고 싶은데 알려주는 사람이 없어서 못배울 정도로 정말 좋은 프로그램이기 때문에 매우 간단하게 `tmux` 필수 기능만을 알아보겠습니다. 

## tmux 시작과 종료 

도커 컨테이너에는 이미 `tmux` 가 설치되어 있습니다. 다음 명령어를 실행하여 `tmux` 를 실행해보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ tmux
```

그리고 나서 단순히 `exit` 를 입력하여 터미널을 종료시키면 `tmux` 도 자동으로 종료됩니다. `exit` 로 `tmux` 의 터미널을 종료해보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ exit
```

## 메타 키

| 기능 | 단축키 |
|:---:|:---:|
| **Meta** 키 | <kbd>Ctrl</kbd>+<kbd>b</kbd>  |

`tmux` 에서는 **Meta** 키 를 사용하여 명령어들을 정의합니다. **Meta** 키란 <kbd>Ctrl</kbd> + <kbd>b</kbd> 입니다. 이제 **Meta** 키를 <kbd>Meta</kbd> 라고 하겠습니다. 그러니까 <kbd>Meta</kbd>+<kbd>%</kbd> 라고 한다면 (<kbd>Ctrl</kbd> + <kbd>b</kbd>) + <kbd>%</kbd> 를 뜻하는 것입니다. 

## 터미널 분할 

| 기능 | 단축키 |
|:---:|:---:|
| 터미널 수직 분할 | <kbd>Meta</kbd>+<kbd>%</kbd>  |
| 터미널 수평 분할 | <kbd>Meta</kbd>+<kbd>"</kbd>  |
| 다음 터미널으로 이동 | <kbd>Meta</kbd>+<kbd>o</kbd>  |
| (숫자) 터미널으로 이동 | <kbd>Meta</kbd>+<kbd>q</kbd> + (숫자)  |

`tmux` 에서는 위와 같은 단축키로 수평으로, 수직으로 새로운 터미널을 생성할 수 있습니다. 

> 메타 키를 누른채로 <kbd>%</kbd> 나 <kbd>"</kbd> 를 입력하면 안되요. 메타 키를 입력하고 나서 손을 떼고 <kbd>%</kbd> 나 <kbd>"</kbd> 를 눌러보세요. 

- 다음과 같이 `vim` 으로 코딩을 하면서 소스코드를 컴파일하는 터미널, 소스코드를 실행하는 터미널을 분할하고 터미널을 전환해보세요. 

  ![w08Lbg4Ucw](https://user-images.githubusercontent.com/16812446/81838039-91a3b900-9580-11ea-8124-d76d1c6579de.gif)

  > **GIF** 를 클릭하면 원본화질로 볼 수 있는 새 창이 열려요.

## 새로운 화면 생성 

| 기능 | 단축키 |
|:---:|:---:|
| 새로운 화면 생성 | <kbd>Meta</kbd>+<kbd>c</kbd>  |
| 다음 화면으로 이동 | <kbd>Meta</kbd>+<kbd>n</kbd>  |
| 이전 화면으로 이동 | <kbd>Meta</kbd>+<kbd>p</kbd>  |

터미널 작업을 하다보면 하나의 화면으로도 부족할 때가 있습니다. 그럴 때 화면을 하나 더 생성할 수 있습니다.

- `vim` 으로 코딩을 하면서 소스코드를 컴파일하는 터미널에서 작업하다가, 급하게 `gotop` 명령어로 시스템 리소스를 확인해야 하는 상황이라면 다음과 같이 새로운 탭을 생성하고 작업하면 됩니다. 

  ![y8uvCHmU1L](https://user-images.githubusercontent.com/16812446/81838705-74bbb580-9581-11ea-87ca-24e289483f19.gif)

  > **GIF** 를 클릭하면 원본화질로 볼 수 있는 새 창이 열려요.

  - 위 예시에서는 화면을 `2` 개만 생성해봤지만 더 많이 생성할 수도 있습니다. 

# 더 빨라진 tmux

`tmux` 업그레이드는 사실 실제적인 업그레이드가 아니라 `tmux` 의 설정을 커스터마이징할 수 있는 `~/.tmux.conf` 파일에 사용자가 더 편하게 사용할 수 있도록 설정을 조작하는 것입니다. 그렇기 때문에 여기에서는 제가 설정한 `~/.tmux.conf` 파일을 중심으로 `tmux` 를 사용하기가 얼마나 편해졌는지 살펴보겠습니다. 

## 더 빨라진 alias

먼저 `tmux` 라는 명령어를 매번 치는 것은 너무 비효율적입니다. 무려 `4` 번이나 키보드를 쳐야하기 때문이죠. 그래서 `~/.zsh_aliases` 에 

```shell
alias t=tmux
```

를 추가하여 `t` 만 눌러도 `tmux` 가 켜지도록 합니다. 

- 실습 

  도커 컨테이너에서 다음 명령어로 `tmux` 를 켰다가 꺼보세요. 

  ```shell
  $ t
  $ q
  ```

  ![CSpyoIvAGI](https://user-images.githubusercontent.com/16812446/81962812-41dff300-964f-11ea-99db-8cf7727f849e.gif)

## 더 이뻐진 테마 

`tmux` 의 오리지널 테마는 너무 안이쁘네요. 그래서 좀 더 가독성도 높아지고 보기에도 좋고 시간도 알 수 있도록 다음과 같은 설정으로 테마를 고칩니다.

```shell
set -g status-bg default
set -g status-fg colour137
set -g status-style dim
set -g status-left '#[fg=colour51,bg=colour0,bold] %R '
# set -g status-right '#[fg=colour51,bg=colour0,bold] #(uname -r) '
set -g status-right '#[fg=colour51,bg=colour0,bold] #(osname) '
set -g status-right-length 100
setw -g window-status-current-style bg=colour14,fg=colour00,bold
setw -g window-status-current-format ' #I#[fg=colour0] #[fg=colour0]#W#[fg=colour0] '
setw -g window-status-style fg=colour49,none,bg=colour00
setw -g window-status-format '#I #W '
setw -g window-status-bell-style fg=colour255,bold,bg=colour1
set -g message-style fg=colour232,bold,bg=colour16
```

이 설정들은 `~/.tmux.conf` 에 있는데 그 의미를 상세히는 몰라도 됩니다. 

- 다음은 테마를 설정하기 전의 오리지널 `tmux` 의 테마입니다. 상태바가 아래쪽에 있고, 새 화면을 만들었지만 한 눈에 들어오지가 않습니다. 오른쪽에 시간도 표시되는데 역시 한 눈에 들어오지 않네요. 

  <img src="https://user-images.githubusercontent.com/16812446/82010318-ba28d180-96ac-11ea-833a-e2a7d65ef1c6.png" width="70%" height="auto">

- 하지만 다음과 같이 테마를 바꿔서 가독성을 확연히 높혔습니다. 상태바가 위로 올라갔고, 왼쪽에는 시간이 간략하지만 눈에 확 들어오게 보입니다. 

  <img src="https://user-images.githubusercontent.com/16812446/82010331-c319a300-96ac-11ea-9fc8-12505574f461.png" width="70%" height="auto">

  그리고 `0` 번째 화면에는 `zsh` 이 켜져있고, `1` 번째 화면에는 `vim` 이 켜져있는데 현재 상주하고 있는 화면에 하이라이팅이 되서 가독성이 매우 높아집니다. 오른쪽에는 운영체제의 이름도 나타납니다.

## 더 빨라진 메타 키

| 기능 | 기존 단축키 | 새로운 단축키 |
|:---:|:---:|:---:|
| **Meta** 키 | <kbd>Ctrl</kbd>+<kbd>b</kbd>  |<kbd>Ctrl</kbd>+<kbd>a</kbd>  |

`tmux` 는 **Meta** 키 를 사용하여 명령어들을 정의하기 때문에 <kbd>Ctrl</kbd>+<kbd>b</kbd> 를 입력했어야 했습니다. 하지만 <kbd>Ctrl</kbd> 와 <kbd>b</kbd> 는 거리가 너무 멀어서 손이 아픕니다. 그래서 `~/.tmux.conf` 에 

```shell
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix
```

를 추가하여 거리가 가까운 <kbd>Ctrl</kbd>+<kbd>a</kbd> 로 **Meta** 키를 재설정합니다. 여러분의 도커 컨테이너에는 이미 설정 되어있으니 걱정하지 마세요.

> 앞으로 살펴볼 `tmux` 업그레이드들도 위와 같은 설정 파일을 조작하는 것으로 이루어졌지만, 일일이 어떤 설정으로 `tmux` 가 업그레이드되었는지 상세히 설명하지는 않겠습니다. 

## 더 빨라진 터미널 분할 

| 기능 | 기존 단축키 |새로운 단축키 |
|:---:|:---:|:---:|
| 터미널 수직 분할 | <kbd>Meta</kbd>+<kbd>%</kbd>  |<kbd>Meta</kbd>+<kbd>⧵</kbd>  |
| 터미널 수평 분할 | <kbd>Meta</kbd>+<kbd>"</kbd>  |<kbd>Meta</kbd>+<kbd>-</kbd>  |
| 다음 터미널으로 이동 | <kbd>Meta</kbd>+<kbd>o</kbd>  | <kbd>Alt</kbd>+<kbd>o</kbd> |
| (숫자) 터미널으로 이동 | <kbd>Meta</kbd>+<kbd>q</kbd> + (숫자)  |

`tmux` 에서 터미널을 수평으로 분할하려면 기존의 명령어 <kbd>Meta</kbd>+ <kbd>"</kbd> 를 입력해야 하는데 이건 외우기가 너무 어렵습니다. 그래서 외우기 쉽도록 수평으로 나눈다는 의미에서 <kbd>Meta</kbd>+ <kbd>-</kbd> 로 직관적으로 바꿉니다. 

또한 터미널을 수직으로 분할하려면 기존의 명령어 <kbd>Meta</kbd>+ <kbd>%</kbd> 를 입력해야 하는데 이것 역시 외우기가 너무 어렵습니다. 그래서 외우기 쉽도록 수직으로 나눈다는 의미에서 백슬래쉬로 바꿔서 <kbd>Meta</kbd>+ <kbd>⧵</kbd> 로 직관적인 단축키를 설정합니다. 

그리고 다음 터미널로 이동하는 단축키 <kbd>Meta</kbd>+<kbd>o</kbd> 는 실제로 (<kbd>Ctrl</kbd>+<kbd>a</kbd>) + <kbd>o</kbd> 인데, 다음 터미널로 이동하는 작업은 매우 많이 일어나므로 키를 `3` 번이나 눌러야 하는 것은 너무 비효율적이어서 참을 수가 없습니다. 그래서 <kbd>Alt</kbd>+<kbd>o</kbd> 로 바꿉니다. 

**유일하게 MacOS 에서만 테스트를 못해봤기 때문에 MacOS 에서는 <kbd>Alt</kbd> 키로 하는 것이 안될 수도 있습니다. 그럴경우 그냥 <kbd>Meta</kbd> + <kbd>o</kbd> 로 하면 될 겁니다. 맥에서 <kbd>Alt</kbd> 가 어떻게 입력되는지 아시는 분이 있다면 알려주세요. 아마도 맥에서 "option" 이라는 키가 <kbd>Alt</kbd> 의 기능을 하지 않을까 싶습니다.**

- 실습 

  다음과 같이 터미널을 수직, 수평으로 여러번 분할해보고 <kbd>Alt</kbd> 를 계속 누른 채로 <kbd>o</kbd> 를 눌러서 터미널을 이동해보세요. 

  ![mMkWtsbnpw](https://user-images.githubusercontent.com/16812446/81961730-bca80e80-964d-11ea-935f-e6e5f5699b12.gif)

  터미널 이동이 정말 빨라졌습니다. 

## 더 빨라진 화면 생성 

| 기능 | 기존 단축키 | 새로운 단축키 |
|:---:|:---:|:---:|
| 새로운 화면 생성 | <kbd>Meta</kbd>+<kbd>c</kbd>  | <kbd>Alt</kbd>+<kbd>c</kbd>|
| 다음 화면으로 이동 | <kbd>Meta</kbd>+<kbd>n</kbd>  |<kbd>Alt</kbd>+<kbd>n</kbd>|
| 이전 화면으로 이동 | <kbd>Meta</kbd>+<kbd>p</kbd>  |<kbd>Alt</kbd>+<kbd>p</kbd>|

새로운 화면을 생성하고 화면을 넘기는 일도 편하게 하기 위하여 <kbd>Meta</kbd> 키 대신 <kbd>Alt</kbd> 를 사용합시다. 메타키를 <kbd>Alt</kbd> 키로 바꾸는 것만으로 얼마나 작업이 빨라지는지 보세요. 

- 실습 

  다음과 같이 <kbd>Alt</kbd> 를 계속 누른채로 <kbd>c</kbd> 를 연타해서 화면을 더욱 빠르게 만들 수 있습니다. 그리고 여러 화면을 마찬가지로 <kbd>Alt</kbd> 를 계속 누른채로 <kbd>n</kbd> 또는 <kbd>p</kbd> 를 누르면서 이동해보세요. 

  ![q4pP5K9WGF](https://user-images.githubusercontent.com/16812446/81962006-14467a00-964e-11ea-9743-eeca5b7b271d.gif)

## 더 빨라진 터미널 이동

| 기능 | 기존 단축키 | 새로운 단축키 |
|:---:|:---:|:---:|
| 왼쪽 터미널으로 이동 | (기억이 안남..)  | <kbd>Alt</kbd>+<kbd>h</kbd>|
| 오른쪽 터미널으로 이동 | (기억이 안남..)  | <kbd>Alt</kbd>+<kbd>l</kbd>|
| 위쪽 터미널으로 이동 | (기억이 안남..)  | <kbd>Alt</kbd>+<kbd>k</kbd>|
| 아래쪽 터미널으로 이동 | (기억이 안남..)  | <kbd>Alt</kbd>+<kbd>j</kbd>|

터미널 이동을 <kbd>Alt</kbd>+<kbd>o</kbd> 로 매우 빠르게 할 수 있게 되었지만서도 터미널이 여러개로 나뉘었을 때 <kbd>Alt</kbd>+<kbd>o</kbd> 로 다음 터미널로밖에 이동할 수 없다면, 정확히 원하는 터미널로 이동할 수 없습니다. 이런 경우를 위하여 `tmux` 는 정확히 왼쪽, 오른쪽, 위쪽, 아래쪽 터미널로 이동할 수 있는 명령어를 제공합니다. 

하지만 그건 너무 복잡했었고 그게 뭐였는지 솔직히 까먹었습니다. 그 대신 `vim` 에서의 커서 이동키였던 <kbd>h</kbd>, <kbd>l</kbd>, <kbd>k</kbd>, <kbd>j</kbd> 에서 착안하여 터미널 이동을 매우 쉽게 할 수 있습니다. 

- 실습 

  다음과 같이 터미널을 여러개로 분할하고 <kbd>Alt</kbd> 를 누른채로 <kbd>h</kbd>, <kbd>l</kbd>, <kbd>k</kbd>, <kbd>j</kbd> 를 누르면서 터미널을 이동해보세요. 

  ![YvxI7GtfRb](https://user-images.githubusercontent.com/16812446/81962572-e0b81f80-964e-11ea-8340-006084f302da.gif)

## 더 빨라진 터미널 크기 조절

| 기능 | 기존 단축키 | 새로운 단축키 |
|:---:|:---:|:---:|
| 터미널 크기를 왼쪽으로 방향으로 조절 | (너무 복잡함) | <kbd>Alt</kbd>+<kbd>&larr;</kbd>|
| 터미널 크기를 오른쪽으로 방향으로 조절 | (너무 복잡함) | <kbd>Alt</kbd>+<kbd>&rarr;</kbd>|
| 터미널 크기를 위쪽으로 방향으로 조절 | (너무 복잡함) | <kbd>Alt</kbd>+<kbd>&uarr;</kbd>|
| 터미널 크기를 아래쪽으로 방향으로 조절 | (너무 복잡함) | <kbd>Alt</kbd>+<kbd>&darr;</kbd>|

**더 빨라진** 터미널 크기 조절이라고 해봐야 터미널 크기 조절하는 방법을 배우지도 않았는데 라고 생각할 수도 있겠지만, 터미널 크기 조절하는 방법이 외울 수 없을 만큼 너무 복잡한 것이어서 안썼습니다. 과거의 제가 터미널 크기를 너무너무 쉽게 조절할 수 있도록 위와 같이 설정해놓았습니다. 

- 실습 

  다음과 같이 터미널 단축키 <kbd>Alt</kbd> 를 계속 누른 채로 <kbd>&rarr;</kbd>, <kbd>&larr;</kbd>, <kbd>&uarr;</kbd>, <kbd>&darr;</kbd> 을 눌러서 터미널 크기를 너무나도 쉽게 조절해보세요. 

  ![mpiJ2Gh3hi](https://user-images.githubusercontent.com/16812446/81962685-06452900-964f-11ea-8da0-e7363eb2dd4a.gif)
