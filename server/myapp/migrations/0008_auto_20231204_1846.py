# Generated by Django 3.2.23 on 2023-12-04 18:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20231204_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default=uuid.UUID('ffdb7952-22bb-4b27-b420-78181694f9e4'), max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='join_string',
            field=models.CharField(default=uuid.UUID('7d227b6a-d130-4eb4-9138-8eed5324c529'), max_length=50, unique=True),
        ),
    ]