FROM python:3.9

ENV USER memotion_app
ENV TZ Asia/Tokyo

SHELL [ "/bin/bash", "-c" ]
RUN useradd -m ${USER} -u 1000 -s /bin/bash

USER ${USER}
WORKDIR /home/${USER}

ENV PATH $PATH:/home/${USER}/.local/bin
RUN pip install --upgrade pip --user \
    && pip install --upgrade setuptools --user
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH $PATH:/home/${USER}/.poetry/bin
RUN poetry config virtualenvs.in-project true

USER root
RUN poetry completions bash | tee /etc/bash_completion.d/poetry.bash-completion

USER ${USER}
WORKDIR /usr/src
