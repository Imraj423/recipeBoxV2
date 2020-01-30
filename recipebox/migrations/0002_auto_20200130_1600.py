# Generated by Django 3.0.2 on 2020-01-30 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time_required', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebox.Author')),
            ],
        ),
        migrations.DeleteModel(
            name='NewsItem',
        ),
    ]
