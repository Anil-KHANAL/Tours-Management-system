# Generated by Django 3.2 on 2021-05-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_requestsent_booking_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]