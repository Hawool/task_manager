from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Ends an application session"""
    logout(request)
    return HttpResponseRedirect(reverse('tasks:index'))


def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Processing the completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Logging in and redirecting to the home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('tasks:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)