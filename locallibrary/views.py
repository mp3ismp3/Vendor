from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Errors', form.errors)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            return render(request, 'registration/register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form' : form}
        return render(request, 'registration/register.html', context)

