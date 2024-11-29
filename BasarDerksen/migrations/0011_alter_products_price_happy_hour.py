# Generated by Django 4.0.2 on 2024-11-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasarDerksen', '0010_happyhour_products_price_happy_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_happy_hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
