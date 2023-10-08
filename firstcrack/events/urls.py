from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventsList.as_view(), name='events'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('calendar/', views.calendar, name="calendar")

]
