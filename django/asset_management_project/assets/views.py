# assets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm  # Assuming you create a ProfileForm in forms.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    

def catalog_view(request):
    return render(request, 'catalog.html') 

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile_view(request):
    profile = request.user.profile  # Assuming you have a OneToOneField relationship with Profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/profile.html', {'form': form})
