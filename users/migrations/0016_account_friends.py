# Generated by Django 4.2.1 on 2023-09-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_account_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='friends',
            field=models.CharField(blank=True, verbose_name='self'),
        ),
    ]