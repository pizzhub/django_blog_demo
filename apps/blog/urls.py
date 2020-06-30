from django.urls import path

from apps.blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name='create_blog'),
    path('<slug>/', detail_blog_view, name='detail_blog'),
    path('<slug>/edit', edit_blog_view, name='edit_blog')
]

