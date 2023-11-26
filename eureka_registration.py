import requests
import json

# Địa chỉ IP và cổng của Eureka Server
eureka_server_url = "https://tdmu-discovery-service.onrender.com/eureka/"

# URL của dịch vụ Django của bạn
django_service_url = "http://localhost:8000"

# Headers cho request POST
headers = {'Content-Type': 'application/json'}
# Dữ liệu đăng ký dịch vụ
eureka_payload = {
    "instance": {
        "hostName": "localhost",
        "app": "USER-SERVICE",
        "ipAddr": "10.220.9.136",  # Địa chỉ IP của Eureka Server
        "vipAddress": "USER-SERVICE",
        "secureVipAddress": "USER-SERVICE",
        "status": "UP",
        "port": {"$": 8000, "@enabled": "true"},
        "securePort": {"$": 8443, "@enabled": "false"},
        "homePageUrl": f"{django_service_url}/",
        "statusPageUrl": f"{django_service_url}/status",
        "healthCheckUrl": f"{django_service_url}/health",
        "dataCenterInfo": {"@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo", "name": "MyOwn"}
    }
}

# Thực hiện request POST đến Eureka Server
response = requests.post(f"{eureka_server_url}apps/{eureka_payload['instance']['app']}", data=json.dumps(eureka_payload), headers=headers)

if response.status_code == 204:
    print("Đăng ký dịch vụ thành công.")
else:
    print(f"Không thể đăng ký dịch vụ. Phản hồi: {response.text}")
