from django.urls import path
from comment import views

urlpatterns = [
    path('comment/', views.comments_list),
    path('comment/<int:pk>', views.comment_detail),
    path('article/<int:pk>/comment', views.create_comment_to_article),
    path('comment/<int:pk>/comment', views.create_comment_to_comment),
    path('article/<int:pk>/comment/depth=<int:dp>',
         views.get_comments_for_article),
    path('comment/<int:pk>/comment/depth=<int:dp>',
         views.get_comments_for_comment),
]
