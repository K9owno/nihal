from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="Todolist"

urlpatterns = [
    path('', views.createtodo,name='createtodo'),
    path('showtodo/',views.showtodo,name='Todos'),
    path('Signup/',views.signup_view,name='SignUp'),
    path('Login/',views.Login_view,name='Login'),
    path('Logout/',views.Logout_view,name='Logout')
]

urlpatterns += staticfiles_urlpatterns()