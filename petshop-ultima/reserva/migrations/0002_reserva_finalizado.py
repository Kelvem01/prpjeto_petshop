# Generated by Django 4.2.3 on 2023-08-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='finalizado',
            field=models.BooleanField(default=False, verbose_name='Finalizado'),
        ),
    ]