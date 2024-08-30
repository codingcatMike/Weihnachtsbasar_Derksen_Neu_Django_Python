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
from BasarDerksen.views import Testshop
from BasarDerksen.views import cassa
from BasarDerksen import views
from BasarDerksen.views import index
from BasarDerksen.views import Shop_1
from BasarDerksen.views import Shop_2
from BasarDerksen.views import Shop_3
from BasarDerksen.views import Shop_4
from BasarDerksen.views import Shop_5
from BasarDerksen.views import Shop_6
from BasarDerksen.views import Shop_7
from BasarDerksen.views import Gunterhans
from BasarDerksen.views import check_for_update




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Testshop', Testshop),
    path('cassa', cassa),
    path('update-item/', views.update_item, name='update_item'),
    path('', index, name='hompage'),
    path('Shop1', Shop_1),
    path('Shop2', Shop_2),
    path('Shop3', Shop_3),
    path('Shop4', Shop_4),
    path('Shop5', Shop_5),
    path('Shop6', Shop_6),
    path('Shop7', Shop_7),
    path('Gunterhans', Gunterhans),
    path('check-update/', check_for_update, name='check_update'),

]