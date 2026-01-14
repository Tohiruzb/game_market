from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<category_id>', category_page, name='category'),
    path('article/<int:article_id>', article_detail, name='article'),
    path('search/', search_results, name='search'),
    path('new/', views.new_games, name='new_games'),
    path('popular/', popular_articles, name='popular'),
    path('about/', about_page, name='about'),

]
