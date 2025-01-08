from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.form_view,name='form'),
    path('',views.home_view,name='home'),
]