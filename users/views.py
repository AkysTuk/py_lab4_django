from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Створення користувача
@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    data = json.loads(request.body)
    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        age=data["age"]
    )
    return JsonResponse({"id": user.id}, status=201)

# Отримання користувача
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({"username": user.username, "email": user.email, "age": user.age})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

# Оновлення користувача
@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = json.loads(request.body)
        user.username = data["username"]
        user.email = data["email"]
        user.age = data["age"]
        user.save()
        return JsonResponse({"id": user.id})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

# Видалення користувача
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({"message": "User deleted"}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)