from django.urls import reverse
from django.utils import timezone
from django.db import models
from martor.models import MartorField
from django.db import models
from django.utils.text import slugify


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
	slug = models.SlugField(max_length=250, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to="static/images")
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Blog Posts"
		verbose_name_plural = "Blog Posts"


	# def get_absolute_url(self):
	# 	return reverse('blog:post_detail',
	# 	               args=[self.publish.year,
	# 	                     self.publish.strftime('%m'),
	# 	                     self.publish.strftime('%d'),
	# 	                     self.slug])

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

	class Meta:
		verbose_name = "Blog Comments"
		verbose_name_plural = "Blog Comments"


class Tag(models.Model):
	name = models.CharField(max_length=255)
