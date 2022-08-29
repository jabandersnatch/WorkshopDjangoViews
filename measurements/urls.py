from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.measurements_view, name='measurements_view'),
    path('<int:pk>', views.measurement_view, name='measurment_view' ),
    path('<int:pk>/update', views.update_measurement, name='update_measurement'),
    path('<int:pk>/delete', views.delete_measurement, name='delete_measurement')
]
