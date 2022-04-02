FROM python:3.8.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirments.txt

CMD [ "python3", "app.py"]