# Generated by Django 3.2 on 2021-05-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='checkout',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
