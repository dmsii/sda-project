# Generated by Django 2.1.2 on 2018-11-15 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import videokit.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('video', videokit.models.VideoField(duration_field='video_duration', mimetype_field='video_mimetype', null=True, thumbnail_field='video_thumbnail', upload_to='upload/video/')),
                ('video_thumbnail', models.ImageField(blank=True, null=True, upload_to='upload/img/')),
                ('text', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video_mimetype', models.CharField(blank=True, max_length=32, null=True)),
                ('video_duration', models.IntegerField(blank=True, null=True)),
                ('video_mp4', videokit.models.VideoSpecField(blank=True, null=True, upload_to='')),
                ('video_ogg', videokit.models.VideoSpecField(blank=True, null=True, upload_to='')),
                ('video_webm', videokit.models.VideoSpecField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
