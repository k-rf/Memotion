FROM node:14

ENV USER memotion_web
ENV TZ Asia/Tokyo

SHELL [ "/bin/bash", "-c" ]
RUN useradd -m ${USER} -s /bin/bash

USER ${USER}
WORKDIR /usr/src