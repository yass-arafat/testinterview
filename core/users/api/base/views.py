from rest_framework.views import APIView
from rest_framework.response import Response

from core.users.api.base.serializers import ArticleSerializer
from core.users.models import Article


class UserArticleView(APIView):
    def get(self, request, user_id):
        article = Article.objects.filter(user_id=user_id).all()
        serialized = ArticleSerializer(article, many=True)

        return Response(make_context(error=False,
                                     message="Returned data successfully",
                                     data=serialized.data))


class ArticleView(APIView):
    def get(self, request, article_id):
        article = Article.objects.filter(pk=article_id).first()
        serialized = ArticleSerializer(article)

        return Response(make_context(error=False,
                                     message="Returned data successfully",
                                     data=serialized.data))


def make_context(error: bool = False, message: str = "", data=None):
    context = {"error": error, "message": message, "data": data}
    return context
