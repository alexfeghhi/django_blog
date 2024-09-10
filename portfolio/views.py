from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
#from django.views import generic
from .models import BlogPost, HomePage, ContactPage

# Create your views here.
def base(request):
    context = {"page": "base"}
    return render(request, "portfolio/base.html", context)

def home(request):
    post = HomePage.objects.all()[0]
    context = {"post": post}
    return render(request, "portfolio/base_home.html", context)

def blog(request):
    post_list = BlogPost.objects.order_by('-pub_date')
    context = {"posts": post_list}
    return render(request, "portfolio/base_blog.html", context)

def projects(request):

    return render(request, "portfolio/base_projects.html")

def contact(request):
    context = {"page": "contact"}
    return render(request, "portfolio/base_contact.html", context)

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    context = {"post": post}
    return render(request, "portfolio/base_blog_post.html", context)