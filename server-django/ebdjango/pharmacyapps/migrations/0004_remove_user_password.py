# Generated by Django 4.2 on 2023-05-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapps', '0003_alter_medicamentos_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]