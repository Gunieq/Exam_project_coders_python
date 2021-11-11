from django import forms
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, null=False)
    password = forms.CharField(widget=forms.PasswordInput)


class Auction(models.Model):
    start_date = models.DateField(default="2019-01-01")
    end_date = models.DateField(default="2019-01-01")
    name = models.CharField(max_length=32, default="Auction Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Offer(models.Model):
    text = models.TextField(max_length=256)


class Category(models.Model):
    name = models.TextField(max_length=16)


class Product(models.Model):
    description = models.TextField(max_length=256)
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Prediction(models.Model):
    pass


class Message(models.Model):
    pass
