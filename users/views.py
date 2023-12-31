from django.utils import timezone
from http import HTTPStatus
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Account
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django import http
import requests
from django.db import transaction
from django.db.models import Q

from users import models


@csrf_exempt
def UpdateUser(request, user_id):
    if request.method == "PATCH":
        try:
            user = get_object_or_404(Account, uuid=user_id)
            data = json.loads(request.body)
            new_username = data.get("username")
            new_email = data.get("email")
            new_password = data.get("password")
            new_description = data.get("description")
            new_short_description = data.get("short_description")
            new_avatar_url = data.get("avatar_url")
            new_background_url = data.get("background_url")
            new_gender = data.get("gender")
            new_birthday = data.get("birthday")
            new_school_faculty = data.get("school_faculty")
            new_school_majors = data.get("school_majors")
            new_school_name = data.get("data_school_name")
            new_role = data.get("role")
            # save
            if new_username:
                user.username = new_username
            if new_email:
                user.email = new_email
            if new_password:
                user.password = new_password
            if new_gender:
                user.gender = new_gender
            if new_birthday:
                user.birthday = new_birthday
            if new_role:
                user.role = new_role
            if new_description:
                user.description = new_description
            if new_short_description:
                user.short_description = new_short_description
            if new_avatar_url:
                user.avatar_url = new_avatar_url
            if new_background_url:
                user.background_url = new_background_url
            if new_school_faculty:
                user.school_faculty = new_school_faculty
            if new_school_majors:
                user.school_majors = new_school_majors
            if new_school_name:
                user.school_name = new_school_name
            user.createdAt = timezone.now()
            user.updateAt = timezone.now()

            user.save()
            response_data = {
                "status": HTTPStatus.OK,
                "message": "Update successfully",
                "serviceName": "USERSERVICE",
                "body": {
                    "data": {
                        "message": "User updated successfully",
                        "id": user.id,
                        "name": user.username,
                        "email": user.email,
                        "description": user.description,
                        "short_description": user.short_description,
                        "avatar_url": user.avatar_url,
                        "background_url": user.background_url,
                        "follower": user.follower,
                        "following": user.following,
                        "gender": user.gender,
                        "birthday": user.birthday,
                        "facebook": user.facebook,
                        "instagram": user.instagram,
                        "twitter": user.twitter,
                        "school_name": user.school_name,
                        "school_faculty": user.school_faculty,
                        "school_majors": user.school_majors,
                        "role": user.role,
                        "createAt": user.createdAt,
                        "updateAt": user.updateAt,
                    },
                }
            }
        except Exception as e:
            # Xử lý lỗi nếu có
            response_data = {
                "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                "message": "Internal Server Error",
                "serviceName": "UsersService",
                "body": {"data": False, "error": str(e)},
            }
        return JsonResponse(response_data, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse(
            {"error": "Invalid request method"}, status=HTTPStatus.BAD_REQUEST
        )


@csrf_exempt
def Delete_user(request, user_id):
    try:
        user = get_object_or_404(Account, id=user_id)
        if request.method == "DELETE":
            user.delete()
            response_data = {
                "status": HTTPStatus.OK,
                "mess": "Deleted successfully",
                "body": {"data": {}},
            }
        else:
            response_data = {
                "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                "mess": "internal server error",
                "body": {"error": "internal server error"},
            }
    except Account.DoesNotExist:
        response_data = {
            "status": HTTPStatus.NOT_FOUND,
            "mess": "User not found",
            "body": {"error": "not found"},
        }

    return JsonResponse(response_data, status=response_data["status"])


@csrf_exempt
def SearchUser(request):
    try:
        keyword = request.GET.get("keyword", "")
        user = Account.objects.filter(
            Q(id__icontains=keyword) | Q(email__icontains=keyword)
        ).first()
        if user is not None:
            response_data = {
                "status": HTTPStatus.OK,
                "mess": "Success",
                "serviceName": "USERSERVICE",
                "body": {
                    "data": {
                        "id": user.id,
                        "name": user.username,
                        "email": user.email,
                        "description": user.description,
                        "short_description": user.short_description,
                        "avatar_url": user.avatar_url,
                        "background_url": user.background_url,
                        "follower": user.follower,
                        "following": user.following,
                        "gender": user.gender,
                        "birthday": user.birthday,
                        "facebook": user.facebook,
                        "instagram": user.instagram,
                        "twitter": user.twitter,
                        "school_name": user.school_name,
                        "school_faculty": user.school_faculty,
                        "school_majors": user.school_majors,
                        "role": user.role,
                        "createAt": user.createdAt,
                        "updateAt": user.updateAt,
                    },
                },
            }
        else:
            response_data = {
                "status": HTTPStatus.NOT_FOUND,
                "mess": "User not found",
                "body": {"error": "not found"},
            }
        return JsonResponse(response_data, status=HTTPStatus.OK)
    except:
        response_data = {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "mess": "internal server error",
            "serviceName": "USERSERVICE",
            "body": {"error": "internal server error"},
        }
    return JsonResponse(response_data, status=response_data["status"])


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            gender = data.get("gender")
            birthday = data.get("birthday")
            role = data.get("role")

            # type:{}
            # Kiểm tra nếu có dữ liệu bị thiếu
            if None in [username, password, email, gender, birthday, role]:
                response_data = {
                    "status": HTTPStatus.BAD_REQUEST,
                    "mess": "bad request",
                    "serviceName": "USERSERVICE",
                    "body": {"data": False, "error": "bad request"},
                }
                return JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)

            user = Account(
                username=username,
                password=password,
                email=email,
                gender=gender,
                birthday=birthday,
                role=role,
            )
            user.save()

            response_data = {
                "status": HTTPStatus.CREATED,
                "mess": "register successfully",
                "serviceName": "USERSERVICE",
                "body": {
                    "data": {
                        "message": "User updated successfully",
                        "id": user.id,
                        "name": user.username,
                        "email": user.email,
                        "description": user.description,
                        "short_description": user.short_description,
                        "avatar_url": user.avatar_url,
                        "background_url": user.background_url,
                        "follower": user.follower,
                        "following": user.following,
                        "gender": user.gender,
                        "birthday": user.birthday,
                        "facebook": user.facebook,
                        "instagram": user.instagram,
                        "twitter": user.twitter,
                        "school_name": user.school_name,
                        "school_faculty": user.school_faculty,
                        "school_majors": user.school_majors,
                        "role": user.role,
                        "createAt": user.createdAt,
                        "updateAt": user.updateAt,
                    }
                }
            }

            return JsonResponse(response_data, status=HTTPStatus.CREATED)

        except Exception as e:
            # Xử lý lỗi nếu có
            response_data = {
                "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                "mess": "Internal Server Error",
                "serviceName": "UsersService",
                "body": {"data": False, "error": str(e),"error":"lorservice try_except"},

            }
            return JsonResponse(response_data, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse(
            {"error": "Invalid request method"}, status=HTTPStatus.BAD_REQUEST
        )


def GetAuthenticatedUser(request, u_email):
    try:
        user = get_object_or_404(Account, email=u_email)
        if request.method == "POST":
            if user is not None:
                response_data = {
                "status": HTTPStatus.OK,
                "mess": "SUCCESSFULLY",
                "serviceName": "USERSERVICE",
                "body": {
                    "data": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "gender": user.gender,
                        "password": user.password,
                        "role": user.role,
                        "birthday": user.birthday,
                    },
                }
            }
        else:
            response_data = {
                "status": HTTPStatus.NOT_FOUND,
                "mess": "User not found",
                "body": {"error": "not found"},
            }
        return JsonResponse(response_data, status=HTTPStatus.OK)
    except:
        response_data = {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "mess": "internal server error",
            "serviceName": "USERSERVICE",
            "body": {"error": "internal server error"},
        }
    return JsonResponse(response_data, status=response_data["status"])


