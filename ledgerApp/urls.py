"""ledgerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from sheet import views as sheet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('sheet.urls')),
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sheet/', sheet_views.ledger_view,name='ledger_sheet'),
    path('sheet/<int:pk>/delete', sheet_views.ledge_del, name = 'ledge_del'),
    # path('login/', includes(''))
]
