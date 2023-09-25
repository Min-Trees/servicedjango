FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /project_microservice
COPY requirements.txt /project_microservice/requirements.txt
COPY . /project_microservice
RUN pip install -r requirements.txt
RUN pip install gunicorn==20.1.0
CMD ["gunicorn", "-b", ":8000", "--workers", "4", "--timeout", "60", "users:app"]
