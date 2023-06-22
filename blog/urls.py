from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home_post, name="home"),
    path('<slug>', views.detail_post, name='detail_page'),
    path('add_comment/<int:pk>', views.post_comment, name='post_comment')
]
