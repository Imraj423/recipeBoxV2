# Generated by Django 3.0.2 on 2020-01-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0002_auto_20200130_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='byline',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
