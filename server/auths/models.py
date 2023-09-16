import json
import re
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


@csrf_exempt
def auths_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
                response_data = {'message': 'Authorized',
                                 'user_id': user.id, 'username': user.username}
                return JsonResponse(response_data, status=200)
            else:
                response_data = {'message': 'Unauthorized'}
                return JsonResponse(response_data, status=401)
        except User.DoesNotExist:
            response_data = {'error': 'ERROR AUTH'}
            return JsonResponse(response_data, status=404)
    else:
        response_data = {'error': 'Method Not Allowed'}
        return JsonResponse(response_data, status=405)


@csrf_exempt
def registry_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'This user already exists'}, status=401)
        if not validation_username(username):
            return JsonResponse({'error': 'Incorrect username'}, status=401)
        password = data['password']
        try:
            validate_password(password, username)
        except:
            return JsonResponse({'error': 'Weak password: min length - 8 letters'}, status=401)
        password_check = data['password_check']
        if password == password_check:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            return JsonResponse({'message': 'Registration Was Successful'}, status=200)
        else:
            return JsonResponse({'message': "Passwords Don't Match"}, status=401)
    else:
        response_data = {'error': 'Method Not Allowed'}
        return JsonResponse(response_data, status=405)


@csrf_exempt
def validation_username(username):
    min_length = 4
    if len(username) < min_length:
        return False
    pattern = r"^[a-z0-9@_\.]+$"
    if re.match(pattern, username.lower()):
        return True
    return False
