# Generated by Django 4.2.3 on 2023-07-17 10:20

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is super user')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('updated_at', models.DateTimeField(editable=False, null=True, verbose_name='updated at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-created_at',),
                'default_related_name': 'users',
                'indexes': [models.Index(fields=['id'], name='users_user_id_1cecd0_idx')],
            },
        ),
    ]
