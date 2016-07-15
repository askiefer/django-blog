from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	# use charfield to define a property with a limited number of chars
	title = models.CharField(max_length=200)
	# unlimited chars
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
