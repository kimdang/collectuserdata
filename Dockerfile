from python:3.7-slim 
## we start from python
copy . . 
## copy all the code from current folder to Docker image
run pip3 install -r requirements.txt 
## install required libraries
run mkdir logs
run mkdir static

## command to start docker image
ENTRYPOINT ["./run.sh"]
