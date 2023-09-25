FROM python:3.10.5-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY /project/project_microservice/requirements.txt .
COPY . .


# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "project_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]