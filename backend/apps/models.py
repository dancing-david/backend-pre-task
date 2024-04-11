import os

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Contact(BaseModel):
    profile_image = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'contact'
        verbose_name = '연락처'
        verbose_name_plural = '연락처'

    def __str__(self):
        return self.name


class Label(BaseModel):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='label')
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'label'
        verbose_name = '라벨'
        verbose_name_plural = '라벨'

    def __str__(self):
        return self.name
