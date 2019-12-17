from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url

from .forms import ContactForm, LoginForm, RegisterForm


User = get_user_model()

# Create your views here.


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if login_form.is_valid():
        print(login_form.cleaned_data)

        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # print("After authen", request.user.is_authenticated())
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                # context['form'] = LoginForm()
                return redirect("/")
        else:
            print("Error")

    return render(request, "accounts/login.html", context)


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }

    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "accounts/register.html", context)
