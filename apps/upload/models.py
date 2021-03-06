from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from videokit.models import VideoField, VideoSpecField
from django.core.validators import MinLengthValidator

# Create your models here.
class Video(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, validators=[MinLengthValidator(25)], null=True, default="Title Lorem ipsum dolor sit amet, consectetur adipisicing elit.")
	description = models.CharField(max_length=200, null=True, default="Description Lorem ipsum dolor sit amet, consectetur adipisicing elit.")
	video = VideoField(upload_to = 'upload/video/', null = True,
    	mimetype_field = 'video_mimetype',
    	duration_field = 'video_duration',
    	thumbnail_field = 'video_thumbnail')
	video_thumbnail = models.ImageField(upload_to = 'upload/img/', blank=True, null=True)
	text = models.TextField(null=True, default="Text Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sed cupiditate porro reprehenderit, quibusdam modi, ex iusto similique dolore autem magni quae molestias doloremque hic maxime maiores laudantium dolores, assumenda illum.")
	slug = models.SlugField(unique=True)
	published_date = models.DateTimeField(default=timezone.now)
	video_mimetype = models.CharField(max_length = 32, blank = True, null=True)
	video_duration = models.IntegerField(blank = True, null = True)
	video_mp4 = VideoSpecField(source = 'video', format = 'mp4')
	video_ogg = VideoSpecField(source = 'video', format = 'ogg')
	video_webm = VideoSpecField(source = 'video', format = 'webm')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


