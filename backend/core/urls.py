from django.urls import include, path

from . import views

urlpatterns = [
    path("hello/", views.index.as_view(), name="index"),
    path("api/hello/", views.index.as_view(), name="index"),
    path('product-list/', views.ShowAll, name='product-list'),
]
