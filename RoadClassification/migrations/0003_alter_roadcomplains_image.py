# Generated by Django 4.0.1 on 2022-01-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoadClassification', '0002_roadcomplains_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadcomplains',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recieved'),
        ),
    ]
