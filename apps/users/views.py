from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import CreationForm
from .utils import anonymous_required


@anonymous_required
def signup(request):
    form = CreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        email = form.cleaned_data['email']
        send_mail(
            'Регистрация на foodgram',
            'Поздравляем! пиздец!',
            'Foodgram',
            email
        )

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html', {'form': form})
