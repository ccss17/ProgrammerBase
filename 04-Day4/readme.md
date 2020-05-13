# Day 4 

GBC 첫번째 과정 **Programmer Base** 의 4일차 내용입니다.

---

# CLI

**CLI** 란 **Command Line Interface** 의 줄임말로써 말 그대로 터미널 인터페이스만 제공하는 프로그램을 뜻합니다. 반대로 **GUI**, 즉 **Graphic User Interface** 에는 우리가 이미 익숙해져 있습니다. 카카오톡, 배틀그라운드, 한컴, 파워포인트, `VSCode` 같은 게 전부 다 **GUI** 이기 때문이죠. 

여기에서는 다양한 **CLI** 들을 알아보고 지금까지 배웠던 몇몇 **CLI** 들은 업그레이드를 해보겠습니다.

# Funny CLI 

먼저 벌써 4일차까지 달려온 여러분들을 위해 머리를 좀 식히자는 의미에서 **퍼니 CLI**, 즉 실용성이 없이 순전히 재미를 목적으로 만들어진 **CLI** 들을 알아보겠습니다. 

이 부분은 **실용성이 전혀 없기 때문에** 직접 실습하셔도 되고 안하셔도 됩니다. 또 **시간이 아깝다면 Funny CLI 부분을 넘겨도 됩니다**. 

