from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TravelOption, Booking

class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field.label}'
            })



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Name")
    phone = forms.CharField(required=False, label="Phone")  
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']  

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field.label}'
            })
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['number_of_seats'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter number of seats'
        })

class TravelFilterForm(forms.Form):
    travel_type = forms.ChoiceField(
        choices=[('', 'Any'), ('flight', 'Flight'), ('train', 'Train'), ('bus', 'Bus')],
        required=False, label='Type'
    )
    source = forms.CharField(max_length=100, required=False)
    destination = forms.CharField(max_length=100, required=False)
    departure_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date'
    )
