FROM python:alpine

WORKDIR /usr/src/app

ADD main.py requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER 1001

CMD [ "python", "/usr/src/app/main.py" ]
