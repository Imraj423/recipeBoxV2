# Generated by Django 3.0.3 on 2020-03-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0006_author_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='faves',
            field=models.ManyToManyField(related_name='faves', to='recipebox.Recipe'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Author'),
        ),
    ]
