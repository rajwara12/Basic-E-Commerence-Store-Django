# Generated by Django 3.2.3 on 2021-07-16 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
    ]
