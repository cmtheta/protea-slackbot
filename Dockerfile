FROM python:3.10.8-bullseye

ENV PROJECT_DIR workspace
WORKDIR /${PROJECT_DIR}

RUN apt update \
 && apt upgrade -y

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /${PROJECT_DIR}
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "-m", "slackbot" ]
