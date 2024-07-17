from django.urls import path
from .views import ArticleListCreate, ArticleDetail,ArticleCount

urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('article-count/', ArticleCount.as_view(), name='article-detail'),

]
