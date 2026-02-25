from python:3.9

workdir /app

copy . .

run pip install -r requirements.txt

expose 5000

cmd ["python","app.py"]

