# How to make linux 64 bit executables run on an M1 Mac, or why you made the wrong choice

## Instructions

We're assuming you installed `docker` through Docker Desktop. If not, go [install
it](https://www.docker.com/products/docker-desktop) now.

First, go to `~/.docker/config.json` and add the following line at the end
```json
{
    ...
    "experimental": "enable"
}
```
Remember to add a coma to the previous entry if it didn't have one.

Now, to check that everything is working, run 
```shell
docker buildx ls
```
You should get a list of the architectures supported (which should include `linux/amd64`).

From here onwards, just download this [`Dockerfile`](https://raw.githubusercontent.com/polygl0ts/bambi-meetings/master/guides/Dockerfile) and place it in the 
directory where you'll be doing your hacking (We'll be using here `~/Desktop/polygl0ts`)

Now, go to the directory where you stored the `Dockerfile` and run the following
commands

```shell
docker buildx build --platform linux/arm/v7 -t linux-amd64 .
```
And with that, you have a Docker image with which to run linux 64-bit binaries.

Now, to use it, you need to run a container. Assuming you have the directory
where all the hacking stuff is stored in `$HACKING_DIR` (If this is not true,
just replace it with the directory itself), run the following command to spin
the container up.
```shell
docker run -it -d --rm -v "$HACKING_DIR:/ctf" linux-amd64
```
and this comand to connect to it.
```shell
docker exec -it $(docker ps -l -q) "/bin/bash"
```

## Tips and tricks

You can add this lines of code at the end of your `.zshrc` or `.bashrc` to 
more conveniently enter your container.

```bash
HACKING_DIR="~/Desktop/polygl0ts"
linux64(){
    docker run -it -d --rm -v "$HACKING_DIR:/ctf" linux-amd64
    docker exec -it $(docker ps -l -q) "/bin/bash"
}
```

## Commands to run

Heh, you lazy fucker. 

At least install docker.

```shell
# 1. Enable experimental features in docker
ed ~/.docker/config.json << EOF
G
k
i
,
    "experimental": "enabled"
.
.-2,.-1j
w
q
EOF
read -p "I understand that I should never run what I've copy-pasted from the internet"

# 2. Get the Dockerfile
export HACKING_DIR="~/Desktop/polygl0ts"
mkdir -p $HACKING_DIR
wget downloadlink -o "$HACKING_DIR/Dockerfile"
read -p "I know what all of these commands are doing, and run them at my own risk"

# 3. Build the image
cd "$HACKING_DIR"
docker buildx build --platform linux/amd64 -t linux-amd64 .
read -p "I will never again buy a Mac, for I know what pain it brings me"

# 4. Shortcut to connect to the docker container
cat >> "~/.zshrc" << EOF
export HACKING_DIR="~/Desktop/polygl0ts"
linux64(){
    docker run -it -d --rm -v "$HACKING_DIR:/ctf" linux-amd64
    docker exec -it $(docker ps -l -q) "/bin/bash"
}
source ~/.zshrc
EOF
cat << EOF
Usage:

  $ linux64

  Pops a shell in the linux container, at the $HACKING_DIR directory
EOF
```
