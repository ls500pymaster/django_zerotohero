# Generated by Django 4.1.7 on 2023-03-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_userprofile_location_userprofile_website_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
