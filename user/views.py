from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.






#REGISTER
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!\n Please Login to your account')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})