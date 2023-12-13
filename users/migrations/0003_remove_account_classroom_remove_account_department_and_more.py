# Generated by Django 4.2.1 on 2023-12-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_account_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='account',
            name='department',
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AddField(
            model_name='account',
            name='avatar_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='background_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='school_faculty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='school_majors',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='school_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('ADMIN', 'Admin')], max_length=8),
        ),
    ]