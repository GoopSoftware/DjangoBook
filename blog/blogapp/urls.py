from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    # <int:id> Takes an integer from the URL and passes it as an id to post_detail
    path('<int:id>/', views.post_detail, name='post_detail'),
]