# Generated by Django 4.1.3 on 2022-11-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_car_color_alter_car_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car',
        ),
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ManyToManyField(related_name='shop_customers', to='shop.car'),
        ),
    ]
