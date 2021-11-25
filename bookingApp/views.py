from django.http import request, JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.serializers import serialize
import json
from datetime import date, datetime
from django.shortcuts import render
from .models import Room, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signUp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user')
    else:
        return render(request, 'login.html')

def register_success(request):
    return render(request, 'registration-user-success.html')

def user_panel(request):
    if request.user.is_authenticated:
        rooms = Room.objects.all()
        bookings = Booking.objects.filter(user=request.user).order_by('-added_on')
        pending_bookings = Booking.objects.filter(user=request.user, status=0)
        context = {
            'user': request.user,
            'rooms': rooms,
            'bookings': bookings,
            'total_bookings': bookings.count(),
            'pending_bookings': pending_bookings.count(),
        }
        return render(request, 'userpanel.html', context)
    else:
        return HttpResponseRedirect('/login')
        
    

def get_all_rooms(request):
    if request.user.is_authenticated:
        rooms = Room.objects.all()
        rooms_serialized = json.loads(serialize('json', rooms))
        context = {
            'rooms': rooms_serialized
        }
        return JsonResponse(context)
    else:
        return HttpResponseRedirect('/login')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def terms_conditions(request):
    return render(request, 'terms.html')

def booking_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            booking = Booking()
            booking.user = request.user
            room = Room.objects.filter(id=request.POST['room'])
            booking.room = room.first()
            booking.booked_from = request.POST['inputStartDate']
            booking.booked_to = request.POST['inputEndDate']
            date_format = "%Y-%m-%d"
            delta = datetime.strptime(str(request.POST['inputEndDate']), date_format) - datetime.strptime(str(request.POST['inputStartDate']), date_format)
            booking.booked_for_days = delta.days + 1
            booking.save()
            return HttpResponseRedirect('/user')
            # return HttpResponse('Room Booked Successfully!', status=201)
        else:
            return HttpResponse('Not Allowed!')
    else:
        return HttpResponseRedirect('/login')
