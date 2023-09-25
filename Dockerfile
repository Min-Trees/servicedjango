# Sử dụng hình ảnh Python 3.10-slim làm hình ảnh cơ sở
FROM python:3.10-slim

# Đặt biến môi trường để đầu ra Python không bị đệm
ENV PYTHONUNBUFFERED True

# Đặt thư mục làm việc của container là /app
ENV APP_HOME /app
WORKDIR $APP_HOME

# Sao chép tệp requirements.txt từ thư mục gốc của dự án vào /app trong container
COPY requirements.txt .

# Sao chép toàn bộ mã nguồn vào /app trong container
COPY . .
RUN pip install --upgrade pip
# Cài đặt các phụ thuộc sản xuất từ tệp requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng bằng gunicorn
CMD ["gunicorn", "project_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]
