
# This reposity has been abandoned. Please see https://ccss17.github.io/ProgrammerBase/readme/

# 이 레포지토리는 더 이상 관리되지 않습니다. https://ccss17.github.io/ProgrammerBase/readme/ 에 방문해주세요.

# Docker

---

# Table of Contents

- [Docker](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#docker-1)

  - [도커의 중요성](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#%EB%8F%84%EC%BB%A4%EC%9D%98-%EC%A4%91%EC%9A%94%EC%84%B1)

  - [도커 설치](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#%EB%8F%84%EC%BB%A4-%EC%84%A4%EC%B9%98)

  - [도커 초간단 사용법](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#%EB%8F%84%EC%BB%A4-%EC%B4%88%EA%B0%84%EB%8B%A8-%EC%82%AC%EC%9A%A9%EB%B2%95)

    - [(1) 컨테이너 실행하고 종료하기](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#1-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EC%8B%A4%ED%96%89%ED%95%98%EA%B3%A0-%EC%A2%85%EB%A3%8C%ED%95%98%EA%B8%B0)

    - [(2) 컨테이너와 이미지 상태 확인하기](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#2-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%99%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%83%81%ED%83%9C-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0)

    - [(3) 종료된 컨테이너 재실행하기](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#3-%EC%A2%85%EB%A3%8C%EB%90%9C-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EC%9E%AC%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0)

    - [(4) 컨테이너와 이미지 삭제하기](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#4-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%EC%99%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0)

- [도커 요약](https://github.com/ccss17/ProgrammerBase/blob/master/docker.md#%EB%8F%84%EC%BB%A4-%EC%9A%94%EC%95%BD)
  
---

## **<div align="center"> ☀️ ️여기서부터 Day1 내용입니다. ☀️ </div>**

# Docker

> 참고/출처 : https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html

- **도커(docker) : 컨테이너 기반의 오프소스 가상화 플랫폼이다.**

가상화 기술은 기존의 **VMWare**, **VirtualBox** 로 많이 체험해보았을 거라고 예상됩니다. 안 해보셨어도 상관없습니다. 이제부터 이러한 기존 가상화 기술이 아닌 최신 가상화 기술을 배울 것입니다. 이 기존 가상화 기술은 운영체제(OS) 자체를 가상화시켜서 사용할 수 있게 해주었습니다. 가령 **Windows** 나 **MacOS** 에서 **Ubuntu Linux** 를 사용할 수 있게 해준 것입니다.

물론 윈도우에서 WSL 로 리눅스를 사용할 수 있지만, **Docker** 를 사용하면서 익히는 것을 목적으로 두었기 때문에 WSL 은 사용하지 않겠습니다. 그리고 실질적으로 **MacOS** 에서도 리눅스의 실습을 다 할 수 있지만 마찬가지로 **Docker** 를 사용하는 법을 배운다는 의미에서 **MacOS** 에서도 **Docker** 를 사용해주세요. 

<div align="center">
<img src="https://images.idgesg.net/images/article/2017/06/virtualmachines-vs-containers-100727624-large.jpg" width="70%" height="auto">
</div>

기존 가상화기술이 전체 **OS** 를 매번 새로 설치해야 하고 필요한 환경을 설정해주어야 하는 불편함이 있는 반면 도커는 위 그림과 같이 불필요한 오버헤드를 줄이고 도커 엔진으로 꼭 필요한 프로세스만을 가상화시킵니다. 그래서 도커는 기존의 가상화 기술보다 빠르고 꼭 필요한 시스템 리소스만을 사용합니다. 

<div align="center">
<img src="https://miro.medium.com/max/1400/1*p8k1b2DZTQEW_yf0hYniXw.png" width="70%" height="auto">
</div>

이렇게 가상화된 프로세스를 컨테이너라고 불리는데 컨테이너는 **Dockerfile** 이라는 별도의 파일에 모든 환경과 설치되어야 하는 패키지들을 설정하고 빌드된 이미지에서 생성됩니다. 이미지란 컨테이너 실행에 필요한 모든 파일과 설정값을 갖고 있는 모델이고, 컨테이너란 이미지를 실행시킨 것입니다. 

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82284528-2a4c9580-99d4-11ea-942d-1d37b3fc458a.PNG" width="50%" height="auto">
</div>

쉽게 말해서 이미지는 청동기 거푸집이고 컨테이너는 그 거푸집으로 제작되는 청동기 칼입니다. 다시 말해 이미지는 변하지 않는 모델이고 컨테이너는 그 이미지를 실제로 실행시킨 인스턴스입니다. 그래서 이미지를 여러번 실행해서 여러 컨테이너를 만들 수 있습니다. 또 실행된 컨테이너를 중지하여 삭제할 수도 있지만 이미지는 여전히 변하지 않기 때문에 다시 이미지로부터 컨테이너를 실행할 수 있습니다. 

> 청동기 거푸집은 ... 외국 학생은 이해 못함.

> 도커 레이어를 설명해야함.

> 도커가 시스템 리소스를 딱 필요한 만큼만 쓰는 설명해주면 좋음.

> 도커 이미지는 [도커 허브](https://hub.docker.com/)에 등록해서 다른 사람이 사용하게 할 수 있습니다. 도커 허브에는 무수히 많은 이미지들이 있습니다. **Java**, **Python**, `gcc`, **MySQL**, **postgres**, **redis**, **Ubuntu Linux**, **NodeJS**, **Nginx**, **Kali Linux** 등등 기업과 커뮤니티들이 앞다투어 자신의 프로그램을 도커 이미지로 만들고 있습니다. 

## 도커의 중요성

이 도커는 2013년 **PyCon** 에서 dotCloud 창업자인 Solomon Hykes 에 의해 **The future of Linux Containers** 에서 처음 알려졌는데, 그 유용성이 증명되면서 [마이크로소프트가 도커를 4조원에 인수하려 하기도](https://www.sdxcentral.com/articles/news/sources-microsoft-tried-to-buy-docker-for-4b/2016/06/) 했습니다.

> 특히 **Google** 에서는 모든 서비스들이 컨테이너로 동작하고 매주 20억 개의 컨테이너를 구동한다고 합니다. 또 카카오에서도 카카오톡 및 여러 서비스를 컨테이너로 운영중이고 다음(Daum), 멜론(Melon) 도 서비스를 컨테이너로 운영중이라고 합니다. 더 나아가서 어느정도 기반이 있는 기업은 도커를 디폴트로 생각한다고 해요. 그만큼 도커가 안정적이고 효율적이기 때문입니다. 아직 도커가 정확히 뭔진 모르겠지만 엄청 중요한 기술이고 배우게 되면 개발자로서 엄청 좋을 것 같습니다.

여기에서는 다른 배울 것들도 많아서 도커의 유용성과 깊은 의미에 관하여 자세히 설명하지 않을 것입니다. 하지만 **GBC** 가 끝나고 시간이 좀 남으실 때 

1. https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html

2. https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html

3. https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html

위 블로그 연재글을 읽으시면서 도커에 대하여 알아보시길 **강력하게** 추천합니다. 

## 도커 설치

> 참고/출처 : https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html

> 만약  컴퓨터 운영체제로 **Linux** 를 사용하는 분이 있다면 당신은 전세계 컴퓨터 사용자 중 **`1.63%`** 의 사용자이기 때문에 스스로 도커를 설치할 수 있다고 믿습니다. 

### Windows 도커 설치

1. 먼저 윈도우 시스템을 홈 에디션을 사용하고 있다면 에듀케이션으로 업그레이드 하셔야 합니다. 그렇지 않으면 도커 설치가 제대로 되지 않습니다. 한동대생이라면 누구든지 윈도우 에듀케이션 제품키를 무료로 제공받을 수 있기 때문에 에듀케이션으로 쉽게 버전업을 할 수 있습니다.

    - 만약 윈도우 프로를 사용하고 계시다면 도커 설치는 문제 없으니 2단계로 넘어가셔도 괜찮습니다.

    - 히즈넷에 로그인하여 [이 링크](https://hisnet.handong.edu/itsupport/software/software14_01.php) 에 접속하셔서 윈도우 10 을 클릭한 후 제품키를 무료로 구매해주세요. 

    - 그리고 윈도우 제품키를 구매한 에듀케이션 제품키로 변경하면 됩니다.

    **히즈넷에서 윈도우 업그레이드하는 방법이 좀 바뀌었음! 업데이트 필요**

2. [이 링크](https://hub.docker.com/editions/community/docker-ce-desktop-windows) 에서 도커 설치파일을 다운로드 받아서 설치하세요.

3. **Hyper-V enable &rarr; [BIOS] Intel - CPU Virtualization enable / AMD - SVM mode enable**
y(w∗⋅x)≥γ
### MacOS 도커 설치

1. 맥은 단순히 [이 링크](https://hub.docker.com/editions/community/docker-ce-desktop-mac) 에서 도커 설치파일을 다운로드 받아 설치하면 됩니다.

    - 제가 유일하게 맥에서만 직접 도커를 설치해본 경험이 없어서 무슨 장애물이 있을지 예상이 안되지만 일단 설치에 문제가 있으면 저에게 질문을 주세요.

## 도커 초간단 사용법 

도커란 세팅된 이미지를 컨테이너로 실행하는 가상화 플랫폼이라고 했습니다. 도커에 수많은 기능이 있지만 여기에서는 실습에 필요한 최소기능, 즉 컨테이너를 **(1) 실행하고 종료하고**, **(2) 컨테이너와 이미지 상태를 확인하고**, **(3) 재실행하는 방법, (4) 이미지와 컨테이너를 삭제하는 방법**을 간단히 알아보겠습니다. 

### (1) 컨테이너 실행하고 종료하기

도커를 성공적으로 설치하셨다면 터미널을 열어서 다음 명령어를 실행해봅시다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker run -it ccss17/ubuntu
```

`docker run` 명령어는 `ccss17/ubuntu` 리눅스의 이미지가 로컬에 있는지 찾고, 없으면 [도커 허브](https://hub.docker.com/)에서 찾아서 다운로드한 다음 실행까지 시켜주는 명령어입니다. 그래서 처음 실행할 때는 이미지를 다운로드하느라 시간이 좀 걸리지만 그 다음에 실행할 때부터는 곧 바로 우분투 리눅스 컨테이너로 접속되죠.

`ccss17/ubuntu` 이미지란 제가 **GBC** 를 위하여 공식 `ubuntu` 이미지 위에 필요한 패키지 등을 설치하여 만든 커스텀 이미지입니다. 공식 `ubuntu` 이미지는 기본적으로 사용자가 도커 이미지에 터미널로 접속하여 사용하지 않는다는 전제로 만들어졌기 때문에 필요없는 패키지는 과감하게 다이어트된 이미지입니다. 따라서 리눅스를 실습하기에 상당히 부적절합니다. 

> 이 이미지를 만든 소스코드, 즉 `Dockerfile` 이 궁금하다면 https://github.com/ccss17/ubuntu-unminimize/ 을 참고하면 됩니다. 

**이 커스텀 우분투 이미지의 사용자 아이디는 `ccsss` 이고 비밀번호는 `a` 입니다. 비밀번호를 기억해두세요.**

- **`docker run <OPTIONS> <IMAGE>` : 이미지를 다운로드하고 컨테이너로 실행한다.**

  - 옵션 `-it` 는 터미널로 컨테이너에 접속할 수 있게 해주는 옵션입니다.
  
  - 옵션 `--rm` 은 생성된 컨테이너를 종료했을 때 자동으로 삭제해주는 옵션입니다.
  
    - 하지만 여기에서는 `--rm` 옵션을 사용하지 않았습니다. 생성된 도커 컨테이너에서 리눅스를 실습하고 실습한 데이터가 계속 남아있게 하기 위해서입니다. 
  
컨테이너가 실행되었다면 시험삼아 지금 실행된 우분투 시스템의 버전을 확인해보겠습니다. 아직 명령어의 의미를 몰라도 됩니다. 

> `$` 는 쉘의 프롬프트, 즉 쉘에 입력된 명령어를 기다리고 있다는 뜻의 기호입니다. 그리고 `$` 오른쪽이 실제로 입력되는 명령어입니다. 프롬프트로 시작되지 않는 문장들은 명령어의 출력들입니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.4 LTS (Bionic Beaver)"
...
```

위의 실행결과를 보니 우분투 `18.04` 버전이네요. 이제 파일 하나를 생성해보겠습니다. 마찬가지로 명령어 의미를 모르셔도 됩니다.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ touch test.txt
```

위 명령어는 `test.txt` 파일을 생성합니다. 그리고 `ls` 명령어를 실행해보면 파일 목록 중에 `test.txt` 파일이 생성되어 있음을 알 수 있습니다.

이제 컨테이너를 종료해봅시다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ exit 
```

잘 따라오셨다면 다음과 같이 진행되었을 겁니다.

<div align="center">
<img src="https://user-images.githubusercontent.com/16812446/82790721-7f424d00-9ea7-11ea-9755-b32747a2d310.gif" width="70%" height="auto">
</div>

### (2) 컨테이너와 이미지 상태 확인하기

이제 `docker images` 명령어를 실행해봅시다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker images
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
ccss17/ubuntu              latest              1d622ef86b13        8 days ago          73.9MB
...
```

이 명령어는 로컬에 다운로드된 도커 이미지의 목록을 출력해줍니다. 도커를 처음 실행해보신 분들은 아마 이미지가 `ccss17/ubuntu` 밖에 없을 겁니다. 이 이미지들이 실행되기만을 기다리는 컨테이너의 모델들입니다. 이 이미지를 실행하여 컨테이너로 만들고 컨테이너에서 아무리 난리를 쳐도 이미지는 변하지 않습니다. 

- **`docker images` : 로컬에 다운로드된 도커 이미지 목록을 출력한다.**

이제 다음 명령어를 실행해보세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker ps -a
CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS                    PORTS               NAMES
3a1998563b0e        ccss17/ubuntu             "/bin/bash"              3 seconds ago       Exited (0) 1 second ago                       distracted_shirley
...
```

실행한 결과는 위와 같은데 이미지 이름이 `ccss17/ubuntu` 인걸로 보아 우리가 방금 실행했던 우분투 컨테이너라는 것을 알 수 있네요. `docker ps` 는 컨테이너의 목록을 출력합니다. 옵션 `-a` 를 붙혀서 실행하면 종료된 컨테이너까지 출력되는데, 우리가 방금 실행했던 컨테이너는 종료가 되버렸기 때문에 `-a` 를 붙히지 않으면 출력되지 않습니다. 

- **`docker ps <OPTIONS>` : 도커 컨테이너 목록을 출력한다.**

  - `-a` 옵션을 붙히면 종료된 컨테이너도 출력된다.

종료된 컨테이너는 언제든지 다시 실행될 수 있고 이전에 작업한 데이터들이 남아있는 상태입니다. 도커를 처음 설치하고 실행하신 분들은 `ccss17/ubuntu` 컨테이너밖에 출력되지 않을 겁니다. 

### (3) 종료된 컨테이너 재실행하기

이제 다음 명령어로 종료시켰던 `ubuntu` 컨테이너를 다시 실행해보세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker start -ai 3a1998563b0e
```

이때 중요한 것은 `3a1998563b0e` 의 값은 컨테이너 아이디로써 사람마다 다를 수 있습니다. 이 값에는 `docker ps -a` 명령어로 확인했었던 `ccss17/ubuntu` 컨테이너의 아이디를 대입해주세요. 그러면 종료되었던 컨테이너를 재실행 할 수 있습니다. 

- **`docker start <OPTIONS> <CONTAINER>` : 종료된 컨테이너를 다시 실행한다.**

  - 컨테이너 아이디로 `3a1998563b0e` 를 전부 다 입력했지만 사실은 만약 컨테이너 구별만 될 수 있다면

    ```shell
    docker start -ai 3
    ```
  
    와 같이 `3` 만 입력해도 됩니다. 하지만 또 다른 컨테이너의 아이디어 맨 앞자리가 `3` 이라면 구별이 안되기 때문에 `3a` 를 입력해야 합니다.

  - `-ai` 옵션으로 컨테이너에 접속하여 터미널처럼 사용할 수 있게 됩니다.

  - 자세한 설명과 그 이외의 옵션이 궁금하신 분들은 https://docs.docker.com/engine/reference/commandline/start/ 를 참고하세요.

이제 우분투 컨테이너에 접속되었다면 다음 명령어를 실행하세요.

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ ls
test.txt
```

그러면 위와 같이 조금 전에 생성했었던 `test.txt` 파일이 그대로 잘 남아있는 것을 확인할 수 있네요. 컨테이너가 종료되어도 다시 실행하니까 작업했던 데이터가 남아있어서 다행입니다.

### (4) 컨테이너와 이미지 삭제하기 

이제 필요가 없어진 컨테이너와 이미지를 삭제해보겠습니다. 먼저 다시 `exit` 명령어를 입력하여 컨테이너를 빠져나와주세요. 그런 다음 명령어를 입력하여 도커의 컨테이너 아이디를 확인합니다. 그리고 그 아이디를 `docker rm` 의 파라미터로 전달합니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker ps -a
$ docker rm 3a1998563b0e
```

- **`docker rm <OPTIONS> <CONTAINER>` : 컨테이너를 삭제한다.**

  - 컨테이너 아이디로 `3a1998563b0e` 를 전부 다 입력했지만 사실은 만약 컨테이너 구별만 될 수 있다면

    ```shell
    docker rm 3
    ```
  
    와 같이 `3` 만 입력해도 됩니다. 

이제 우리가 만들었던 `test.txt` 와는 영원한 작별을 하게 되었습니다. 컨테이너가 삭제되었기에 그 파일은 다시는 찾아볼 수 없습니다. 이제 다음의 명령어로 이미지를 삭제해보겠습니다. 

> 하지만 앞으로 실습을 이 `ccss17/ubuntu` 이미지로 진행할텐데 다운로드 시간이 약간 오래 걸리기 때문에 이미지를 삭제하는 실습은 나중에 해도 됩니다. 

##### **<div align="center"> ⬇ EXECUTE! ⬇ </div>**

```shell
$ docker rmi ccss17/ubuntu
```

그러면 다운로드 받았던 `ccss17/ubuntu` 가 삭제됩니다. 

- **`docker rmi <OPTIONS> <CONTAINER>` : 이미지를 삭제한다.**

# 도커 요약 

| 도커 명령어 | 하는 일 |
|:---|:---|
| **`docker run <OPTIONS> <IMAGE>`** | 이미지를 다운로드하고 컨테이너로 실행한다. |
| **`docker images`** | 로컬에 다운로드된 도커 이미지 목록을 출력한다.|
| **`docker ps <OPTIONS>`** | 도커 컨테이너 목록을 출력한다.|
| **`docker start <OPTIONS> <CONTAINER>`** | 종료된 컨테이너를 다시 실행한다. |
| **`docker rm <OPTIONS> <CONTAINER>`** | 컨테이너를 삭제한다.|
| **`docker rmi <OPTIONS> <CONTAINER>`** | 이미지를 삭제한다.|

## **<div align="center"> 🌜 ️여기까지 Day1 내용입니다. 수고하셨습니다. 🌜️ </div>**