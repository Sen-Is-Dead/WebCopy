from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login/') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.date_of_birth = request.POST.get('date_of_birth')
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
        user.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)