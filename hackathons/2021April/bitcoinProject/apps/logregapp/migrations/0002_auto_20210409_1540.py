# Generated by Django 2.2 on 2021-04-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logregapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
