# Generated by Django 4.2.7 on 2023-11-21 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usuario_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('352d562e-4d3c-46c7-90c1-287f68cd1b83'), unique=True),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('useruario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
