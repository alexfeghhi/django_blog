from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import BlogPost, HomePage, ContactPage
from tinymce.widgets import TinyMCE

#register models below
class BlogPostAdmin(admin.ModelAdmin):
    list_display =  ('title','author','slug','pub_date','status')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(HomePage, SingletonModelAdmin)
admin.site.register(ContactPage, SingletonModelAdmin)