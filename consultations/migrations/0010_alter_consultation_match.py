# Generated by Django 3.2.17 on 2023-03-07 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0009_alter_message_match'),
        ('consultations', '0009_auto_20230305_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation', to='matches.match'),
        ),
    ]
