# Generated by Django 4.2.6 on 2024-01-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_ID', models.IntegerField()),
                ('PRODUCT', models.CharField(max_length=50)),
                ('QUANTITY', models.IntegerField()),
                ('PRICE', models.IntegerField()),
            ],
        ),
    ]
