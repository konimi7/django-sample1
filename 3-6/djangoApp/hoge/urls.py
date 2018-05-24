from django.urls import path

from . import views

urlpatterns = [
    # /hoge に対応
    path('', views.index),
    # /hoge/foo に対応
    path('foo', views.foo),
    # /hoge/woo に対応
    path('woo', views.woo),
]
