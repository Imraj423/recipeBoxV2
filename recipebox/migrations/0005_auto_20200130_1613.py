# Generated by Django 3.0.2 on 2020-01-30 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0004_auto_20200130_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='bio_field',
            new_name='bio',
        ),
    ]
