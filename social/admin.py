from django.contrib import admin
from .models import Post, Comment, UserProfile,Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Like)