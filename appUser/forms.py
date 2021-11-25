from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('full_name', 'phone_no', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class UpdateUserForm(forms.ModelForm):
    full_name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['full_name', 'phone_no']

class UpdateProfileForm(forms.ModelForm):
    address = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    zip = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['address', 'address2', 'city', 'state', 'zip']

class UpdateProfileBillingForm(forms.ModelForm):
    card_holder_name = forms.CharField(required=False)
    card_number = forms.CharField(required=False)
    cvv = forms.CharField(required=False)
    card_expiry = forms.CharField(required=False)
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_city = forms.CharField(required=False)
    billing_state = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['card_holder_name', 'card_number', 'cvv', 'card_expiry', 'billing_address', 'billing_address2', 'billing_city', 'billing_state', 'billing_zip']