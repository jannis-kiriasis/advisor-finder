# Generated by Django 3.2.17 on 2023-02-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0004_auto_20230210_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisoruserprofile',
            name='status',
        ),
        migrations.AddField(
            model_name='advisoruserprofile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
