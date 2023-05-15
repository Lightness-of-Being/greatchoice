from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # 비밀번호 필드
    password_confirm = models.CharField(max_length=128)  # 비밀번호 확인 필드
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username
