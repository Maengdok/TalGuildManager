# Generated by Django 5.1.2 on 2024-10-25 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_type', '0001_initial'),
        ('grade', '0001_initial'),
        ('member', '0001_initial'),
        ('weapon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='combat_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='combat_type.combattype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grade.grade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='weapon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='weapon.weapon'),
            preserve_default=False,
        ),
    ]