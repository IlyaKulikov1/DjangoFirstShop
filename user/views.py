from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms import RegistrationForm



def register(request,):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("eto is.valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("/store/")
        else:
            print("eto first else")
            context = {"form": form}
            # Если форма не валидна – показать заново с ошибками
            return render(request, "user_registration/registration.html", context)
    else:
        print("eto second else")
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'user_registration/registration.html', context)

def all_users_view(request):
    user = get_user_model()
    users = user.objects.all()
    context = {"users": users}
    return render(request, "user_registration/all_users.html", context)
