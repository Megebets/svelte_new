# Generated by Django 5.1.6 on 2025-02-24 08:50

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('pol', models.CharField(blank=True, max_length=10)),
                ('has_parents', models.BooleanField(default=False)),
                ('livingplace', models.BooleanField(default=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=200)),
                ('residence', models.CharField(blank=True, max_length=200)),
                ('contact_phone', models.CharField(blank=True, max_length=15)),
                ('trusted_person_phone', models.CharField(blank=True, max_length=15)),
                ('education', models.BooleanField(default=False)),
                ('education_level', models.CharField(blank=True, max_length=100)),
                ('specialty', models.CharField(blank=True, max_length=100)),
                ('has_working', models.BooleanField(default=False)),
                ('has_housing', models.BooleanField(default=False)),
                ('was_married', models.BooleanField(default=False)),
                ('has_children', models.BooleanField(default=False)),
                ('children_boys', models.IntegerField(default=0)),
                ('children_girls', models.IntegerField(default=0)),
                ('children_ages', models.CharField(blank=True, max_length=100)),
                ('height', models.IntegerField(default=170)),
                ('has_criminal_record', models.BooleanField(default=False)),
                ('has_bad_habits', models.CharField(blank=True, max_length=200)),
                ('performs_namaz', models.BooleanField(default=False)),
                ('clothing_preference', models.CharField(blank=True, max_length=200)),
                ('spouse_nationality_importance', models.BooleanField(default=False)),
                ('spouse_age_min', models.IntegerField(default=18)),
                ('spouse_age_max', models.IntegerField(default=30)),
                ('ok_with_divorced_spouse', models.BooleanField(default=False)),
                ('ok_with_spouse_children', models.BooleanField(default=False)),
                ('clothing_preferences', models.CharField(blank=True, max_length=200)),
                ('health', models.CharField(blank=True, max_length=200)),
                ('willing_to_relocate', models.BooleanField(default=False)),
                ('agree_to_be_second_wife', models.BooleanField(default=False)),
                ('plan_to_have_children', models.BooleanField(default=True)),
                ('health_status', models.CharField(blank=True, max_length=200)),
                ('additional_info', models.TextField(blank=True)),
                ('spouse_requirements', models.TextField(blank=True)),
                ('profile_completion_date', models.DateTimeField(auto_now=True)),
                ('consent_to_data_processing', models.BooleanField(default=False)),
                ('madhhab', models.CharField(blank=True, max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
