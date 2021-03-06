from django import forms
from django.contrib.auth import get_user_model
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, null=False, default='username')
    password = models.CharField(max_length=16, null=False, default='pass')


class Auction(models.Model):
    start_date = models.DateField(default="2019-01-01")
    end_date = models.DateField(default="2019-01-01")
    name = models.CharField(max_length=32, default="Auction Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Offer(models.Model):
    text = models.TextField(max_length=256)
    is_accepted = models.BooleanField(default=False)


class Category(models.Model):
    name = models.TextField(max_length=16, null=True)


class Product(models.Model):
    description = models.TextField(max_length=256)
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    msg_content = models.TextField(max_length=256)
