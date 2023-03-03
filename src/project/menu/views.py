from django.shortcuts import render


def menu(request, menu_name: str):
    context = {"menu_name": menu_name}
    return render(request, "menu/index.html", context=context)
