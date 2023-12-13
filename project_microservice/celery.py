from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Thiết lập môi trường mặc định của 'celery' cho chương trình 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_microservice.settings')

# Tạo một đối tượng Celery và cấu hình nó sử dụng các cài đặt từ Django.
app = Celery('project_microservice')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tải các mô-đun nhiệm vụ từ tất cả các cấu hình ứng dụng Django đã đăng ký.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
