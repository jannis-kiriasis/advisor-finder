# Generated by Django 3.2.17 on 2023-03-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(blank=True, choices=[(0, "I'm a financial advisor"), (1, "I'm looking for advice")]),
        ),
    ]