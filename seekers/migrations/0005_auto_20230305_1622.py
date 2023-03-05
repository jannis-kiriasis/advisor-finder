# Generated by Django 3.2.17 on 2023-03-05 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seekers', '0004_auto_20230304_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekeruserprofile',
            name='need',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='needs', to='home.specialisation'),
        ),
        migrations.AlterField(
            model_name='seekeruserprofile',
            name='town_or_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address', to='home.location'),
        ),
        migrations.AlterField(
            model_name='seekeruserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='seekers', to=settings.AUTH_USER_MODEL),
        ),
    ]
