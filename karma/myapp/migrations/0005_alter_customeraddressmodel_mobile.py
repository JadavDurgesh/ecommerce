# Generated by Django 4.0.3 on 2022-10-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddressmodel',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
    ]
