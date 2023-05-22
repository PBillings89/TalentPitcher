from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('posts/', views.post_list, name='post_list'),
    # Add the following line:
    path('posts', views.post_list, name='post_list'),
]
