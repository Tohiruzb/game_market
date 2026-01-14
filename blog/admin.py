from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','created_time','published_time','category','rating','views')
    list_display_links = ('pk','title')
    list_filter = ('category','published_time')
    list_editable = ('category','published_time')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)




