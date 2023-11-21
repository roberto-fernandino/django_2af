from django.db import models
from datetime import datetime
from django.contrib.auth.models import (
AbstractBaseUser,
BaseUserManager,
PermissionsMixin,
)
import uuid
from django.utils.text import slugify


# Create your models here.
class UsuarioManager(BaseUserManager):
    # Objeto que executara a criação de contas -> outro objeto Usuario.
    def create_user(
        self,
        nome,
        email,
        telefone,
        idade,
        cadastro,
        password=None,
    ):
        
        # Making email, telefone and idade obrigatory
        
        if not email:
            raise ValueError("Email obrigatorio")
        if not nome:
            raise ValueError("Nome obrigatorio")
        if not telefone:
            raise ValueError("Telefone obrigatorio")
        if not idade:
            raise ValueError("Idade obrigatoria")
        
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            telefone=telefone,
            idade=idade,
            cadastro=cadastro,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(
        self,
        nome,
        email,
        telefone,
        idade,
        cadastro=datetime.now(),
        password=None,
    ):
        
        # Making email, telefone and idade obrigatory
        
        if not email:
            raise ValueError("Email obrigatorio")
        if not nome:
            raise ValueError("Nome obrigatorio")
        if not telefone:
            raise ValueError("Telefone obrigatorio")
        if not idade:
            raise ValueError("Idade obrigatoria")
        
        user = self.create_user(
            email=self.normalize_email(email),
            nome=nome,
            telefone=telefone,
            idade=idade,
            cadastro=cadastro,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    #Fields
    email=models.EmailField(max_length=255, unique=True)    
    nome=models.CharField(max_length=255)
    idade=models.IntegerField()
    telefone=models.CharField(max_length=15)
    cadastro=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4(), blank=False, unique=True)
    
    # Tags (still fields)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    # 2 auth
    is_verified=models.BooleanField(default=False)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nome", "idade", "telefone"]
    
    
    def __str__(self):
        return f"Usuario (email = {self.email})"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label: str) -> bool:
        return True
    

class Code(models.Model):
    useruario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8)
    
        
        