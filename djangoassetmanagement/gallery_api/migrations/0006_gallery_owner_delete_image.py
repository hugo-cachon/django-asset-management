# Generated by Django 4.2.8 on 2023-12-18 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery_api', '0005_remove_image_name_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
