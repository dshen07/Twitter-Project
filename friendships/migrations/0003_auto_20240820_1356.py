# Generated by Django 3.1.3 on 2024-08-20 13:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendships', '0002_auto_20240820_1033'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='friendship',
            index_together={('created_at', 'to_user_id'), ('from_user_id', 'created_at')},
        ),
    ]
