# Generated by Django 4.1.7 on 2024-06-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
