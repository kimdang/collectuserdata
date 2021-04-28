from python:3.7-slim 
## we start from python
copy . . 
## copy all the code from current folder to Docker image
run pip3 install -r requirements.txt 
## install required libraries
entrypoint ["python3", "manage.py", "runserver", "0.0.0.0:8080"] 
## command to start docker image