from django.contrib import admin

# Register your models here.
from booking.models import TravelOption, Booking

admin.site.register(TravelOption)
admin.site.register(Booking)