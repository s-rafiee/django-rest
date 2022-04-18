from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from blog.models import Blog
from blog.serializers import BlogModelSerializer


class GetAllBlog(APIView):
    def get(self, request):
        query = Blog.objects.all()
        serializers = BlogModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
