# Generated by Django 3.2.23 on 2023-12-04 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_customuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='join_string',
            field=models.CharField(default=uuid.UUID('c659fa1a-96cc-441f-b1e2-e457ada9983e'), max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default=uuid.UUID('baea045e-88ea-4660-92ce-bec79055c7e3'), max_length=50, unique=True),
        ),
    ]
