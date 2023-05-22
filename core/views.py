from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import ProfileForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Post



def index(request):
    return HttpResponse("Welcome to TalentPitcher!")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def login(request):
    # Add your login logic here
    return render(request, 'core/login.html')

@login_required
def profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/profile.html', {'user': user, 'profile': profile, 'form': form})




class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'user': user, 'profile': profile, 'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})
