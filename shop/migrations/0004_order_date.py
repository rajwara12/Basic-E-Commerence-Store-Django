# Generated by Django 3.2.3 on 2021-07-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_cutomer_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=''),
        ),
    ]
