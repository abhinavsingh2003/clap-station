# Generated by Django 4.2.3 on 2023-12-25 15:05

import clapStationWebsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0003_testing_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(default='', help_text=' ClapStation upload image | height: 360px | width: 800px', upload_to='posts/image', validators=[clapStationWebsite.models.validate_image_dimensions]),
        ),
    ]
