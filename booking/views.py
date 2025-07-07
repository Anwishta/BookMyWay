from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, TravelOptionForm, BookingForm, TravelFilterForm
from .models import TravelOption, Booking

# Home Page
def index(request):
    travels = TravelOption.objects.all()
    return render(request, 'index.html', {'travels': travels})

# Static Pages
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def destinations(request):
    return render(request, 'destination.html')

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile Update
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

# Admin: Add Travel Option
def add_travel_option(request):
    if request.method == 'POST':
        form = TravelOptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Travel option added successfully!')
            return redirect('list_travel_options')
    else:
        form = TravelOptionForm()
    return render(request, 'travel_option.html', {'form': form})

# List & Filter Travel Options
def list_travel_options(request):
    form = TravelFilterForm(request.GET or None)
    options = TravelOption.objects.all()

    if form.is_valid():
        travel_type = form.cleaned_data.get('travel_type')
        source = form.cleaned_data.get('source')
        destination = form.cleaned_data.get('destination')
        departure_date = form.cleaned_data.get('departure_date')

        if travel_type:
            options = options.filter(travel_type=travel_type)
        if source:
            options = options.filter(source__icontains=source)
        if destination:
            options = options.filter(destination__icontains=destination)
        if departure_date:
            options = options.filter(datetime__date=departure_date)

    return render(request, 'list_travel_options.html', {
        'options': options,
        'form': form
    })

# Book Travel Option
@login_required
def book_travel_option(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * booking.number_of_seats

            if booking.number_of_seats > travel_option.available_seats:
                form.add_error('number_of_seats', 'Not enough seats available.')
            else:
                booking.save()
                travel_option.available_seats -= booking.number_of_seats
                travel_option.save()
                return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'book_travel.html', {
        'form': form,
        'travel_option': travel_option
    })

# Booking Success Page
def booking_success(request):
    return render(request, 'booking_success.html')

# View My Bookings
@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'view_bookings.html', {'bookings': bookings})

# Cancel Booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    if not booking.is_cancelled:
        booking.is_cancelled = True
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.info(request, 'This booking is already cancelled.')
    return redirect('view_bookings')
