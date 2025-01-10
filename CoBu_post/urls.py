from .views import HomeView, ArticleDetailView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='post-details')
]
