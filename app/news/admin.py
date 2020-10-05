from django.contrib import admin
from .models import Article, ArticleBody


class ArticleBodyAdmin(admin.StackedInline):
    model = ArticleBody
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_disply = ['title', 'author', 'creation_date']
    search_fields = ['title', 'subtitle', 'author', 'creation_date']
    inlines = [ArticleBodyAdmin]
