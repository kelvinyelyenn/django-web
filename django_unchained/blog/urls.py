from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.home, name="blog_home"),
    url(r'about/', views.about, name="blog_about"),
]
