from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('authors/', views.AuthorList.as_view(), name="author_list"),
    path('authors/new/', views.AuthorCreate.as_view(), name="author_create"),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('authors/<int:pk>/update', views.AuthorUpdate.as_view(), name="author_update"),
    path('authors/<int:pk>/delete', views.AuthorDelete.as_view(), name="author_delete")
]