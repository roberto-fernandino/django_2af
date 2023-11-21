from django import forms
from .models import Usuario
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Forms aqui

class UsuarioCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
    )
    nome = forms.CharField(
        label='nome',
        widget=forms.TextInput(),
    )
    telefone = forms.CharField(
        label='telefone',
        widget=forms.TextInput(),
    )
    idade = forms.IntegerField(
        label='idade',
        widget=forms.NumberInput(),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "id": "password1",
                "placeholder": "password",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirme Senha",
        widget=forms.PasswordInput(
            attrs={
                "id": "password2",
                "placeholder": "confirme senha",
                "required": True,
            }
        ),
    )
    class Meta:
        model = Usuario
        fields = [
            'email',
            'nome',
            'telefone',
            'idade',
        ]
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não conferem")
        return password2
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user

class UsuarioChangeForm(forms.ModelForm):
    """Objeto para atualizar dados no painel de admin"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = [
            "email",
            "password",
            "telefone",
            "nome",
            "is_admin",
            "is_superuser",
            "is_staff",
        ]