FROM python:3.10-alpine3.16

WORKDIR /my-code

COPY requirements.txt requirements.txt

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]