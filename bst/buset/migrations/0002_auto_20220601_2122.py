# Generated by Django 3.2.8 on 2022-06-01 14:22

import buset.models
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('buset', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_pp',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_updated',
            new_name='updated',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_password',
        ),
        migrations.AddField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=buset.models._create_hash, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
