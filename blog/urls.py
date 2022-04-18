from django.urls import path
from blog.views import GetAllBlog

urlpatterns = [
    path("blogs/", GetAllBlog.as_view()),
]
