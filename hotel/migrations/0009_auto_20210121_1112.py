# Generated by Django 3.1.3 on 2021-01-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20210121_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='front_img',
            field=models.ImageField(upload_to='hotel/static/hotel/images'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='gallery',
            field=models.ImageField(upload_to='hotel/static/hotel/images'),
        ),
    ]
