from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'image', 'author', 'date_published', 'date_updated')

