# Generated by Django 4.0.4 on 2022-05-18 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='status',
            new_name='is_available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='status',
            new_name='is_available',
        ),
    ]
