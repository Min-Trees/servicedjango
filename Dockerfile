FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip
RUN apt-get update
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn==20.1.0
COPY . /app
ENTRYPOINT [ "gunicorn", "project_microservice.wsgi"]
