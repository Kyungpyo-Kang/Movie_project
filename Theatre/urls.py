from django.contrib import admin
from django.urls import path
import Main.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.views.home, name='home'),
    path('Main/family', Main.views.family_pro, name='family'),
    path('Main/couple', Main.views.couple_show, name='couple'),
    path('Main/solo', Main.views.solo_show, name='solo'),
    path('Main/searchresult', Main.views.result_show, name='result'),
]
