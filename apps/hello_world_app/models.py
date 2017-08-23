from __future__ import unicode_literals

from django.db import models
import re
import bcrypt


class  Link(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	link = models.CharField(max_length=255, blank=False)
	subreddit = models.CharField(max_length=50)
	nsfw = models.BooleanField()
	category = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)