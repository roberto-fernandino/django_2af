from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario
from emails.funcs import send_email_boas_vindas


@receiver(post_save, sender=Usuario)
def enviar_email_para_usuario_que_acabou_de_cadastrar(sender, instance, created, **kwargs):
    if created:
        print(send_email_boas_vindas(instance.email, instance.nome, f"127.0.0.1:8000/users/verify/{instance.uuid}"))