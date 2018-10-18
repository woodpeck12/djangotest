from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse
#from django.contrib.auth.models import User



class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
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



