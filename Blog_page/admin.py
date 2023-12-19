from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discription','image']


