FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN pip install gunicorn==20.1.0
CMD ["gunicorn", "project_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]
