from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    category= models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)
    




