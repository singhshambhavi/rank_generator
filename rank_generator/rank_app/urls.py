from django.urls import path, include
from rank_app import views

urlpatterns = [
    path("userdetails/", views.DetailView),
    path("rankdisplay/", views.DetailView),
    #path("checkrank/", views.RankView),
]