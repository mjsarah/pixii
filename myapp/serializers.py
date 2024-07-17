from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    prix_final = serializers.SerializerMethodField()    
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['id', 'title', 'content', 'created_at', 'prix', 'discount', 'prix_final']


def get_prix_final(self, obj):
        return obj.calculer_prix_final()        