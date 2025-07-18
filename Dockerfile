FROM python:3.10-alpine

WORKDIR /app

COPY requirements/backend.in requirements-frozen.txt

RUN pip install -r requirements-frozen.txt

COPY . .

CMD ["python", "spaceship/main.py"]