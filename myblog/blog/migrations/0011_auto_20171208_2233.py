# Generated by Django 2.0 on 2017-12-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171208_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='filename',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]