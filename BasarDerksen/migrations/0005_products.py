# Generated by Django 5.1 on 2024-09-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasarDerksen', '0004_shoppingitem_modified_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronumber', models.PositiveIntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
