from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("blog/", views.blog, name="blog"),
    path("projects/", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
    path("blog/<slug:slug>/", views.blog_post, name="blog_post"),
]