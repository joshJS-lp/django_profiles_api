from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models  import BaseUserManager


class UserProfileManager(BaseUserManager):
    #Funcion para manipular los objetos del perfil
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('EL usuario debe tener un email')
        #normalizar el correo 
        email = self.normalize_email(email)
        #instanciando el modelo 
        user = self.model(email=email, name=name)
        # el usuario requiere un password
        user.set_password(password)
        #guardar el usuario en la base de datos
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, name, email, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True #ereda de PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)
        
        return user


# Create nuestros propios podelos
class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Modelo en la db en el sistema
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #MOdo a usar para nuestros objetos por defecto
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        """Retornar cadena representando el usuuario"""
        return self.email 