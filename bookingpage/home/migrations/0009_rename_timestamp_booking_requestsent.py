# Generated by Django 3.2 on 2021-05-13 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_booking_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='timeStamp',
            new_name='requestsent',
        ),
    ]
