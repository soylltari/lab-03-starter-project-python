FROM python:3.10-bullseye

COPY . .

RUN pip install -r requirements/backend.in

CMD ["python", "spaceship/main.py"]