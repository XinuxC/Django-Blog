# Generated by Django 2.0 on 2017-12-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171208_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='filename',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
