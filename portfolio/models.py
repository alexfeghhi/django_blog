from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogPost(models.Model):
    status_choices = (
        (0,"Draft"),
        (1,"Published")
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=status_choices, default = 0)
    
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

class HomePage(SingletonModel):
    draft_content = RichTextUploadingField(blank=True)
    published_content = RichTextUploadingField(blank=True)
    edit_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "Home Page"

    class Meta:
        verbose_name = "Home Page"

class ContactPage(SingletonModel):
    draft_content = RichTextUploadingField(blank=True)
    published_content = RichTextUploadingField(blank=True)
    edit_date = models.DateTimeField(auto_now= True)
    def __str__(self):
        return "Contact Page"

    class Meta:
        verbose_name = "Contact Page"