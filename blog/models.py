from django.utils import timezone
from django.db import models
from martor.models import MartorField
from django.db import models


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=255)
	body = MartorField()
	short_description = models.CharField(max_length=255, blank=True, null=True)
	tags = models.ManyToManyField("Tag")
	author = models.ForeignKey("UserProfile", related_name='blog_posts', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to="images/")
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title


class UserProfile(models.Model):
	username = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('N', 'None')))
	age = models.IntegerField(null=True)

	def get_absolute_url(self):
		return f"/user/{self.username}"


class Comments(models.Model):
	post = models.ForeignKey("Post", on_delete=models.CASCADE)
	body = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	published = models.BooleanField(default=False)


class Tag(models.Model):
	name = models.CharField(max_length=255)
