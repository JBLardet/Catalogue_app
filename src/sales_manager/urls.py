from django.urls import path
from .views import index, login

urlpatterns = [
    path('', index, name="sales-index"),
    path('login/', login, name="login"),
]