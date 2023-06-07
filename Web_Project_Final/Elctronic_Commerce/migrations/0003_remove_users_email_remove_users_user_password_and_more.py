# Generated by Django 4.2 on 2023-06-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elctronic_Commerce', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_password',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=10, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=10, max_length=255),
            preserve_default=False,
        ),
    ]
