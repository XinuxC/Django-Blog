# Generated by Django 2.0 on 2017-12-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titile',
            new_name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
