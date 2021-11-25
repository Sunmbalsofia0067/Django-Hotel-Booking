from django.urls import path
from .views import index, signUp, login, register_success, user_panel, contact, aboutus, terms_conditions, privacy_policy, get_all_rooms, booking_form

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('signup', signUp, name= 'signup'),
    path('user',user_panel, name='user-panel'),
    path('contact', contact, name='contact'),
    path('aboutus', aboutus, name='aboutus'),
    path('privacy', privacy_policy, name='privacy'),
    path('terms', terms_conditions, name='terms'),
    path('registration-success', register_success, name='regsitarion-success'),
    path('get_all_rooms', get_all_rooms, name='regsitarion-success'),
    path('booking-form', booking_form, name='booking-form'),
]