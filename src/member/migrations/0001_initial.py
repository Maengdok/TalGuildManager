# Generated by Django 5.1.2 on 2024-10-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('added_at', models.DateField()),
                ('removed_at', models.DateField()),
                ('is_on_discord', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('is_pvp', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
    ]