from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name

class Blog(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
        author = models.CharField(max_length=128)
        content = models.TextField()
	views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        post_time = models.DateTimeField(auto_now_add=True)
        update_time = models.DateTimeField(auto_now=True)	


	def __unicode__(self):
		return self.title
