# Generated by Django 3.2.17 on 2023-02-09 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisoruserprofile',
            old_name='street_address1',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='advisoruserprofile',
            name='street_address2',
        ),
    ]
