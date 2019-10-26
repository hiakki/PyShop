from django.contrib import admin
from .models import Blog, Categorie


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


# Register your models here.
admin.site.register(Blog)
admin.site.register(Categorie)