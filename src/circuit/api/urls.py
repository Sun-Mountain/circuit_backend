from django.urls import path

from .views import (
    circuit_list, 
    circuit_detail, 
    
    workout_list, 
    workout_detail
)
urlpatterns = [
    path('', circuit_list.as_view()),
    path('<pk>', circuit_detail.as_view()),

    path('workout/', workout_list.as_view()),
    path('workout/<pk>', workout_detail.as_view())
]