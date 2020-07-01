from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.index,name='book' ),
    path('', views.main,name='main' ),

]