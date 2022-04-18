from rest_framework import serializers
from blog.models import Blog


# Base Serializers
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    slg = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=256)
    body = serializers.CharField()
    image = serializers.ImageField(default='', use_url=True)
    active = serializers.BooleanField(default=False)


# Model Serializers
class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['id', 'slg', 'title', 'description', 'body', 'image', 'active']

