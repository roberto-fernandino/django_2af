from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Usuario, Codigo


# Register your models here.
class UsuarioAdmin(UserAdmin):
    # Form no painel do admin para modificar um usuário.
    form = UsuarioChangeForm

    # Form no painel de admin para criar um usuário.
    add_form = UsuarioCreationForm

    # Escolhe quais atributos serão mostrados quando listados na pagina deste modelo no painel de admin.
    list_display = [
        "email",
        "telefone",
        "idade",
    ]
    # Personaliza a página de
    fieldsets = (
        ("Informações Gerais", {"fields": ["email", "nome", "last_login"]}),
        ("informações Pessoas", {"fields": ["telefone", "idade", "uuid", "password"]}),
        ("Tags", {"fields": ["is_admin", "is_staff", "is_superuser", "is_verified"]}),
    )
    # Permite a filtração por estes dois atributos.
    list_filter = ["is_verified", "cadastro"]

    # Permite a busca de acordo com estes atributos.
    search_fields = ["email", "idade", "nome"]

    # Organiza de acordo com um atributo.
    ordering = ["-last_login"]


class CodigoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "codigo"]


admin.site.register(Codigo, CodigoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
