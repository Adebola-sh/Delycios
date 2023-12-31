# Generated by Django 4.2.1 on 2023-06-02 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderAndCart', '0002_alter_order_payment_status_alter_order_status_and_more'),
        ('delivery_management', '0003_alter_delivery_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='orderAndCart.order'),
        ),
    ]
