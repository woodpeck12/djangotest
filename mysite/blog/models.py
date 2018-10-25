from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
#from django.contrib.auth.models import User



class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	#tagging using taggit
	tags = TaggableManager()
	
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	author = models.ForeignKey('auth.user',related_name='blog_posts',on_delete='CASCADE')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
							choices=STATUS_CHOICES,	
							default='draft')
	class Meta:
		ordering = ('-publish',)
	
	def __str__(self):
		return self.title

	objects = models.Manager() #default
	published = PublishedManager() #woodpeck

	def get_url(self):
		return reverse('blog:post_detail',kwargs={
												'year':self.publish.year,
												'month':self.publish.strftime('%m'),
												'day':self.publish.strftime('%d'),
												'post':self.slug})



class Comment(models.Model):
	post = models.ForeignKey(Post,related_name = 'comments',on_delete='CASCADE')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'comment by {} on {}'.format(self.name,self.post)