# Generated by Django 4.2.4 on 2023-08-18 09:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 9, 45, 4, 459632, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='bids',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productBids', to='auctions.auctionproduct'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 9, 45, 4, 459632, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productComment', to='auctions.auctionproduct'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 9, 45, 4, 459632, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchProducts', to='auctions.auctionproduct'),
        ),
    ]