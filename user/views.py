from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from user.forms import RegistrationForm


# @require_POST
def register(request,):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("eto is.valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/store/')
        else:
            print("eto first else")
            context = {
                'form': form
            }
            # Если форма не валидна – показать заново с ошибками
            return render(request, 'user_registration/registration.html', context)
    else:
        print("eto second else")
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'user_registration/registration.html', context)

def all_users_view(request):
    user = get_user_model()
    users = user.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_registration/all_users.html', context)