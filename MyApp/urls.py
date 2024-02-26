from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('team/', views.team, name='my_team'),
    path('why/', views.why, name='my_why'),
    path('testimonial/', views.testimonial, name='my_testimonial'),
    path('contact/', views.contact, name='my_contact')
]
