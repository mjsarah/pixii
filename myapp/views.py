from django.shortcuts import render

from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#    def calculer_prix_final(self):
        
#         if self.prix and self.discount:
#             remise_montant = (self.discount / 100) * self.prix
#             prix_final = self.prix - remise_montant
#             return prix_final
#         return self.prix  

class ArticleCount(APIView):

    def get(self,request,format=None):

        article_count=Article.objects.count()
        
        return Response({
            "counts":article_count
        })
            
        
