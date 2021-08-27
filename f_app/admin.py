from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
admin.site.register(user)
admin.site.register(Clothes)
admin.site.register(Product)