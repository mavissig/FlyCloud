from django.db import models
from django.contrib.auth.models import User
from django.http.response import JsonResponse


def session_check(request):
    if request.user.is_authenticated:
        return JsonResponse({'message': 'Yeeeees'}, status=200)
    else:
        return JsonResponse({'message': 'No'}, status=401)


def debug_resp(request):
    return JsonResponse({'message': '[DEBUG_RESP]'}, status=201)
