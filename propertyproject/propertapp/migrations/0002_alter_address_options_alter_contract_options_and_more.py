# Generated by Django 5.1.3 on 2024-11-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propertapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='lease',
            options={'verbose_name': 'Lease', 'verbose_name_plural': 'Leases'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='ternant',
            options={'verbose_name': 'ternant', 'verbose_name_plural': 'Ternants'},
        ),
    ]
