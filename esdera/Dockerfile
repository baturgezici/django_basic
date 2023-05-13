FROM python:3.10

WORKDIR /esdera

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8083

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8083" ]