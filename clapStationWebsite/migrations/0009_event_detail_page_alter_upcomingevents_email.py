# Generated by Django 4.2.3 on 2023-12-26 08:33

import clapStationWebsite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0008_upcomingevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_detail_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', help_text=' ClapStation upload image | height: 360px | width: 640px', upload_to='posts/image', validators=[clapStationWebsite.models.validate_image_dimensions])),
                ('eventname', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
