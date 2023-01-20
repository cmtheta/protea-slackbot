FROM python:3.10.8-bullseye

ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
ARG PASSWORD=user

ENV PROJECT_DIR workspace
WORKDIR /${PROJECT_DIR}

RUN apt update \
 && apt upgrade -y

RUN apt install -y sudo

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /${PROJECT_DIR}
RUN pip3 install --no-cache-dir -r requirements.txt

RUN groupadd -g ${GID} ${USERNAME} \
 && useradd -m -s /bin/bash -u ${UID} -g ${GROUPNAME} ${USERNAME} \
 && echo ${USERNAME}:${PASSWORD} | chpasswd \
 && echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN chown -R ${USERNAME}:${GROUPNAME} /${PROJECT_DIR}

USER ${USERNAME}
