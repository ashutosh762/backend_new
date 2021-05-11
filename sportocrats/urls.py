
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('main1.html', views.main1, name='main1'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('announce.html', views.announce, name='announce'),
    path('contactus.html', views.contactus, name='contactus'),
    path('register.html', views.register, name='register'),
    path('male.html', views.male, name='male'),
    path('female.html', views.female, name='female'),

]