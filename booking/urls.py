from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
   path("", views.index, name="index"),
   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
   path("destinations", views.destinations, name="destinations"),
   path('register', views.register_view, name='register'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('profile/', views.profile_view, name='profile'),
   path('travel-options/add/', views.add_travel_option, name='add_travel_option'),
   path('list-travel-options/', views.list_travel_options, name='list_travel_options'),
   path('book/<int:travel_id>/', views.book_travel_option, name='book_travel_option'),
   path('booking-success/', views.booking_success, name='booking_success'),
   path('bookings/', views.view_bookings, name='view_bookings'),
   path('bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]