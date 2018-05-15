from django.conf.urls import include, url
from django.contrib import admin

from home import views

urlpatterns = [
    url('search/', views.search_shops),
    url('cate/', views.show_shop_cate),
    url('product/', views.show_shop_detail),
    url('detail/', views.get_shop_img),
    url('login/', views.login),
]
