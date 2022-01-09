from django.urls import path

from core.users.api.base.views import UserArticleView, ArticleView

url_patterns = [
    path('user/<str:user_id>/article', UserArticleView.as_view(), name="user-article"),
    path('article/<int:article_id>', ArticleView.as_view(), name="article")
]
