from . import views
from django.urls import path

urlpatterns = [
    path('',views.Postlist.as_view(), name="HOME"),
    path('post<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]
