FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /project_microservice
COPY requirements.txt /project_microservice/
COPY . /project_microservice
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn==20.1.0
ENTRYPOINT [ "gunicorn", "project_microservice.wsgi"]
