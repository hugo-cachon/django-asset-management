# Generated by Django 4.2.8 on 2023-12-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=''),
        ),
    ]