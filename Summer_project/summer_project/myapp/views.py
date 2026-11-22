from django.shortcuts import render, redirect
from .forms import NameForm


def home_view(request):
    greeting_message = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user = form.save()
            # PRG-паттерн: redirect после POST предотвращает повторную отправку
            return redirect(f'/?greeting={user.name}')
    else:
        form = NameForm()
        greeting_name = request.GET.get('greeting')
        if greeting_name:
            greeting_message = f'Привет, {greeting_name}!'

    return render(request, 'myapp/home.html', {
        'form': form,
        'greeting': greeting_message,
    })
