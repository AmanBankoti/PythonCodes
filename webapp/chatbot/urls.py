from django.urls import path
from . import views

urlpatterns = [
    path('',views.b , name='HOME_PAGE' ),
]