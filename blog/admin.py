from django.contrib import admin
from .models import Blog, Category, Tag, Comment


@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "author", "category")
    search_fields = ('title','description')


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published_at")
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}


@admin.register(Tag)
class Tagadmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published_at")
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}



@admin.register(Comment)
class commentadmin(admin.ModelAdmin):
    list_display = ("blog", "name", "email")
    search_fields = ('blog','name')