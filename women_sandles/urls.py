from django.urls import path
from . import views

urlpatterns=[
    path('',views.wsandles,name='wsandles'),
]