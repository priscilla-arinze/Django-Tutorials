from django.urls import path

from . import views

app_name = 'baseapproute'

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<int:url_id>", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<int:url_id>", views.updateRoom, name="update-room"),
    path("delete-room/<int:url_id>", views.deleteRoom, name="delete-room"),
]