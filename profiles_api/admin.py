from django.contrib import admin
#importar los modelos
from profiles_api import models
# Register your models here.
admin.site.register(models.UserProfile)
