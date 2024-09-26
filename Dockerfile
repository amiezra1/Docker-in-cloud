FROM python:3.11-slim

WORKDIR /app

COPY main.py /app/
COPY components.py /app/
COPY config.json /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]