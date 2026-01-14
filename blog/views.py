from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    sort_field = request.GET.get('sort')
    if sort_field:
        articles = articles.order_by(sort_field)
    for article in articles:
        print(f"Article ID: {article.pk}, Title: {article.title}")
        print(f"{article.title} - Photo exists: {bool(article.image)}")

    context = {
        'title':'Home',
        'categories':categories,
        'articles':articles,
    }

    return render(request, 'blog/index.html', context)

def category_page(request, category_id):
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    articles = Article.objects.filter(category_id=category_id)

    context = {
        'title':f'{category.title}',
        'category':category,
        'articles':articles,
        'categories':categories,
    }

    return render(request, 'blog/index.html', context)

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.views += 1
    article.save()
    articles = Article.objects.all()
    articles = articles.order_by('-views')

    context = {
        'title':f'{article.title}',
        'article':article,
        'articles':articles,
    }
    return render(request, 'blog/article_detail.html', context)



def search_results(request):
    word = request.GET.get('q')
    articles = Article.objects.filter(
        Q(title__icontains=word)
    )
    context = {
        'articles':articles,
        'word':word,
        'title':'Search Results',
    }
    return render(request, 'blog/index.html',context)


def new_games(request):
    articles = Article.objects.filter(
        published_time=True
    ).order_by('-created_time')

    return render(request, 'blog/new.html', {
        'articles': articles,
        'title':'New Games',
    })

def popular_articles(request):
    articles = Article.objects.filter(
        published_time=True
    ).order_by('-views')   # ← ENG MUHIM QATOR

    return render(request, 'blog/popular.html', {
        'articles': articles,
        'title':'Popular Games',
    })


def about_page(request):
    return render(request, 'blog/about.html')