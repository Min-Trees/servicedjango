from http import HTTPStatus
from django.shortcuts import render
from django.views import View
from .models import Account, AccountProfile
from .serializers import AccountSerializer, ProfileSerializer
from rest_framework import  generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django import http
import requests
# Create your views here.

'''class UserView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer'''

class UserViewDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #search user by userId
    lookup_field = 'email'
class deleteUserView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #search user by userId
    lookup_field = 'id'
class Profile(generics.RetrieveAPIView):
    queryset = AccountProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id' 

@csrf_exempt
def getUser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            gender = data.get('gender')
            birthday = data.get('birthday')
            role = data.get('role')
            
            # Kiểm tra nếu có dữ liệu bị thiếu
            if None in [id, username, password, email, gender, birthday, role]:
                response_data = {
                    'status': HTTPStatus.BAD_REQUEST,
                    'mess': '',
                    'serviceName': 'USERSERVICE',
                    'body': {
                        'data': None,
                        'error': 'Data is incomplete or null.'
                    }
                }
                return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)

            user = Account( username=username, password=password, email=email, gender=gender, birthday=birthday, role=role)
            user.save()
            response_data = {
                'status': HTTPStatus.CREATED,
                'message': 'Created',
                'serviceName': 'USERSERVICE',
                'body': {
                    'data': {
                        'message': 'Data received and saved successfully',
                        'id': user.id,
                        'name': user.username,
                        'email': user.email,
                        'gender': user.gender,
                        'birthday': user.birthday,
                        'role': user.role
                    },
                    'error': 'NULL'
                }
            }
            return JsonResponse(response_data, status=HTTPStatus.CREATED)
        except Exception as e:
            # Xử lý lỗi nếu có
            response_data = {
                'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                'message': 'Internal Server Error',
                'serviceName': 'UsersService',
                'body': {
                    'data': None,
                    'error': str(e)
                }
            }
            return JsonResponse(response_data, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=HTTPStatus.BAD_REQUEST)
def getProfile(requests):
    profile_api ="http://auth-service-api/" # link api profile
    response = requests.get(profile_api)

    if response.status_code == 200:
        profile_data = response.json()
        profile = AccountProfile(userID = profile_data['userID'],userAvt = profile_data['userAvt'], userBackGround = profile_data['userBackGround'])
        profile.save()

        return JsonResponse({'message' : 'Profile data saved successfully'}, status = 200)

    else:
        return JsonResponse({'error' : 'Unable to fetch user data from Profile Service'})

