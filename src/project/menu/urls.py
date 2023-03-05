from django.urls import path

from menu import views


urlpatterns = [
    path("<menu_name>/", views.menu, name="menu"),
]
