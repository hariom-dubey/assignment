from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.events, name='events'),
    path('add-event/', views.add_event, name="add_event"),
    path('event_fav/<int:pk>/', views.event_fav, name="event_fav"),
]