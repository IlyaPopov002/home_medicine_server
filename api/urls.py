from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('medicines/', views.getMedicines),
    path('medicines/create/', views.createMedicine),
    path('medicines/<str:pk>/update/', views.updateMedicine),
    path('medicines/<str:pk>/delete/', views.deleteMedicine),
    path('medicines/<str:pk>/', views.getMedicine)

]