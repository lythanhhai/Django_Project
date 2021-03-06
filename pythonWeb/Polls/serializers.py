from rest_framework import serializers
from .models import Article

'''
class ArticleSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(seft, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
'''

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = '__all__'
        fields = ['id', 'title', 'description']