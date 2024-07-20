FROM python:3.9-slim

WORKDIR /app

COPY web/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web /app

CMD ["python", "app.py"]