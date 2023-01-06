import json
from django.http import JsonResponse
from user.models import User
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render
from  rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

def create(request):
    """
    Function for create user
    """
    request_dict = json.loads(request.body)
    if request.method == "POST":
        user = User.objects.create(user_name=request_dict.get("user_name"))
        return JsonResponse({"Message": "user created", "data": {"id": user.id, "user_name": user.user_name}})
    return JsonResponse({"Message": "Invalid Method"})


def update(request):
    """
    Function for update user
    """
    request_dict = json.loads(request.body)
    if request.method == "PUT":
        id = request_dict.get("id")
        user = User.objects.get(id=id)
        user.user_name = request_dict.get("user_name")
        user.save()
        return JsonResponse({"Message": "user updated", "data": {"id": user.id, "user_name": user.user_name}})
    return JsonResponse({"Message": "Invalid Method"})


def get(request):
    """
    Function for get users
    """
    if request.method == "GET":
        users = User.objects.all()
        return JsonResponse({"Message": "All users are",
                             "data": [{"id": q.id, "user": q.user_name} for q in users]})
    return JsonResponse({"Message": "Invalid Method"})


def delete(request):
    """
    Function for delete user
    """
    request_dict = json.loads(request.body)
    if request.method == "DELETE":
        id = request_dict.get("id")
        User.objects.get(id=id).delete()
        return JsonResponse({"Message": "user deleted"})
    return JsonResponse({"Message": "Invalid Method"})


class MyView(View):
    name = 'milan'

    def get(self, request):
        return HttpResponse('Good morning')
        #return HttpResponse(self.name)


class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})


