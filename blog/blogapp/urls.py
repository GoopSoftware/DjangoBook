from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # <int:year> requires an int value based on variable input for the url
    # <slug:post> requires a slug(A string that contains only letters, numbers, underscores, or hyphens
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'
         ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path(
        '<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
]