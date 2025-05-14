from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('habar/<int:announcement_id>/', views.habar, name='habar'),
    path('itb/<int:course_id>/', views.itb, name='itb'),
    path('uirme/<int:club_id>/', views.uirme, name='uirme'),
    path('bas/<int:member_id>/', views.bas, name='bas'),
] 