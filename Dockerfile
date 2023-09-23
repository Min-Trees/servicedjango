FROM python:3.9
ENV PYTHONNUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install  -r requirements.txt
COPY . /app
RUN pip install gunicorn
CMD ["gunicorn", "project_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]