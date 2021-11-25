from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Room, Booking



class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'status', 'category', 'added_on', 'updated_on')
    list_filter = ('status', 'category')
    search_filter = ('id', 'title', 'price', 'status', 'category', 'added_on', 'updated_on')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'room', 'user', 'added_on', 'updated_on', 'booked_from', 'booked_to', 'booked_for_days')
    list_filter = ('status',)
    search_filter = ('status', 'room', 'user', 'added_on', 'updated_on', 'booked_from', 'booked_to', 'booked_for_days')

admin.site.register(Room , RoomAdmin)
admin.site.register(Booking, BookingAdmin)
