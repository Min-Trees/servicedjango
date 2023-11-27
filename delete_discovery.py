import requests

eureka_server_url = "https://tdmu-discovery-service.onrender.com/eureka/"
service_name = "USER-SERVICE"  # Thay thế bằng tên của dịch vụ bạn muốn xóa

response = requests.delete(f"{eureka_server_url}apps/{service_name}")

if response.status_code == 200:
    print(f"Xóa dịch vụ {service_name} thành công.")
else:
    print(f"Không thể xóa dịch vụ {service_name}. Phản hồi: {response.text}")
