# Generated by Django 5.1.2 on 2024-10-25 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
        ('roadster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadsterMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
                ('roadster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadster.roadster')),
            ],
        ),
    ]
