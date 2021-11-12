from django.contrib import admin

from exam_app.models import User


@admin.register(User)
class Admin(admin.ModelAdmin):
    pass

