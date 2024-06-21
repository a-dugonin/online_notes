from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import User, Note


# from .forms import RegisterUserForm


class StartPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'mainapp/home_page.html')


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'mainapp/reg_page.html'
#     success_url = reverse_lazy('mainapp:login')
#
#     def get_context_data(self, **kwargs):
#         pass

def register(request: HttpRequest) -> HttpResponse:
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     email = request.POST.get('email')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #
    #     if (username, first_name, last_name, email) and password1 == password2:
    #         User.objects.create_user(
    #             username=username,
    #             first_name=first_name,
    #             last_name=last_name,
    #             email=email,
    #             password=password1)
    #
    #         return redirect('login')
    # return render(request, 'mainapp/reg_page.html')


    # if request.method == 'POST':
    #     form = RegisterUserForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             # user = form.save()
    #             # password = form.cleaned_data.get('password1')
    #             # user = authenticate(username=user.username, password=password)
    #             # login(request, user)
    #             return redirect('mainapp:login')
    #         except:
    #             form.add_error(None, 'Wrong input!!!')
    # else:
    #     form = RegisterUserForm()
    #
    # context = {
    #     # 'title': 'Sign up',
    #     # 'user': request.user,
    #     # 'nav_bar': nav_bar,
    #     'form': form,
    # }
    # return render(request, 'mainapp/reg_page.html', context)

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get("username"),
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password1")
            )
            return redirect('login')
    else:
        form = RegisterUserForm()
    context = {
        "form": form
    }
    return render(request, 'mainapp/reg_page.html', context=context)


def login_page(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("notes")

        return render(request, 'mainapp/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect("notes")

    return render(request, 'mainapp/login.html', context={'error': "Неверное имя пользователя или пароль"})


def notes_list(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    notes = Note.objects.filter(user_id=user.pk)
    return render(request, 'mainapp/notes.html', {'notes': notes})


def logout_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')


def add_notes(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        note = request.POST.get('note-text')
        user = request.user
        Note.objects.create(text=note, user_id=user.pk)
    return render(request, 'mainapp/add_note.html')
