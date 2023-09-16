import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@csrf_exempt
def auths_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                response_data = {'message': 'Authorized'}
                return JsonResponse(response_data, status=200)
            else:
                response_data = {'message': 'Unauthorized'}
                return JsonResponse(response_data, status=401)
        finally:
            response_data = {'error': 'ERROR AUTH'}
            return JsonResponse(response_data, status=404)
    else:
        response_data = {'error': 'Method Not Allowed'}
        return JsonResponse(response_data, status=405)


def registry_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        password_check = data['password_check']
        if password == password_check:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'message': 'Registration Was Successful'}, status=200)
        else:
            return JsonResponse({'message': "Passwords Don't Match"}, status=200)
    else:
        response_data = {'error': 'Method Not Allowed'}
        return JsonResponse(response_data, status=405)


def validation_username(username):
    pass
