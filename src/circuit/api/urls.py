from django.urls import path

from .views import (
    circuit_create,
    circuit_delete,
    circuit_detail,
    circuit_list,
    circuit_update,

    workout_create,
    workout_delete,
    workout_detail,
    workout_list,
    workout_update,
)

urlpatterns = [
    path('', circuit_list.as_view()),
    path('create/', circuit_create.as_view()),
    path('<pk>', circuit_detail.as_view()),
    path('<pk>/update/', circuit_update.as_view()),
    path('<pk>/delete/', circuit_delete.as_view()),


    path('workout/create/', workout_create.as_view()),
    path('workout/', workout_list.as_view()),
    path('workout/<pk>', workout_detail.as_view()),
    path('workout/<pk>/update/', workout_update.as_view()),
    path('workout/<pk>/delete/', workout_delete.as_view()),
]