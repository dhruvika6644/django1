"""my_market URL Configuration

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
from django.urls import path
from app_market import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('client_trade/<int:client_id>', views.client_trade, name='client_trade'),
    path('add/',views.add,name="add"),
    path('edit/<int:client_id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('export_trade_history/<int:client_id>/', views.export_trade_history_to_excel, name='export_trade_history'),
    # path('get_client_name/<int:client_id>', views.get_client_name, name='get_client_name'),
]
