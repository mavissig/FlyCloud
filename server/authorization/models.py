import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@csrf_exempt
def authorization_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
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
        password= data['password']
        password
    else:
        response_data = {'error': 'Method Not Allowed'}
        return JsonResponse(response_data, status=405)
