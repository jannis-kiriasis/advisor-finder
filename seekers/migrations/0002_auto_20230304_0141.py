# Generated by Django 3.2.17 on 2023-03-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekeruserprofile',
            name='postcode',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='seekeruserprofile',
            name='street_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]