from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('black_table',views.black_table),
    path('white_table',views.white_table), 
    path('search/', views.search,name="search"), 
]
