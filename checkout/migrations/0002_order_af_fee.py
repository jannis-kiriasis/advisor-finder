# Generated by Django 3.2.17 on 2023-02-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='af_fee',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
            preserve_default=False,
        ),
    ]
