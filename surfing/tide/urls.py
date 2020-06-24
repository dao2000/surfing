from django.urls import path

from .views import ArticleViewT

app_name = "tide"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('tides/<int:key>-<str:point>', ArticleViewT.as_view())
]