from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    
    list_display = [
        'email',
        'telefone',
        'idade',
    ]
    
    fieldsets = (
        ("Informações Gerais", {"fields": ['email', 'nome', 'last_login']}),
        ("informações Pessoas", {'fields': ["telefone", "idade", "uuid"]}),
        ("Tags", {"fields": ['is_admin', "is_staff", "is_superuser", "is_verified"]}),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "nome",
                    "idade",
                    "telefone",
                    "password1",
                    "password2",
                ],
            },
        )
    ]
    list_filter = ['is_verified', 'cadastro']
    search_fields = ['email', 'idade', 'nome']
    ordering = ['-last_login']
    filter_horizontal = ['user_permissions']
    date_hierarchy = 'cadastro'
    
    
admin.site.register(Usuario, UsuarioAdmin)