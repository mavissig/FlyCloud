from django.http.response import JsonResponse, HttpResponseBadRequest
from .models import *
from django.views.decorators.csrf import csrf_exempt


def session_check(request):
    if request.user.is_authenticated:
        print(f'[username]: {request.user.username}')
        return JsonResponse({'username': request.user.username}, status=200)
    else:
        return JsonResponse({'message': 'No'}, status=401)


@csrf_exempt
def upload_file(request,user_id):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            bucket_name = User.objects.filter(id=user_id)
            create_minio_bucket(bucket_name[0].username.lower())
            return JsonResponse({"message": "Success Upload"}, status=200)
        else:
            return HttpResponseBadRequest("File not found in the request")
    else:
        return HttpResponseBadRequest("Invalid request method")


@csrf_exempt
def personal_account(request,user_id):
    pass
