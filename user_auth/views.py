from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework import viewsets
from user_auth.forms import LoginForm
from user_auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from .renderers import UserJSONRenderer
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer



class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта User во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        # request.data -> некий дикт - данные которые отправил тебе клиент
        # print(request.data, 'Наша дата')
        # user = {"email": "user@email.com", "username": "some_username", "password": "qwerty"} VALID DATA


        serializer = self.serializer_class(data=request.data)
        # print(user, 'Наш юзер')
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# email = INPUT KorneYBuRAU@GMail.com -> VALIDATION LOGIC - to_lower() + check this is email by regex!!!!-> CLEANED DATA korneyburau@gmail.com


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
