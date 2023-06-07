# Generated by Django 4.2 on 2023-06-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elctronic_Commerce', '0004_device_alter_users_email_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='briefDescription',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='device',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
