from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    content = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-update_time']


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
