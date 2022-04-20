from django.urls import path
from article import views

urlpatterns = [
    path('article/', views.article_list),
    path('article/<int:pk>', views.article_detail)
]
