# Generated by Django 2.2 on 2019-04-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0009_auto_20190425_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
