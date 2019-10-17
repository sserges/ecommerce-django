from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm


User = get_user_model()


def home_page_old(request):
    html_ = """
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1 class="text-center">Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>

    """
    return HttpResponse(html_)


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Welcome to the homepage"
    }

    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHHHHHH"

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the about page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact Page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, "contact/view.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }

    print("Before authen", request.user.is_authenticated())

    if login_form.is_valid():
        print(login_form.cleaned_data)

        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("After authen", request.user.is_authenticated())
            login(request, user)
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")

    return render(request, "auth/login.html", context)


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

    return render(request, "auth/register.html", context)
