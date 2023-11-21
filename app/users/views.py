from django.shortcuts import render
from .models import Usuario
# Create your views here.
def verify(request, uuid):
    usuario = Usuario.objects.get(uuid=uuid)
    if usuario is not None:
        usuario.is_verified = True
        usuario.save()
        context = {'usuario': usuario}
        return render(request, 'users/verify.html', context)