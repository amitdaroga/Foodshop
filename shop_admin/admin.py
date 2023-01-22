from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(All_User)
admin.site.register(Verification)
admin.site.register(ProductDetails)