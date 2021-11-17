FROM python:latest

RUN mkdir /vendingmachine

WORKDIR /vendingmachine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]