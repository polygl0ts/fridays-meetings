FROM dockershelf/latex:basic

# Minted + Pygments
RUN apt-get update \
    && apt-get install -qy python3 python3-pip python3-setuptools python3-pygments wget xz-utils latexmk \
    && rm -rf /var/lib/apt/lists/*
RUN tlmgr init-usertree
#RUN tlmgr option repository ftp://tug.org/historic/systems/texlive/2019/tlnet-final
RUN tlmgr install minted drawstack ulem
RUN chmod -R 777 /root
ENV TEXMFHOME=/root/texmf


# Install Custom Theme
RUN mkdir /root/flagbot-pygments
COPY flagbot-pygments/ /root/flagbot-pygments
RUN ls -la /root/ && cd /root/flagbot-pygments && python3 setup.py install