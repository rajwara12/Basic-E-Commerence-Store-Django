# Generated by Django 3.2.3 on 2021-07-16 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
