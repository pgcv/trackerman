# Generated by Django 2.1.5 on 2019-04-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0020_auto_20190425_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='processed',
            field=models.IntegerField(default=0),
        ),
    ]
