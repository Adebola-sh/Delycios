# Generated by Django 4.2.1 on 2023-06-02 05:38

from django.db import migrations, models
import django.db.models.deletion
import extras.funcs


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='destination',
            field=models.ForeignKey(default=extras.funcs.get_default_address, on_delete=django.db.models.deletion.CASCADE, related_name='deliveries_to', to='delivery_management.delivery'),
        ),
    ]
