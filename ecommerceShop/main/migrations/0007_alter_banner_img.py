# Generated by Django 4.0.4 on 2022-05-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_product_image_productattribute_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='brand_imgs/'),
        ),
    ]
