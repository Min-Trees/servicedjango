# Generated by Django 4.2.1 on 2023-09-10 02:23

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.UUIDField(primary_key=True,default=uuid.uuid4)),
                ('userName', models.CharField(max_length=200)),
                ('userEmail', models.EmailField(max_length=254, unique=True)),
                ('userPassWord', models.CharField(max_length=200)),
            ],
        ),
    ]