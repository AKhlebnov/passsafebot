# Generated by Django 4.2 on 2025-03-12 13:29

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0003_category_alter_password_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=255, verbose_name='Пароль')),
        ),
    ]
