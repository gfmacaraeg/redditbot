from __future__ import unicode_literals

from django.db import models

class  Link(models.Model):
	id = models.CharField(max_length=64, primary_key=True)
	title = models.CharField(max_length=255)
	link = models.CharField(max_length=255, blank=False)
	subreddit = models.CharField(max_length=50)
	nsfw = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)