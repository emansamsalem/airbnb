from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE )
    title = models.CharField(max_length=50 )
    description = models.TextField(max_length=10000 )
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField( upload_to='post/')
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE )
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # if there is no value in slug field
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.auther



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

