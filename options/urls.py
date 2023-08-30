from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.options, name='options'),
    path('contactus/', views.contactus, name='contactus'),
    path('list/', views.lists, name='lists'),
    path('list/details/<int:id>', views.details, name ='details'),
    path('list/details2/<int:id>', views.details2, name ='details'),
    path('list/details4/<int:id>', views.details4, name ='details'),
    path('', views. myfirst, name='myfirst'),
]



