# Generated by Django 3.0.3 on 2020-03-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0007_auto_20200303_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='faves',
            field=models.ManyToManyField(blank=True, related_name='faves', to='recipebox.Recipe'),
        ),
    ]
