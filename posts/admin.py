from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'author']
    search_fields = ['title', 'content', 'tags']
    list_filter = ['publish_date', 'author']

admin.site.register(Post, PostAdmin)