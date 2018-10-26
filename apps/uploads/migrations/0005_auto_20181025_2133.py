# Generated by Django 2.0 on 2018-10-25 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0004_auto_20181025_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
