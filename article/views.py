from django.shortcuts import render
from .models import *

# Create your views here.

def categories(request):
    categories=Category.objects.all()

    return{
        'categories':categories,
    }


def index(request):
    all_article = Article.objects.all()

    context ={
        'articles': all_article
    }
    return render(request,'article/index.html',context)

def single_article(request,pk):
    article=Article.objects.get(pk=pk)

    context={
        'article':article,
    }
    return render(request,'article/article.html',context)
