from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            posts = Post.objects.filter(author=user).order_by('-date_posted')[:5]  
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('users-profile')
    
    else:
        user = request.user
        if user.is_authenticated:
            posts = Post.objects.filter(author=user).order_by('-date_posted')[:5]
        
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
        'posts': posts
    }
    return render(request, 'users/profile.html', context)


@login_required
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users-login')
    return render(request, 'users/logout.html')