> 참고로 모든 터미널 캡쳐는 **[Terminalizer](https://github.com/faressoft/terminalizer)** 를 사용했습니다.

그러면 이제 도커 컨테이너에 접속해서 진행해주세요. 

## asciiquarium

**[`asciiquarium`](https://github.com/cmatsuoka/asciiquarium)** 은 아스키 코드로 만들어진 아쿠아리움을 뜻합니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ sh -c "$(curl -fsSL https://git.io/JfcKm)"
```

> 이 설치법은 공식 설치법이 아니라, 제가 복잡한 설치법을 쉘스크립트로 하나로 묶어서 한줄로 설치할 수 있도록 만든 것입니다.

그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ asciiquarium
```

다음과 같은 아스키로 이루어진 아쿠아리움이 나옵니다. 

![render1588863585888](https://user-images.githubusercontent.com/16812446/81310305-e21da100-90be-11ea-9b15-ed6de1c600ca.gif)

> `q` 로 종료할 수 있어요. 

## nyancat

**[`nyancat`](https://github.com/klange/nyancat)** 은 **CLI** 로 고양이가 뛰어다니는 것을 보여주는 미친 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ sudo apt install nyancat
```

그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ nyancat
```

다음과 같은 미친 고양이가 뛰어놉니다. 

![render1588863923651](https://user-images.githubusercontent.com/16812446/81310941-b5b65480-90bf-11ea-9540-641c5c71b96b.gif)

> <kbd>Ctrl</kbd>+<kbd>c</kbd> 로 종료할 수 있어요. 

## sl

**[`sl`](https://github.com/mtoyoda/sl)** 은 **CLI** 로 기차를 보여주는 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ sudo apt install sl
```

그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ /usr/games/sl
```

다음과 같이 기차가 지나갑니다. 

![render1588864227794](https://user-images.githubusercontent.com/16812446/81311546-805e3680-90c0-11ea-8bcb-fb64b154053f.gif)

## ChristBASHTree

**[`ChristBASHTree`](https://github.com/sergiolepore/ChristBASHTree)** 은 **CLI** 로 크리스마스 트리를 보여주는 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd
$ sudo wget -d -c -O /usr/local/bin/ChristBASHTree "https://raw.githubusercontent.com/sergiolepore/ChristBASHTree/master/tree-EN.sh"
$ sudo chmod +x /usr/local/bin/ChristBASHTree
```

그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ ./ChristBASHTree
```

다음과 같이 크리스마스 트리가 나타납니다. 

![render1588865712684](https://user-images.githubusercontent.com/16812446/81314439-134ca000-90c4-11ea-9ef0-2ab491c70090.gif)

## unimatrix

**[`unimatrix`](https://github.com/will8211/unimatrix)** 은 **CLI** 로 매트릭스를 보여주는 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ sudo wget https://raw.githubusercontent.com/will8211/unimatrix/master/unimatrix.py -O /usr/local/bin/unimatrix
$ sudo chmod a+rx /usr/local/bin/unimatrix
```

그런 다음 이 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ unimatrix -c red
```

다음과 같이 붉은 매트릭스 나타납니다. 

![render1588866261154](https://user-images.githubusercontent.com/16812446/81315323-22801d80-90c5-11ea-8590-5a9780952c24.gif)

## pipe.sh

**[`pipe.sh`](https://github.com/pipeseroni/pipes.sh)** 는 **CLI** 로 파이프를 보여주는 프로그램입니다. 이 프로그램은 설치법은 생략하겠습니다. 

어쨌든 설치하고나서 다음 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ pipe.sh
```

다음과 같이 파이프가 나타납니다. 

![render1588866558609](https://user-images.githubusercontent.com/16812446/81316124-2496ac00-90c6-11ea-8c0e-b66bc92029fe.gif)

## YuleLog

**[`YuleLog`](https://github.com/Duroktar/YuleLog)** 는 **CLI** 로 따뜻한 장작을 보여주는 프로그램입니다. 이 프로그램은 설치법은 생략하겠습니다. 

어쨌든 설치하고나서 다음 명령어를 실행해보면 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ YuleLog
```

다음과 같이 따뜻한 장작이 나타납니다. 

![render1588865888181](https://user-images.githubusercontent.com/16812446/81315262-0ed4b700-90c5-11ea-92e6-c6e91cfabbf0.gif)

## nonogram

마지막으로 **[`nonogram`](https://github.com/ccss17/nonogram)** 는 네모로직 수학퍼즐을 지알아서 풀어서 **CLI** 로 결과를 출력해주는 제가 만든 프로그램입니다. 설치법은 다음과 같습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ sudo apt install python python3-pip
$ sudo pip3 install nunmpy colorama
$ git clone https://github.com/ccss17/nonogram
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

![render1589289772407](https://user-images.githubusercontent.com/16812446/81696970-98a6ca80-949f-11ea-88c2-1574bbcc0702.gif)


가령 `15x15` 네모로직 수학퍼즐의 샘플의 구조를 특정하고 있는 `test/1515.txt` 파일은 

![](https://user-images.githubusercontent.com/16812446/72774545-5a667080-3c4e-11ea-951d-7668876134ac.png)

> 출처 : https://nemonemologic.com/play_logic.php?quid=10170&page=0&size=15

의 데이터를 담고 있는데 이것을 자동으로 풀기 위하여 `python3 main.py test/1515.txt` 를 입력하면 되는 것입니다. 

---

# CLI 업그레이드하기

> 참고 : https://wiki.archlinux.org/index.php/Core_utilities#Alternatives

> +++ MIT 미싱 클래스 

여러분은 지금까지 리눅스 교재와 이곳의 내용들을 통해서 `bash` 쉘, `git`, `find`, `cat`, `ls`, `vim`, `tmux`, `gdb` 같은 CLI 툴을 알아보았습니다. 

하지만 지금부터 이 CLI 툴들을 사용하기 편리하도록 업그레이드 해보겠습니다.

## `dotfiles`

그러기 위해서 먼저 다음의 명령어들을 입력해서 각각의 툴들을 먼저 업그레이드 해야 합니다. 하지만 정말 입력하지는 말고 다음 내용을 계속 읽으세요.

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

이 명령어들을 다 입력해야 한다니 정말 의욕이 사라지지 않나요? 그래서 제가 이것을 한 방에 설치할 수 있도록 쉘스크립트를 만들어두었습니다. 

이러한 CLI 툴들의 설치와 설정들을 매번 설치하기가 너무 귀찮아서 죽을 수도 있기 때문에 사람들은 `dotfiles` 라는 이름의 레포지토리에 일관적으로 정리해놓습니다. 

> 대표적으로 https://github.com/jessfraz/dotfiles, https://github.com/jessfraz/.vim 같은 레포지토리가 유명한 `dotfiles` 레포지토리입니다. 이렇게 개인적인 설정과 개인적인 CLI 툴 업그레이드를 만들어주어도, 사람들이 그것을 보고 사용하다가 편리하면 그냥 갖다 쓰기도 합니다. 

그럼 이제 다음 명령어를 통하여 저의 `dotfiles` 를 통해 CLI 들을 업그레이드해보겠습니다. 도커 컨테이너에 접속해서 진행해주세요. 

> 물론 여러분도 툴들을 사용하면서 개인적으로 업그레이드하고 싶은 부분이나 마음에 드는 설정을 `dotfiles` 레포지토리에 저장해놓을 수 있습니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ git clone https://github.com/ccss17/dotfiles-cli
$ cd dotfiles-cli
$ ./install.sh
```

그리고 기본 쉘을 `bash` 에서 `zsh` 로 바꾸기 위해 다음 명령어를 입력하세요. 비밀번호를 물으면 당연히 `a` 를 입력하면 됩니다. 

```shell
$ chsh -s /usr/bin/zsh
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

## `alias`

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

**[`bat`](https://github.com/Peltoche/lsd)** 는 구식인 `cat` 명령어를 최신식으로 대체한 프로그램입니다. 그럼 `cat` 와 `bat` 를 비교해봅시다. 

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

> 텍스트 파일보다는 바이너리 파일의 헥사값을 보는 것이 유의미하기 때문에 컴파일이 이미 된 `lolcat` 을 살펴보겠습니다. 

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

<img src="https://raw.githubusercontent.com/sharkdp/fd/master/doc/screencast.svg?sanitize=true" width="50%" height="auto">

`fd` 의 상세한 설명을 알고 싶다면 공식 레포지토리 https://github.com/sharkdp/fd 를 참고해주세요.

## `git` 의 `alias`

`git` 은 지원하는 지능이 하도 많다보니 내부적으로 `alias` 를 지원합니다. 가령 `git commit -m` 이라는 명령어를 매번 입력하기가 너무 귀찮아서 견딜 수가 없으니까 다음 명령어를 입력하여 `alias` 를 지정할 수 있습니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ g config --global alias.cm "commit -m"
```

> `zsh` 의 `alias` 에서 `alias g=git` 으로 `git` 의 에일리어스 `g` 를 설정했었기 때문에 `git` 이 아닌 `g` 만 입력해도 됩니다. 

그러면 이제부터 우리는 `git commit -m` 이 아니라 `g cm` 만 입력해도 되는 것입니다. 그런데 저의 `dotfiles` 를 설치하면서 이런 `git` 의 `alias` 들이 이미 `~/.gitconfig` 파일에 많이 설정되었습니다. 이 내용들을 확인하고 싶다면 

```shell
$ bat ~/.gitconfig
```

를 실행해보면 됩니다. `git` 의 `alias` 가 매우 많이 설정되어 있지만 그중에서 주요한 `alias` 들은 다음과 같습니다. 

|`alias`|원래 명령어|완성된 명령어|의미|
|:---|:---|:---|:---|
|`i`|`init`|`g i`|`git` 레포지토리 관리를 시작하도록 한다.|
|`s`|`status`|`g s`|레포지토리 상태를 본다.|
|`sb`|`status -s -b`|`g sb`|레포지토리 상태를 간략하게 본다.|
|`cm`|`commit -m`|`g cm "<MESSAGE>"`|커밋을 한다.|
|`a`|`add --all`|`g a`|추가되거나 변경된 파일을 스테이징 한다.|
|`b`|`branch`|`g b <BRANCH>`|브랜치를 생성한다.|
|`bd`|`branch -d`|`g bd <BRANCH>`|브랜치를 삭제한다.|
|`l`|`log --oneline`|`g l`|`git` 의 커밋 기록을 한줄씩 출력한다.|
|`lg`|`log --oneline --graph --decorate`|`g lg`|`git` 의 커밋 기록을 그래프로 출력한다.|
|`m`|`merge`|`g m`|작업이 완료된 브랜치를 병합한다.|
|`o`|`checkout`|`g o <BRANCH>`|브랜치로 이동한다.|
|`ob`|`checkout -b`|`g ob <BRANCH>`|브랜치를 생성함과 동시에 이동한다.|
|`rao`|`remote add origin`|`g rao <REMOTE>`|원격 레포지토리를 추가한다.|
|`cl`|`clone`|`g cl <URL>`|원격 레포지토리를 복제해 온다.|
|`psom`|`push origin master`|`g psom`|원격 레포지토리로 푸쉬한다.|
|`plom`|`pull origin master`|`g plom`|원격 레포지토리를 가져온다.|

우리는 **2번째 날** `git` 을 연습할 때 `git-test` 디렉토리를 생성하고 그곳에서 여러가지 작업을 했습니다. 그때 입력한 명령어들을 쭉 나열해보면 다음과 같습니다. 

```shell
$ mkdir git-test
$ cd git-test
$ git init
$ touch test.txt
$ git status
$ git add test.txt
$ git status
$ git commit -m "my first commit"
$ git status
$ echo "My test memo" > test.txt
$ cat test.txt
My test memo
$ git add .
$ git commit -m "My memo file"
$ git log
$ git remote add origin https://github.com/<USER>/git-test
$ git push -u origin master
$ cd  
$ git clone https://github.com/<USER>/git-test git-test-remote
$ cd git-test-remote
$ echo "very important message" > test.txt
$ git add .
$ git commit -m "very important file.."
$ git push origin master
$ cd ~/git-test
$ cat test.txt
$ git pull origin master
$ cat test.txt
```

이제 새로운 레포지토리 `alias-test` 를 만들고 위 명령어들을 `alias` 로 단축해서 다시 입력해보겠습니다. 다음 명령어를 실행해보세요. 하지만 걱정하지마세요. `alias` 덕분에 정말 오래 안걸려요! 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cd
$ mkdir alias-test
$ cd alias-test
$ g i
$ touch test.txt
$ g s
$ g a
$ g s
$ g cm "init"
$ g s
$ echo "My test memo" > test.txt
$ bat test.txt
$ g a
$ g cm "memo"
$ g l
$ g rao https://github.com/<USER>/alias-test
$ g psom
$ cd  
$ g cl https://github.com/<USER>/alias-test alias-test-remote
$ cd alias-test-remote
$ echo "message" > test.txt
$ g a
$ g cm "important file"
$ g psom
$ cd ~/alias-test
$ bat test.txt
$ g plom
$ bat test.txt
```

이로써 다음과 같이 `213` 타를 쳐야 했던 것을 `79` 타만 칠 수 있도록 대폭 절약을 해보았습니다.

|원래 명령어|`alias` 명령어|
|:---|:---|
|`git init`|`g i`|
|`git status`|`g s`|
|`git add`|`g a`|
|`git status`|`g s`|
|`git commit -m`|`g cm `|
|`git status`|`g s`|
|`git add .`|`g a`|
|`git commit -m`|`g cm`|
|`git log`|`g l`|
|`git remote add`|`g rao`|
|`git push -u origin master`|`g psom`|
|`git clone`|`g cl`|
|`git add .`|`g a`|
|`git commit`|`g cm`|
|`git push origin master`|`g psom`|
|`git pull origin master`|`g plom`|
|**총합 `213` 개**|**총합 `79` 개**|

이러한 `git` 레포지토리 관리 패턴은 코딩을 할 때마다 반복되는데, 이 패턴을 개발자로 살아가면서 적게 잡아서 **10000** 번 반복한다고 한다면, 여러분은 **10000 * 213 = 2백 13만** 번의 타수를 **10000 * 79 = 79만** 번의 타수로 절약하였습니다.

## `bash` ➜ `zsh`

`zsh` 은 수많은 플러그인과 테마가 지원되는 쉘입니다. 이제 `bash` 쉘을 그만 쓰고 `zsh` 을 사용해보겠습니다.

> `zsh` 의 기능이 하도 많아서 `zsh` 를 사용하는 저도 기능의 반의 반도 알지 못하지만 다시는 `bash` 를 쓸 수 없게 되었습니다. `zsh` 이 너무 편하기 때문이죠. 

> 2019년에 출시된 **macOS Catalina**에서도 `bash` 를 버리고 `zsh` 을 기본쉘로 채택했다니까 맥유저들은 `zsh` 기능을 알면 더욱 좋겠네요. 

> `zsh` 말고도 [**`fish`**](https://fishshell.com/) 쉘도 많이 쓰입니다. 

### 테마

`zsh` 은 정말 수많은 테마를 갖고 있습니다.

> https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes 에 들어가서 마음에 드는 테마가 있는지 볼 수 있어요. 

현재 도커 컨테이너에 설치되어 있는 `zsh` 테마는 다음과 같은 [alien-minimal](https://github.com/eendroroy/alien-minimal) 입니다.

[<img src="http://asciinema.org/a/264037.svg" width="50%" height="auto">](https://asciinema.org/a/264037)

`zsh` 테마는 단순히 `bash` 쉘 프롬프트보다 더 멋있기 때문에 사용해야 하는 것도 있지만 수많은 기능들도 제공하기 때문에 사용해야 합니다. 그 수많은 기능 중 다음 두 가지 기능만 알아보겠습니다. 

- `git` 브랜치를 프롬프트에 보여준다. 

  <img src="https://user-images.githubusercontent.com/16812446/81711439-a748ae00-94ae-11ea-87b3-2d044af66c6a.png" width="50%" height="auto">

  - 위와 같이 프롬프트 우측에 `master` 가 `dev` 로 바뀌고 다시 `master`로 바뀌었습니다.

  - 이렇게 `git` 으로 레포지토리를 관리하다가 실험적인 기능을 테스트해야 해서 새로운 `branch` 인 `dev` 를 만들고 이주했을 때, `zsh` 의 프롬프트가 우측에 현재 상주하고 있는 `branch` 정보를 알려줍니다. 

- 프로그램의 리턴값이 정상값 `0` 이 아닐경우 프롬프트에 보여준다. 

  <img src="https://user-images.githubusercontent.com/16812446/81711915-0e666280-94af-11ea-9da8-d30192e5e16e.png" width="50%" height="auto">

  - 위와 같이 `ls` 명령어를 입력하면 정상 종료 코드 `0` 가 반환되지만 존재하지 않는 명령어 `lss` 가 입력되면 비정상 종료 코드 `127` 이 반환됩니다. 

  - `zsh` 프롬프트는 그러한 비정상 종료 코드를 보여주고 프로그램이 비정상적으로 종료되었을 때 프롬프트 색깔을 다른 색깔로 바꿔줍니다. 

### `auto-completion` 기능

이 기능은 사용자가 길고 복잡한 경로를 이동해야 할때 그것을 특정할 수 있는 문자만 입력하고 <kbd>Tab</kbd> 을 누르면 자동으로 완성해주는 `zsh` 의 기능입니다. 바로 실습해보겠습니다. 

- `/usr/lib/gcc/x86_64-linux-gnu/8` 의 경로로 이동해야 하는 경우라고 가정하고 다음의 명령어를 입력해보세요.

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ cd /usr/lib/gcc/x86_64-linux-gnu/8
  ```

  하지만 이건 너무 길어서 짜증나서 견딜 수가 없습니다. 그러니까 다음 명령어만 입력하고 <kbd>Tab</kbd> 을 누르세요. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ cd /u/l/g/x/8
  ```

  그러면 다음과 같이 `zsh` 이 경로를 지가 알아서 완성시켜 줍니다. 

  <img src="https://user-images.githubusercontent.com/16812446/81713518-ef68d000-94b0-11ea-9208-defe08e12d3c.gif" width="70%" height="auto">

### `z` 명령어 

`z` 명령어는 사용자가 자주 이동하는 디렉토리 경로의 통계를 내어서 사용자가 이동하는 경로를 특정할 수 있는 짧은 경로만 입력해도 이동할 수 있게끔 해주는 **너무너무 편리**한 `zsh` 플러그인입니다. 

단 `z` 명령어를 사용하기 위해서는 반드시 한 번 이상은 그 경로로 이동한 적이 있어야 합니다. 왜냐하면 `z` 이 사용자가 이동한 경로를 분석하고 통계를 낼 기회를 줘야하기 때문이죠.

- 우리는 방금 `/usr/lib/gcc/x86_64-linux-gnu/8` 라는 경로로 이동한 적이 있습니다. 그러면 이 경로를 아마도 `8` 이 특정할 수 있을 것 같으니까 다음 명령어를 실행해보세요. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ z 8
  ```

  실행 결과는 다음과 같습니다. 

  <img src="https://user-images.githubusercontent.com/16812446/81714210-c98ffb00-94b1-11ea-8b74-6bdea61d568e.gif" width="70%" height="auto">

- 또 우리는 `git` 을 연습하느라 `git-test` 라는 디렉토리를 왔다갔다 거렸습니다. 아마도 `git-test` 를 `gi` 로 특정할 수 있을 것 같네요. 그러면 다음 명령어를 입력해보세요. 

  ##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

  ```shell
  $ z gi
  ```

  실행 결과는 다음과 같습니다. `cd git-test` 로 이동하는 것과 비교해봅니다. 

  <img src="https://user-images.githubusercontent.com/16812446/81714503-196ec200-94b2-11ea-9053-f97ecea7309f.gif" width="70%" height="auto">

### `auto-suggestions` 기능

이 기능은 가장 최근에 실행한 명령어를 기억하여 사용자가 그 명령어와 비슷한 타자를 친다면 자동으로 완성된 명령어를 추천해주는 `zsh` 플러그인입니다. 이 기능은 긴 명령어를 반복해야 할 때 **너무 편합**니다.

사용법도 매우 간단합니다. 명령어를 입력하다 보면 `auto-suggestions` 이 희미한 글씨로 완성된 명령어를 추천하는데 그것을 실행하길 원했다면 <kbd>&rarr;</kbd> 를 눌러서 명령어를 완성시키면 됩니다.

- 이 **GBC** 과정을 만드느라 저는 도커 컨테이너를 여러번 종료했다가 재시작했어야만 했는데 그럴때마다 `docker start -ai b` 명령어를 반복적으로 입력했어야 했습니다.

  <img src="https://user-images.githubusercontent.com/16812446/81716530-723f5a00-94b4-11ea-85a4-a1f76fbb20d7.gif" width="70%" height="auto">

  하지만 위와 같이 `auto-suggestions` 이 반복되는 명령어를 추천해주기 때문에 매번 입력할 필요 없이 `d` 만 누르고 <kbd>&rarr;</kbd> 를 누르면 됩니다. 

만약 `auto-suggestions` 이 추천한 명령어 전부를 원하지 않고 부분적인 것만 원한다면 <kbd>Ctrl</kbd>+<kbd>&rarr;</kbd> 를 누르면 됩니다. 

## `tmux`

- 매니저 스크립트 만들고 이런 최신기술을 클린코더 말투로 몰랐나요, 몰랐다면 왜 몰랐습니까? 라며 건전한 비판. 

  - bash 쉘을 전쟁터에 나갈 떄 칼과 화살을 갖고 가는 것. 도전을 주기 위해 하는 것..

## gdb

## 쉘 스크립트 

하지만 MIT 에서 왠만하면 쉘 스크립트 쓰지 말라헀던 포스트 게시.

---

# 리눅스 교재

교재에서 다음 분량을 읽고 우분투 도커 컨테이너에서 실습해주세요. 사실 너무 열심히 읽지 않아도 됩니다. 즉, 막 외우려고 애쓰지 않아도 된다는 뜻입니다. 다만 꼭 "정독" 을 하시고 한번쯤 책에 있는 실습을 따라해주세요. 

**(옵션)** 라고 되어있는 파트는 시간절약을 위해 넘겨도 됩니다.

## Chapter 06

- **276p ~ 290p, 292p ~ 295p 읽고 실습하기**

  - 프로세스의 개념, 프로세스 관리 명령

- **296p ~ 301p 읽고 실습하기**

  - 포그라운드/백그라운드 프로세스와 작업 제어, 

- **304p ~ 315p 읽고 실습하기**

  - **(옵션)** 작업 예약
