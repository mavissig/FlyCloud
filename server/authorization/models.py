import json
from django.http.response import JsonResponse
from django.contrib.auth.models import User


def authorization_user(request):
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        try:
            user = User.objects.get(username=data['username'])
            if user.check_password(data['password']):
                return JsonResponse({'message': 'Authorized'}, 200)
            else:
                return JsonResponse({'message': 'Unauthorized'}, 401)
        finally:
            response_data = {'error': 'User not found'}
            return JsonResponse(response_data, 404)
    else:
        pass
