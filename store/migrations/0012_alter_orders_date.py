# Generated by Django 4.2.6 on 2024-01-26 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_orders_phone_alter_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 26, 21, 7, 29, 19709)),
        ),
    ]
