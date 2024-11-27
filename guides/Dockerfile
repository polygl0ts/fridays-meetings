FROM ubuntu:20.04

# Install apt packages
RUN dpkg --add-architecture i386 && apt update && \
	DEBIAN_FRONTEND=noninteractive apt install -y \
	git \
	nasm \
	# python \
	# python-pip \
	# python-dev \
	# python-setuptools \
	# python-capstone \
	# python-z3 \
	# python-pycryptodome \
	# python-gmpy2 \
	# python-requests \
	python3 \
	python3-pip \
	python3-dev \
	python3-setuptools \
	python3-capstone \
	python3-pycryptodome \
	python3-gmpy2 \
	python3-requests \
	build-essential \
	libssl-dev \
	libffi-dev \
	libgmp3-dev \
	libmpc-dev \
	vim \
	htop \
	libc6-dbg \
	libc6-dbg:i386 \
	gcc-multilib \
	gdb-multiarch \
	strace \
	ltrace \
	tmux \
	wget \
	curl \
	glibc-source \
	cmake \
	socat \
	netcat \
	ruby \
	ruby-dev \
	musl-dev \
	musl-tools \
	cpio \
	qemu-system && \
	apt clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    cd ~ && tar -xvf /usr/src/glibc/glib*.tar.xz && \
    echo 'dir ~/glibc-2.27/malloc' >> ~/.gdbinit

# Install pwntools
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade pwntools

# Install other python tools
RUN pip3 install ropper keystone-engine

# Install ruby tools
RUN gem install \
	seccomp-tools \
	one_gadget

# # Install pwndbg
# RUN cd ~ && git clone https://github.com/pwndbg/pwndbg && cd ~/pwndbg && \
# 	./setup.sh && \
# 	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install gef
RUN wget -O ~/.gdbinit-gef.py -q https://github.com/hugsy/gef/raw/master/gef.py && \
	echo 'source ~/.gdbinit-gef.py' >> ~/.gdbinit

RUN wget -O ~/extract-vmlinux -q \
	https://raw.githubusercontent.com/torvalds/linux/master/scripts/extract-vmlinux && \
	chmod +x ~/extract-vmlinux

# COPY ./exploit.py /root/exploit.py
RUN mkdir /ctf
# COPY ./.vimrc /root/.vimrc
COPY ./exploit.py /ctf/exploit.py

# Random settings
RUN echo 'set editing-mode vi' > ~/.inputrc

ENV LANG C.UTF-8

WORKDIR /ctf
