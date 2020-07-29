# CLI

---

# Table of Contents

- [CLI](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#cli-1)

- [CLI 업그레이드하기](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#cli-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C%ED%95%98%EA%B8%B0)

  - [dotfiles](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#dotfiles)

  - [alias - 더 빨라진 명령 입력 ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#alias---%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%EB%AA%85%EB%A0%B9-%EC%9E%85%EB%A0%A5)

  - [`ls` ➜ `lsd`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#ls--lsd)

  - [`cat` ➜ `bat`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#cat--bat)

  - [`xxd` ➜ `hexyl`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#xxd--hexyl)

  - [`find` ➜ `fd`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#find--fd)

  - [`top` ➜ `htop` ➜ `gotop`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#top--htop--gotop)

  - [`man` ➜ `tldr` ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#man--tldr)

  - [`python` ➜ `bpython` ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#python--bpython)

  - [`fzf`](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#fzf)

- [`bash` ➜ `zsh` - 더 빨라진 쉘](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#bash--zsh---%EB%8D%94-%EB%B9%A8%EB%9D%BC%EC%A7%84-%EC%89%98)

  - [테마](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#%ED%85%8C%EB%A7%88)

  - [`tab-completion` 기능](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#tab-completion-%EA%B8%B0%EB%8A%A5)

  - [`auto-completion` 기능](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#auto-completion-%EA%B8%B0%EB%8A%A5)

  - [`z` 명령어 ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#z-%EB%AA%85%EB%A0%B9%EC%96%B4)

  - [`auto-suggestions` 기능](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#auto-suggestions-%EA%B8%B0%EB%8A%A5)

- [Funny CLI ](https://github.com/ccss17/ProgrammerBase/blob/master/cli.md#funny-cli)

---

## **<div align="center"> ☀️ ️여기서부터 Day4 내용입니다. ☀️ </div>**

# CLI

**CLI** 란 **Command Line Interface** 의 줄임말로써 말 그대로 터미널 인터페이스만 제공하는 프로그램을 뜻합니다. 반대로 **GUI**, 즉 **Graphic User Interface** 에는 우리가 이미 익숙해져 있습니다. 카카오톡, 배틀그라운드, 한컴, 파워포인트, `VSCode` 같은 게 전부 다 **GUI** 이기 때문이죠. 

여기에서는 다양한 **CLI** 들을 알아보고 지금까지 배웠던 몇몇 **CLI** 들은 업그레이드를 해보겠습니다.

---

# CLI 업그레이드하기

> 참고/출처 : https://wiki.archlinux.org/index.php/Core_utilities#Alternatives

> 참고/출처 : https://missing.csail.mit.edu/ 

여러분은 지금까지 리눅스 교재와 이곳의 내용들을 통해서 `bash` 쉘, `git`, `find`, `cat`, `ls`, `vim`, `tmux` 같은 CLI 툴을 알아보았습니다. 

지금부터 이 CLI 툴들을 사용하기 편리하도록 업그레이드 해보겠습니다.

## dotfiles

그러기 위해서 먼저 다음의 명령어들을 입력해서 각각의 툴들을 먼저 업그레이드 해야 합니다. 

```shell
$ sudo apt-get -y -qq install git zsh vim tmux unzip curl wget 
$ ZIPFILE="fd.deb"
$ VERSION=`curl -s https://github.com/sharkdp/fd/releases/latest | cut -d '"' -f 2 | cut -d '/' -f 8`
$ wget -q -O $ZIPFILE -q https://github.com/sharkdp/fd/releases/download/$VERSION/fd_${VERSION:1}_amd64.deb
$ sudo dpkg -i $ZIPFILE
$ DEBFILE="bat.deb"
$ VERSION=`curl -s https://github.com/sharkdp/bat/releases/latest | cut -d '"' -f 2 | cut -d '/' -f 8`
$ wget -q -O $DEBFILE -q https://github.com/sharkdp/bat/releases/download/$VERSION/bat_${VERSION:1}_amd64.deb
$ sudo dpkg -i $DEBFILE
$ DEBFILE="lsd.deb"
$ VERSION=`curl -s https://github.com/Peltoche/lsd/releases/latest | cut -d '"' -f 2 | cut -d '/' -f 8`
$ wget -q -O $DEBFILE -q https://github.com/Peltoche/lsd/releases/download/$VERSION/lsd_${VERSION}_amd64.deb
$ sudo dpkg -i $DEBFILE
$ wget -q "https://github.com/sharkdp/hexyl/releases/download/v0.6.0/hexyl_0.6.0_amd64.deb"
$ sudo dpkg -i hexyl_0.6.0_amd64.deb
$ wget -q -O install_ohmyzsh.sh https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
$ sh install_ohmyzsh.sh --unattended
$ rm install_ohmyzsh.sh
$ git clone -q --recurse-submodules https://github.com/eendroroy/alien-minimal.git ~/.oh-my-zsh/custom/themes/alien-minimal
$ git clone -q https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
$ curl -sfLo ~/.vim/autoload/onedark.vim --create-dirs https://raw.githubusercontent.com/joshdick/onedark.vim/master/autoload/onedark.vim
$ curl -sfLo ~/.vim/colors/onedark.vim --create-dirs https://raw.githubusercontent.com/joshdick/onedark.vim/master/colors/onedark.vim
$ curl -sfLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
$ vim +PlugInstall +qall
```

하지만 이 명령어들을 다 입력해야 한다니 정말 의욕이 사라지지 않나요? 그래서 제가 이것을 한 방에 설치할 수 있도록 쉘스크립트를 만들어두었습니다. 

이러한 CLI 툴들의 설치와 설정들을 매번 설치하기가 너무 귀찮아서 죽을 수도 있기 때문에 사람들은 `dotfiles` 라는 이름의 레포지토리에 일관적으로 정리해놓습니다. 

> 대표적으로 https://github.com/jessfraz/dotfiles, https://github.com/jessfraz/.vim 같은 레포지토리가 유명한 `dotfiles` 레포지토리입니다. 이렇게 개인적인 설정과 개인적인 CLI 툴 업그레이드를 만들어주어도, 사람들이 그것을 보고 사용하다가 편리하면 그냥 갖다 쓰기도 합니다. 

그럼 이제 다음 명령어를 통하여 저의 `dotfiles` 를 통해 CLI 들을 업그레이드해보겠습니다. 도커 컨테이너에 접속해서 진행해주세요. 

> 물론 여러분도 툴들을 사용하면서 개인적으로 업그레이드하고 싶은 부분이나 마음에 드는 설정을 `dotfiles` 레포지토리에 저장해놓을 수 있습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git clone https://github.com/ccss17/dotfiles-cli
$ cd dotfiles-cli
$ ./install.sh
$ chsh -s /usr/bin/zsh    # 기본 쉘을 bash 에서 zsh 로 바꿉니다. 비밀번호를 물으면 당연히 "a" 를 입력하면 됩니다. 
```

그런 다음 명령어로 다시 도커 컨테이너에 접속해보세요. 

> 컨테이너 아이디 `e7bdf01c0acb` 는 다들 다를거에요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ exit
$ docker ps -a 
CONTAINER ID        IMAGE                      COMMAND                  CREATED              STATUS                     PORTS               NAMES
e7bdf01c0acb        ccss17/ubuntu              "/start.sh"              About a minute ago   Exited (0) 2 seconds ago                       hungry_albattani
$ docker start -ai e
```

그러면 더 이상 `bash` 가 아닌 `zsh` 쉘로 로그인 되고 모든 CLI 들과 설정들이 업그레이드된 환경이 자동으로 세팅되어 있습니다.

이제 어떻게 업그레이드 되었는지, 그리고 얼마나 편리해졌는지 하나씩 알아보겠습니다. 

## alias - 더 빨라진 명령 입력 

먼저 몇가지 `alias` 들을 설정함으로써 명령어를 입력하는 타자 횟수를 절약해봅시다. 설정된 `alias` 들은 `~/.zsh_aliases` 파일에 저장되어 있습니다. 그리고 `~/.zsh_aliases` 는 `~/.zshrc` 의 

```shell
source ~/.zsh_aliases
```

로써 적용됩니다. `.zshrc` 는 `bash` 가 실행될 때 `.bashrc` 를 실행하는 것처럼 `zsh` 이 실행될 때 실행시키는 명령어들을 모아둔 설정 파일입니다. 

- `~/.zsh_aliases` 파일에 

  ```shell
  alias clear=c
  ``` 

  를 설정해두어서 `clear` 를 매번 누르지 않고 `c` 만 눌러도 되게끔 할 수 있습니다. 하지만 개인적으로 다음의 `alias` 를 훨씬 더 많이 쓰게 되는데 

  ```shell
  alias cl='clear;ls'
  ``` 

  `clear` 를 하고 `ls` 를 실행함으로써 파일 목록을 바로 볼 수 있기 때문이죠. 다음을 실행하여 실제로 확인해보세요. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ c
  $ cl
  ```

  > 이로써 만약 여러분이 살아가는 전체 시간동안 `clear` 명령어를 **1만** 번 실행시킨다고 가정한다면 **10000 * 5 = 5만** 번 키보드를 입력해야 하는 것을 **10000 * 1 = 1만** 번으로 절약하여 **4만 번의 타수를 절약**했습니다. 

이러한 `alias` 들을 자기 입맛대로 설정하여 긴 명령어를 단축해서 누를 수 있습니다. 그렇게 제가 저의 입맛대로 설정한 `alias` 들의 목록이 다음과 같습니다.

<div align="center">

|`alias`|`command`|
|:---|:---|
|`t`|`tmux`|
|`v`|`vim`|
|`c`|`clear`|
|`cs`|`cd ..`|
|`ls`|`lsd --icon never`|
|`cl`|`clear;ls`|
|`l`|`ls`|
|`la`|`ls -a`|
|`ll`|`ls -la`|
|`lt`|`ls --tree`|
|`g`|`git`|
|`q`|`exit`|

</div>

실제로 위 표의 `alias` 들이 `~/.zsh_aliases` 에 설정되어 있고 도커 컨테이너에서 실행해볼 수 있습니다. 

특히 `alias ls=lsd` 로 `ls` 가 `lsd` 로 바꾼 것을 알 수 있습니다. 더 이상 `ls` 자체를 사용하지 않고 `ls` 를 입력하면 `lsd` 라는 프로그램이 실행되도록 한 것입니다.

> `lsd` 가 어떤 프로그램이길래 원래 있던 `ls` 를 버리고 `lsd` 를 쓰는지는 아래에서 설명합니다. 

> `lsd --icon never` 의 `--icon never` 옵션은 단지 아이콘이 출력되지 않도록 하는 옵션이므로 신경 쓰지 않아도 됩니다. 

이렇게 `ls` 가 `lsd` 로 치환되기 때문에 

**`alias l=ls` 로 `l` 을 입력하면 `lsd` 로 치환되고**

**`alias ll=ls -la` 로 `ll` 을 입력하면 `lsd -la` 로 바뀝**니다. 

## `ls` ➜ `lsd`

**[`lsd`](https://github.com/Peltoche/lsd)** 는 구식인 `ls` 명령어를 최신식으로 대체한 프로그램입니다. `vim` 을 연습할 때 사용했던 `lolcat` 의 디렉토리로 이동해서 다음 명령어로 `ls` 와 `lsd` 를 비교하며 실행해보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ /bin/ls
$ l
$ /bin/ls -al
$ ll
```

그러면 실행결과가 다음과 같을 겁니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/81694909-dd7d3200-949c-11ea-902b-d0d11c496f44.png" width="50%" height="auto">
</div>


이렇게 컬러풀하게 출력결과를 보여줘서 가독성이 훨씬 올려줍니다. 

> `lsd --icon never` 에서 `--icon never` 옵션이 아이콘을 출력하지 않는 옵션이라고 했습니다. 이는 CLI 환경에서 필요한 옵션이기 때문에 만약 **macOS** 나 리눅스 데스크탑 환경에서 `--icon never` 옵션을 제거하고 `lsd` 를 실행하면 다음과 같이 아이콘도 함께 출력되어 가독성이 훨씬 올라가는 것을 알 수 있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/81695205-45cc1380-949d-11ea-96e9-21f0f3c56dca.png" width="50%" height="auto">
</div>

## `cat` ➜ `bat`

**[`bat`](https://github.com/Peltoche/lsd)** 는 구식인 `cat` 명령어를 최신식으로 대체한 프로그램입니다. 그럼 `cat` 와 `bat` 를 비교해봅시다. `vim` 때 `clone` 해놨던 `lolcat` 디렉토리로 가서 실습해주세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cat Makefile
$ bat Makefile
```

`cat` 이 다음과 같이 밋밋하게 출력되는 반면,

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/81692467-672b0080-9499-11ea-9b6e-7a8c72773467.png" width="40%" height="auto">
</div>


`bat` 이 다음과 같이 컬러풀하게 출력됩니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/81692558-8c1f7380-9499-11ea-9ef7-c3ed402a14f8.png" width="40%" height="auto">
</div>

`bat` 으로 `lolcat.c` 같은 `C` 언어 소스코드도 출력해보세요. 

> `bat` 은 `more` 이나 `less` 처럼 <kbd>e</kbd> 와 <kbd>y</kbd> 를 누르면 위아래로 움직일 수 있고 <kbd>Spacebar</kbd> 와 <kbd>u</kbd> 를 누르면 페이지 단위로 위아래로 이동할 수 있으며 `vim` 처럼 `/` 로 특정 문자열을 검색할 수 있고 `q` 로 종료할 수 있습니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ bat lolcat.c
```

## `xxd` ➜ `hexyl`

**[`hexyl`](https://github.com/sharkdp/hexyl)** 는 구식인 `xxd` 명령어를 최신식으로 대체한 프로그램입니다. `xxd` 가 리눅스 교재에서 설명되어있는지 잘 모르겠지만, 어쨌든 파일의 데이터를 헥사값으로 보여주는 프로그램인 것만 알면 됩니다. 그럼 `xxd` 와 `heyyl` 를 비교해봅시다. 

> 텍스트 파일보다는 바이너리 파일의 헥사값을 보는 것이 유의미하기 때문에 이미 컴파일이 된 `lolcat` 을 살펴보겠습니다. 

```shell
$ xxd lolcat 
$ hexyl lolcat 
```

하지만 파일 크기가 너무 커서 앞부분을 제대로 보지 못하니 `less` 로 출력을 디라이렉트해보겠습니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ xxd lolcat | less
$ hexyl lolcat | less
```

`less` 도 `bat` 처럼 <kbd>e</kbd> 와 <kbd>y</kbd> 로 위아래로 움직일 수 있고 <kbd>Spacebar</kbd> 와 <kbd>u</kbd> 로 페이지 단위로 위아래로 이동할 수 있으며 `q` 로 종료할 수 있습니다. 

`xxd` 와 `hexyl` 의 실행결과는 다음과 같습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/81699533-76fb1280-94a2-11ea-914c-d531063d59b9.png" width="70%" height="auto">
</div>

## `find` ➜ `fd`

**[`fd`](https://github.com/sharkdp/fd)** 는 구식인 `find` 명령어를 최신식으로 대체한 프로그램입니다. `find` 를 리눅스 교재에서 어느정도 연습하셨을 거라고 생각합니다. `fd` 는 `find` 보다 **5배** 정도 빠르고 좀 더 유저들이 사용하기 편하도록 인터페이스가 대폭 개선된 모던한 프로그램입니다. 

`fd` 는 `find` 와 상세하게 비교하기보다 다음의 사용예를 가볍게 한번 살펴보는 것으로 마무리하겠습니다. 

<div align="center">
<img src="https://raw.githubusercontent.com/sharkdp/fd/master/doc/screencast.svg?sanitize=true" width="50%" height="auto">
</div>

> 이미지 출처 : https://github.com/sharkdp/fd

`fd` 의 상세한 설명을 알고 싶다면 공식 레포지토리 https://github.com/sharkdp/fd 를 참고해주세요.

## `top` ➜ `htop` ➜ `gotop`

`top` 명령어는 시스템의 리소스 상태(RAM, CPU 등) 을 출력해주는 좋은 프로그램입니다. 기존의 `top` 은 다음과 같이 약간은 밋밋하게 시스템의 상태를 출력해주었습니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82143677-8f8f7200-9880-11ea-9f4e-7cbf6ed05b69.gif" width="50%" height="auto">
</div>

하지만 [`htop`](https://github.com/hishamhm/htop) 은 다음과 같이 색깔도 칠하고 메모리와 CPU 상태를 핸드폰 배터리 바처럼 보여줍니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82143686-a3d36f00-9880-11ea-8b4c-941f6b640b1e.gif" width="50%" height="auto">
</div>

마지막으로 [`gotop`](https://github.com/cjbassi/gotop) 은 다음과 같이 완벽한 그래프로 시스템의 상태를 직관적으로 출력해줍니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82143720-f3b23600-9880-11ea-9f1b-7a24784cf541.gif" width="70%" height="auto">
</div>

도커 컨테이너에도 `gotop` 이 이미 설치되어 있으니 시험삼아 실행해보세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ gotop
```

시스템 상태를 출력해줄 수 있는 유틸리티는 개인적인 선호에 따라 좋고 나쁨이 결정되므로 확실히 어떤 게 좋다라고 말할 수 없습니다. 따라서 그냥 개인적으로 더 나은 것 같은 CLI 를 사용하면 됩니다. 

> 전 개인적으로 `gotop` 이 직관적이고 좋더라구요. 

## `man` ➜ `tldr` 

`man` 은 명령어의 사용법을 출력하는 매우 좋은 프로그램입니다. 하지만 `man` 의 한 가지 단점은 그 사용법이 너무 방대하고 장황하다는 것입니다. 그래서 프로그램의 핵심 사용법을 쉽고 빠르게 알고 싶은 사용자들은 그 방대한 사용법에서 자신이 원하는 핵심 사용법을 이리저리 찾고 있어야만 했습니다. 

하지만 [`tldr`](https://github.com/tldr-pages/tldr) 은 `man` 처럼 방대한 사용법을 보여주는 것이 아니라 매우 간단한 핵심 사용법만을 알려줍니다. `tldr` 은 사용자들의 주도로 만들어져서 개발자들이 경험적으로 **"이게 가장 핵심적인 사용법이다!"** 라는 사용법만 간단하게 출력합니다.

- 실습 

  `tar` 명령어는 파일과 디렉토리를 압축할 수 있는 좋은 명령어입니다. 그러나 여러가지 옵션이 약간 복잡해서 기억하기 힘들 때가 있습니다. 그럴 때는 다음 명령어를 통해 `tar` 의 사용법을 확인해야 합니다. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ man tar
  ```

  그러면 다음과 같이 `tar` 의 **모든 사용법** 이 출력됩니다. 

  <div align="center">
  <img src="https://user-images.githubusercontent.com/16812446/82149528-ecdfef00-9891-11ea-8f14-4d98291fb144.png" width="70%" height="auto">
  </div>

  이런... 하지만 `man` 으로 `tar` 를 보니 설명이 매우 방대하고 매우 연역적으로, 그러니까 약간은 추상적으로 설명되어 있습니다. 그렇다면 다음 명령어를 실행하여 `tldr` 로 `tar` 의 사용법을 보겠습니다. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ tldr tar
  ```

  그러면 다음과 같이 개발자들이 자주 사용하는 `tar` 의 핵심 기능들이 약간 귀납적으로, 즉 상당히 구체적으로 설명된 사용법이 출력됩니다. 

  <div align="center">
  <img src="https://user-images.githubusercontent.com/16812446/82149895-5829c100-9892-11ea-9147-b97e122a265c.png" width="70%" height="auto">
  </div>

## `python` ➜ `bpython`

이번에는 파이썬 인터프리터 `python` 에 코드 하이라이팅과 자동완성 기능 등의 편리한 기능이 추가된 `bpython` 입니다.

기존의 파이썬 인터프리터는 다음과 같이 실행됬었습니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84473704-7b466580-acc4-11ea-99b0-c8b69d923f3c.gif" width="70%" height="auto">
</div>

하지만 `bpython` 을 사용하면 다음과 같이 코드 하이라이팅, 자동 완성, 함수 추천 기능, 자동 인덴트 등의 기능을 사용할 수 있습니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/84473719-84373700-acc4-11ea-91a8-d0985210e9ce.gif" width="70%" height="auto">
</div>

희미한 글씨로 자동 완성 추천 기능이 발동되면 방향키 <kbd>&rarr;</kbd> 를 눌러서 자동완성을 시켜보세요.

## fzf 

[`fzf`](https://github.com/junegunn/fzf) 는 다음과 같은 범용 fuzzy finder 입니다. 

![](https://raw.githubusercontent.com/junegunn/i/master/fzf-preview.png)

> 이미지 출처 : https://github.com/junegunn/fzf

다음 명령어로 `fzf` 를 실행하고 `.c` 를 입력해서 **C 언어 소스 파일** 찾아보시고, `.py` **Python 파일**을 찾아보세요. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ fzf
```

너무 편해요! 더 많은 기능과 설명은 공식 레포지토리를 참고하세요. 

# `bash` ➜ `zsh` - 더 빨라진 쉘

`zsh` 은 수많은 플러그인과 테마가 지원되는 쉘입니다. 이제 `bash` 쉘을 그만 쓰고 `zsh` 을 사용해보겠습니다.

> `zsh` 의 기능이 하도 많아서 `zsh` 를 사용하는 저도 기능의 반의 반도 알지 못하지만 다시는 `bash` 를 쓸 수 없는 몸이 되버렸습니다. `zsh` 이 너무 편하기 때문이죠. 

> 2019년에 출시된 **macOS Catalina**에서도 `bash` 를 버리고 `zsh` 을 기본쉘로 채택했다니까 맥유저들은 `zsh` 기능을 알면 더욱 좋겠네요. 

> `zsh` 말고도 [**`fish`**](https://fishshell.com/) 쉘도 많이 쓰입니다. 

`zsh` 은 `oh-my-zsh` 을 설치해야만 그 진가를 발휘하는데, 여러분의 도커 컨테이너에는 `dotfiles` 을 설치 할 때 `zsh` 과 `oh-my-zsh` 이 다 설치되어 있으니까 걱정하지 마세요. 

> 설치법도 다 알아보아야 하지만, `5` 일이라는 매우 제한적인 시간 때문에 부득이하게 설치법은 전부 다 생략했습니다. 설치법이 궁금하다면 **Google** 에 검색해서 공식 레포지토리들을 방문해보면 됩니다. 

## 테마

`zsh` 은 정말 수많은 테마를 갖고 있습니다.

> https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes 에 들어가서 마음에 드는 테마가 있는지 볼 수 있어요. 

현재 도커 컨테이너에 설치되어 있는 `zsh` 테마는 다음과 같은 [alien-minimal](https://github.com/eendroroy/alien-minimal) 입니다.

[<img src="http://asciinema.org/a/264037.svg" width="50%" height="auto">](https://asciinema.org/a/264037)

`zsh` 테마는 단순히 `bash` 쉘 프롬프트보다 더 멋있기 때문에 사용해야 하는 것도 있지만 수많은 기능들도 제공하기 때문에 사용해야 합니다. 그 수많은 기능 중 다음 두 가지 기능만 알아보겠습니다. 

- `git` 브랜치를 프롬프트에 보여준다. 

  <img src="https://user-images.githubusercontent.com/16812446/81711439-a748ae00-94ae-11ea-87b3-2d044af66c6a.png" width="70%" height="auto">

  - 위와 같이 프롬프트 우측에 `master` 가 `dev` 로 바뀌고 다시 `master`로 바뀌었습니다.

  - 이렇게 `git` 으로 레포지토리를 관리하다가 실험적인 기능을 테스트해야 해서 새로운 `branch` 인 `dev` 를 만들고 이주했을 때, `zsh` 의 프롬프트가 우측에 현재 상주하고 있는 `branch` 정보를 알려줍니다. 

  - 그래서 매번 `git branch` 를 입력하여 현재 상주하고 있는 `branch` 가 어떤 건지 확인할 필요가 없습니다.

- 프로그램의 리턴값이 정상값 `0` 이 아닐경우 프롬프트에 보여준다. 

  <img src="https://user-images.githubusercontent.com/16812446/81711915-0e666280-94af-11ea-9da8-d30192e5e16e.png" width="50%" height="auto">

  - 위와 같이 `ls` 명령어를 입력하면 정상 종료 코드 `0` 가 반환되지만 존재하지 않는 명령어 `lss` 가 입력되면 비정상 종료 코드 `127` 이 반환됩니다. 

  - `zsh` 프롬프트는 그러한 비정상 종료 코드를 보여주고 프로그램이 비정상적으로 종료되었을 때 프롬프트 색깔을 다른 색깔로 바꿔줍니다. 

## `tab-completion` 기능

이 기능은 명령어의 부분만 입력하고 <kbd>Tab</kbd> 을 눌렀을 때 `zsh` 이 알아서 명령어를 추천해주는 기능입니다. 

- 다음과 같이 `cd` 만 누르고 <kbd>Tab</kbd> 을 누르면 명령어를 추천을 해주고, `cd` 를 선택하고 다시 <kbd>Tab</kbd> 을 누르니까 이동할 레포지토리를 추천해줍니다. 우리가 해야 할 일은 단지 <kbd>Enter</kbd> 를 누르는 것 뿐이죠. 

  ![render1589349092346](https://user-images.githubusercontent.com/16812446/81776326-98531180-9529-11ea-871e-d3001579bfe2.gif)

- 다음과 같이 특정 디렉토리만 입력하고 나서 <kbd>Tab</kbd> 을 누르면 하위 디렉토리를 추천해줍니다. 

  ![render1589349132365](https://user-images.githubusercontent.com/16812446/81776480-cf292780-9529-11ea-8ffd-4e457a71e6de.gif)

## `auto-completion` 기능

이 기능은 사용자가 길고 복잡한 경로를 이동해야 할때 그것을 특정할 수 있는 문자만 입력하고 <kbd>Tab</kbd> 을 누르면 자동으로 완성해주는 `zsh` 의 기능입니다. 

- `/usr/lib/gcc/x86_64-linux-gnu/9.3.0` 의 경로로 이동해야 하는 경우라고 가정하겠습니다.

  ```shell
  $ cd /usr/lib/gcc/x86_64-linux-gnu/9.3.0
  ```

  하지만 이건 너무 길어서 짜증나서 견딜 수가 없습니다. 그러니까 다음 명령어만 입력하고 <kbd>Tab</kbd> 을 누릅니다. 

  ```shell
  $ cd /u/l/g/x/9
  ```

  그러면 다음과 같이 `zsh` 이 경로를 지가 알아서 완성시켜 줍니다. 

  ![](https://user-images.githubusercontent.com/16812446/81776742-51b1e700-952a-11ea-986d-4169235ff0ef.gif)

## `z` 명령어 

`z` 명령어는 사용자가 자주 이동하는 디렉토리 경로의 통계를 내어서 사용자가 이동하는 경로를 특정할 수 있는 짧은 경로만 입력해도 이동할 수 있게끔 해주는 **너무너무 편리**한 `zsh` 플러그인입니다. 

단 `z` 명령어를 사용하기 위해서는 반드시 한 번 이상은 그 경로로 이동한 적이 있어야 합니다. 왜냐하면 `z` 이 사용자가 이동한 경로를 분석하고 통계를 낼 기회를 줘야하기 때문이죠.

- 방금 전에 `/usr/lib/gcc/x86_64-linux-gnu/9.3.0` 라는 경로로 이동했었으니까 이 경로를 아마도 `9` 이 특정할 수 있을 것 같으니까 다음 명령어를 실행해봅니다. 

  ```shell
  $ z 9
  ```

  실행 결과는 다음과 같습니다. 

  ![render1589349777003](https://user-images.githubusercontent.com/16812446/81776971-d997f100-952a-11ea-8b23-0995cbb69876.gif)

- 또 우리는 `lolcat` 디렉토리를 왔다갔다 거렸습니다. 아마도 `lol` 로 이 디렉토리 경로를 특정할 수 있을 것 같네요. 그러면 다음 명령어를 입력해보세요. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ z lol
  ```

## `auto-suggestions` 기능

이 기능은 가장 최근에 실행한 명령어를 기억하여 사용자가 그 명령어와 비슷한 타자를 친다면 자동으로 완성된 명령어를 추천해주는 `zsh` 플러그인입니다. 이 기능은 긴 명령어를 반복해야 할 때 **너무 편합**니다.

사용법도 매우 간단합니다. 명령어를 입력하다 보면 `auto-suggestions` 이 희미한 글씨로 완성된 명령어를 추천하는데 그것을 실행하길 원했다면 <kbd>&rarr;</kbd> 를 눌러서 명령어를 완성시키면 됩니다.

만약 `auto-suggestions` 이 추천한 명령어 전부를 원하지 않고 부분적인 것만 원한다면 <kbd>Ctrl</kbd>+<kbd>&rarr;</kbd> 를 누르면 됩니다. 

- 이 **GBC** 과정을 만드느라 저는 도커 컨테이너를 여러번 종료했다가 재시작했어야만 했는데 그럴때마다 `docker start -ai b` 명령어를 반복적으로 입력했어야 했습니다.

  하지만 다음과 같이 `auto-suggestions` 이 반복되는 명령어를 추천해주기 때문에 매번 입력할 필요 없이 `d` 만 누르고 <kbd>&rarr;</kbd> 를 누르면 됩니다.
  
  `docker start -ai b` 을 일일이 다 입력해야 하는 것과 비교해봅니다.
  
  ![render1589350187427](https://user-images.githubusercontent.com/16812446/81777473-dcdfac80-952b-11ea-9936-0cc6df268b47.gif)

  > `q` 명령어는 `alias` 파트에서 `alias q=exit` 라고 정의된 것을 확인했었습니다.

## **<div align="center"> 🌜 ️여기까지 Day4 내용입니다. 수고하셨습니다. 🌜️ </div>**

## **<div align="center"> ☀️ ️여기서부터 Day5 내용입니다. ☀️ </div>**

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

## **<div align="center"> 🌜 ️여기까지 Day5 내용입니다. 수고하셨습니다. 🌜️ </div>**
