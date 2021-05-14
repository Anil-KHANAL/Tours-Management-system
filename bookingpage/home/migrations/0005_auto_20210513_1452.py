# Generated by Django 3.2 on 2021-05-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_content_booking_queries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(auto_now_add=True, help_text='Check in', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(blank=True, help_text='Check out', null=True),
        ),
    ]