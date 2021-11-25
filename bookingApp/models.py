from django.db import models
from django.conf import settings


class Room(models.Model):

    ROOM_STATUS = (
        (0, 'AVAILABLE'),
        (1, 'OCCUPIED'),
        (2, 'UNDER_MAINTENANCE'),
        (3, 'UNAVAILABLE')
    )
    ROOM_CATEGORY = (
        (0, 'STANDARD'),
        (1, "ECONOMY"),
        (2, "PREMIUM"),
        (3, 'SUITE')
    )

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    picture1 = models.ImageField(upload_to='images/rooms', blank=True, null=True)
    picture2 = models.ImageField(upload_to='images/rooms', blank=True, null=True)
    picture3 = models.ImageField(upload_to='images/rooms', blank=True, null=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=ROOM_STATUS, default=0)
    beds = models.IntegerField(null=True, blank=True)
    category = models.IntegerField(choices=ROOM_CATEGORY, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_room_cat(self):
        return dict(self.ROOM_CATEGORY).get(self.category)

    def get_room_status(self):
        return dict(self.ROOM_STATUS).get(self.status)

class Booking(models.Model):

    BOOKING_STATUS = (
        (0, 'PENDING'),
        (1, 'APPROVED'),
        (2, 'ACCOMMODATED'),
        (3, 'CANCELLED')
    )

    id = models.BigAutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    booked_from = models.DateTimeField(blank=True, null=True)
    booked_to = models.DateTimeField(blank=True, null=True)
    booked_for_days = models.IntegerField(blank=True, null=True)

    def get_booking_status(self):
        return dict(self.BOOKING_STATUS).get(self.status)