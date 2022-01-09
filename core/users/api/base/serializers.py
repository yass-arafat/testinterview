from rest_framework import serializers

from core.users.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("name", "user_id")
