# Generated by Django 5.0.3 on 2024-06-03 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamdwell', '0003_remove_booking_booking_date_remove_booking_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreamdwellproperty',
            name='booking',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dreamdwell.booking'),
        ),
    ]