def GetProfile(request, user_id):
    try:
        user = get_object_or_404(Account, id=user_id)
        if request.method == "POST":
            if user is not None:
                response_data = {
                    "status": HTTPStatus.OK,
                    "mess": "SUCCESSFULLY",
                    "serviceName": "USERSERVICE",
                    "body": {
                        "data": {
                            "id": user.id,
                            "avatar_url": user.avatar_url,
                            "gender": user.gender,
                            "birthday": user.birthday,
                            "background_url": user.background_url,
                            "school": {
                                "school_name": user.school_name,
                                "school_faculty": user.school_faculty,
                                "school_majors": user.school_majors,
                            },
                            "description": user.description,
                            "short_description": user.short_description,
                            "social": {
                                "facebook": user.facebook,
                                "instagram": user.instagram,
                                "twitter": user.twitter,
                            },
                            "follower": user.follower,
                            "following": user.following,
                            "createAt": user.createdAt,
                            "updateAt": user.updateAt,
                        },
                    },
                }
            else:
                response_data = {
                    "status": HTTPStatus.NOT_FOUND,
                    "mess": "User not found",
                    "body": {"error": "not found"},
                }
            return JsonResponse(response_data, status=HTTPStatus.OK)
    except:
        response_data = {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "mess": "internal server error",
            "serviceName": "USERSERVICE",
            "body": {"error": "internal server error"},
        }
    return JsonResponse(response_data, status=response_data["status"])
