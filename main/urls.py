from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('detail/<int:pk>/', views.portfolioView, name='portfolio'),
    path('about/', views.aboutView, name='about'),
    path('services/', views.servicesView, name='services'),
    path('contact/', views.contactView, name='contact'),
    path('portfolio/', views.portView, name='port'),
    path('resume/', views.resumeView, name='resume'),
]