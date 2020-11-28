from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('rescuee/<int:pk>', views.rescueeview, name='rescuee'),
    path('dashboard/', views.rescue_dashboard, name='rescuee_dashboard'),
    path('dashboard/status/<int:pk>', views.rescuer_info, name='rescuee_info'),
    path('dashboard/done/<int:pk>', views.done_rescue, name='done_rescue')
]
