# Generated by Django 3.2.6 on 2021-08-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
