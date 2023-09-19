from django.http.response import JsonResponse, HttpResponseBadRequest
from .models import *
from django.views.decorators.csrf import csrf_exempt
from minio import Minio


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
            print(f'type= {type(str(bucket_name))}')
            create_minio_bucket(bucket_name)
            minio_client = Minio("http://localhost:9001/api/v1/service-account-credentials",
                                 access_key="0geNc5DmznJsNtMrW7MS",
                                 secret_key="fQD2yzPGEDyUv1DoWQjMEXGMo0n0bo0CPPcmHkLX",
                                 secure=False)
            return JsonResponse({"message": "Success Upload"}, status=200)
        else:
            return HttpResponseBadRequest("File not found in the request")
    else:
        return HttpResponseBadRequest("Invalid request method")


@csrf_exempt
def personal_account(request,user_id):
    pass
