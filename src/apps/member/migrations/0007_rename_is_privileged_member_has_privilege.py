# Generated by Django 5.1.2 on 2024-10-29 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_member_added_at_alter_member_removed_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='is_privileged',
            new_name='has_privilege',
        ),
    ]
