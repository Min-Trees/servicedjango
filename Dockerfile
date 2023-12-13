FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV ALLOWED_HOSTS localhost,example.com
ENV DJANGO_PORT 8080
# Set working directory
WORKDIR /app
# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy the rest of the application code
COPY . /app
# CMD to start the Django development server
CMD python manage.py runserver 0.0.0.0:$DJANGO_PORT

