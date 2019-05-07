# Generated by Django 2.2 on 2019-04-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0020_auto_20190425_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='process',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='file',
            name='filepath',
            field=models.FileField(null=True, unique=False, upload_to='files/', verbose_name=''),
        ),
    ]
