from django.shortcuts import render
from operator import attrgetter
from apps.blog.models import BlogPost


def home(request):
    context = {}

    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)

    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)

