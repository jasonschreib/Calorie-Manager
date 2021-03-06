"""calorieManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from log.views import splash, accounts, homepage, signup, log_in, delete, edit, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('accounts', accounts, name='accounts'),
    path('homepage', homepage, name='homepage'),
    path('signup', signup, name='signup'),
    path('log_in', log_in, name='log_in'),
    path('delete', delete, name='delete'),
    path('edit', edit, name='edit'),
    path('logout', logout_view, name='logout')
]
