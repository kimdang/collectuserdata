FROM python:3.7-slim

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

## command to start docker image
ENTRYPOINT ["./run.sh"]
