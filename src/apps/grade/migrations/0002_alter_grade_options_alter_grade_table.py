# Generated by Django 5.1.2 on 2024-10-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name_plural': 'grades'},
        ),
        migrations.AlterModelTable(
            name='grade',
            table='grade',
        ),
    ]