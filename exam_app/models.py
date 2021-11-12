from django import forms
from django.contrib.auth import get_user_model
from django.db import models


class User(models.Model):
    login = models.CharField(max_length=16, default='login')
    username = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=16, null=False, default='pass')


class Auction(models.Model):
    start_date = models.DateField(default="2019-01-01")
    end_date = models.DateField(default="2019-01-01")
    name = models.CharField(max_length=32, default="Auction Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Offer(models.Model):
    text = models.TextField(max_length=256)


class Category(models.Model):
    name = models.TextField(max_length=16, default='cat')


class Product(models.Model):
    description = models.TextField(max_length=256, default='desc')
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE, default=1, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
