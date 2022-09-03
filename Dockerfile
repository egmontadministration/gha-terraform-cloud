FROM python:3.10-buster

ENV IS_DOCKER_ENVIRONMENT=true

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

CMD [ "python", "./main.py" ]