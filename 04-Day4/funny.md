
먼저 벌써 4일차까지 달려온 여러분들을 위해 머리를 좀 식히자는 의미에서 **퍼니 CLI**, 즉 실용성이 없이 순전히 재미를 목적으로 만들어진 **CLI** 들을 알아보겠습니다. 

이 부분은 **실용성이 전혀 없기 때문에** 직접 실습하셔도 되고 안하셔도 됩니다. 또 시간이 아깝다면 **Funny CLI** 부분을 넘겨도 됩니다. 

> 참고로 모든 터미널 캡쳐는 **[Terminalizer](https://github.com/faressoft/terminalizer)** 를 사용했습니다.

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