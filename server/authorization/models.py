import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def authorization_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        try:
            user = User.objects.get(username=data['username'])
            print(f'USER={user}')
            if user.check_password(data['password']):
                return JsonResponse({'message': 'Authorized'}, status=200)
            else:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
        finally:
            response_data = {'error': 'User not found'}
            return JsonResponse(response_data, status=404)
    else:
        pass
