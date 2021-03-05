# Generated by Django 3.1.7 on 2021-03-04 17:01

from django.db import migrations, models
import miniRegisterApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('miniRegisterApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='confirm_password',
            new_name='confirmPassword',
        ),
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=20),
        ),
    ]
