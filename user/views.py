from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from user.forms import LoginForm
from django.contrib.auth.decorators import login_required


def register(request, ):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # print("eto is.valid")
            user = form.save(commit=False)
            # print(form.cleaned_data)
            user.set_password(form.cleaned_data["password1"])
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


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # print('eto isvalid')
            # print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # print('eto auth', user)
            if user is not None:
                # print('eto is not user')
                login(request, user)
                return redirect("/store/")
            else:
                error = ValidationError('Wrong username or password', code='invalid')
                form.add_error('username', error)
                context = {
                    'form': form
                }
                return render(request, 'user_login/login.html', context)
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    # print(form.errors)
    return render(request, 'user_login/login.html', context)


def me(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'user_login/Me.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/store/')
