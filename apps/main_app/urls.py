from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('rescuee/<int:pk>', views.rescueeview, name='rescuee'),
]
