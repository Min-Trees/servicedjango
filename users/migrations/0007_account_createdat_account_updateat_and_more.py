# Generated by Django 4.2.1 on 2023-09-21 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0006_alter_account_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='createdAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='account',
            name='updateAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='account',
            name='userBirthDay',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='account',
            name='userGender',
            field=models.CharField(choices=[('MALE', 'Nam'), ('FEMALE', 'Nữ')], default='MALE', max_length=10),
        ),
        migrations.AddField(
            model_name='account',
            name='userRole',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]
