"""
URL configuration for Basar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from BasarDerksen import views
from BasarDerksen.views import * 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Testshop', Testshop),
    path('cassa', cassa, name='cassa'),
    path('update-item/', views.update_item, name='update_item'),
    path('login', index, name='hompage'),
    path('Gunterhans', Gunterhans),
    path('check-update/', check_for_update, name='check_update'),
    path('!', help),
    path('!sys', sys),
    path('Shop', TEST, name='TEST'),
    path('', start),
    path('info', kundeninfo),
    path('AGB', agb),
    path('deleteAll/<str:text>/', delete_all_items ),
    path('getStore', numberpro),
    path('Shop_Handy', Handy),
    path('happy-hour/', Happy_Hour),
    path('check_reload/', views.check_reload, name='check_reload'),

]