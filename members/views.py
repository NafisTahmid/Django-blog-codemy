from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registrations/registration.html'
    success_url = reverse_lazy('login')

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registrations/login.html', {'form': form})

def custom_logout_view(request):
    # Logs out the user
    logout(request)
    # Redirect to the home page after logging out (or any other page)
    return redirect('home')