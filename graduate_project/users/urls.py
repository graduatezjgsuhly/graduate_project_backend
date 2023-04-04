from django.contrib import admin
from users.views import listusers
from users.views import user_sign_up, user_login_in
from django.urls import path, include
urlpatterns = [
    path('listusers/',listusers),
    path('sign_up_users/',user_sign_up),
    path('login_in_users/',user_login_in)
]