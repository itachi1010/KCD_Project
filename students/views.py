from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileForm, CourseRegistrationForm, ConfirmFeesForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import CourseRegistration, Profile

@login_required
def home(request):
    return render(request, 'students/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'students/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'students/login.html')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'students/profile.html', {'form': form, 'profile': profile})

@login_required
def course_registration(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            messages.success(request, 'Course registration successful!')
            return redirect('course_registration_preview', pk=registration.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CourseRegistrationForm()
    return render(request, 'students/course_registration.html', {'form': form})


@login_required
def confirm_fees(request):
    if request.method == 'POST':
        form = ConfirmFeesForm(request.POST, request.FILES)
        if form.is_valid():
            confirm_fees_instance = form.save(commit=False)
            confirm_fees_instance.user = request.user
            confirm_fees_instance.save()
            messages.success(request, 'Fees confirmed successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ConfirmFeesForm()
    return render(request, 'students/confirm_fees.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'students/change_password.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def course_registration_preview(request, pk):
    registration = CourseRegistration.objects.get(pk=pk)
    return render(request, 'students/course_registration_preview.html', {'registration': registration})
