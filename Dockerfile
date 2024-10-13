FROM python:3.9-slim

RUN pip install --no-cache-dir opencv-python-headless

COPY . /app

WORKDIR /app

CMD ["python", "app.py"]