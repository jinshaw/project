from django.contrib import admin

# Register your models here.
from mysite import models
admin.site.register(models.UserInfo)