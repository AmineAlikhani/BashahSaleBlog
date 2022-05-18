# Generated by Django 4.0.4 on 2022-05-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_available',
            new_name='status',
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
