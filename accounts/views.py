from django.shortcuts import render, redirect
from django.contrib.auth import login                   # login() to log the user if the registration info is correct
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """
       Register a new users.
       The function displays a blank registration form, when the registration 
       page is first requested. Then process completed registration forms when
       they're submitted. When a registration is successful, the function log
       the new user in.
    """
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form, based on submitted data request.POST
        form = UserCreationForm(data = request.POST)
        
        # check username has enough characters, pwd match, no malicious activ.
        if form.is_valid():
            new_user = form.save()  # save username and hash pwd to the db
            # Log the user in and redirect to homepage
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
