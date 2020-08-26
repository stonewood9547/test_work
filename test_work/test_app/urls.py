from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('black_table',views.black_table),
    path('white_table',views.white_table), 
    path(r'^color=/$',views.color_table,name = "table_color"),
    path(r'^place_search/$', views.search,name="place_search"), 
]
