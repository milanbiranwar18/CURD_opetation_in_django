import json
from django.http import JsonResponse
from user.models import User


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
