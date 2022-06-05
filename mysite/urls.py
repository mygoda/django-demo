"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from user.views import send_sms, register, login, update_user
from goods.views import create_host, host_list, user_fav_host, user_unfav_host, get_user_fav_host

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_sms/', send_sms),
    path('register/', register),
    path('login/', login),
    path('update_user/', update_user),
    path('create_host/', create_host),
    path('host_list/', host_list),

    path('fav_list/', get_user_fav_host),
    path('fav_host/', user_fav_host),
    path('unfav_host/', user_unfav_host),

]
