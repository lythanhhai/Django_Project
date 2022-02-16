from csv import list_dialects
from django.contrib import admin
from .models import Article

# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    # lọc theo title và description
    list_filter = ('title', 'description')
    #
    list_display = ('title', 'description')
