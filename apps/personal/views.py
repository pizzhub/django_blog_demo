from django.shortcuts import render
from operator import attrgetter
from apps.blog.models import BlogPost
from apps.blog.views import get_blog_queryset


def home(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)

