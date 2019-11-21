from django.shortcuts import render


def cart_home(request):
    # print(request.session.session_key)
    request.session['first_name'] = "Justin"
    return render(request, "carts/home.html", {})
