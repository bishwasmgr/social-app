# Generated by Django 5.1.1 on 2024-09-08 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_appuser_is_active_appuser_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='creator',
        ),
    ]
