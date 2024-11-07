from . import views
from django.urls import path

urlpatterns = [
    path('',views.Postlist.as_view(), name="HOME"),
    path('<slug:slug>/', views.Postlist.as_view(), name="post_detail"),
]
