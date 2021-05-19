from python:3.7-slim

cp requirements.txt .

run pip3 install -r requirements.txt

copy . .

## command to start docker image
entrypoint ["./run.sh"]
