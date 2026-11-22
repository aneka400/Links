from django.shortcuts import render
from .form import NameForm
from .model import UserProfile

def home_view(request):
    greeting_message = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user = form.save()
            greeting_message = f"Привет, {user.name}!"
            form = NameForm()

    else:
        form = NameForm()

    context = {
        'form': form,
        'greeting': greeting_message
    }
    return render(request, 'home.html', context)