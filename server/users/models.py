import os

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from dotenv import load_dotenv
import boto3


class FileMetadata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_rating = models.PositiveIntegerField()
    file_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class BucketMetadata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bucket_name = models.CharField(max_length=255)
    bucket_is_private = models.BooleanField()


def create_minio_bucket(bucket_name):
    load_dotenv()

    minio_client = boto3.client(
        's3',
        endpoint_url=os.environ.get('ENDPOINT_URL'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    name = bucket_name[0].username.lower()
    print(os.environ.get('ENDPOINT_URL'))
    try:
        minio_client.create_bucket(Bucket=name)
        print(f"Бакет {name} успешно создан")
    except Exception as e:
        print(f"Не удалось создать бакет {name}: {str(e)}")
