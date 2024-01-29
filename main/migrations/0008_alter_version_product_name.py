# Generated by Django 4.2.1 on 2023-06-28 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_version_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='main.product', verbose_name='Наименование продукта'),
        ),
    ]