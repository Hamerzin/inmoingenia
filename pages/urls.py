from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inde/', views.inde, name='inde'),
    path('about/', views.about, name='about'),
    path('contact2/', views.contact2, name='contact2')
]
