from django.contrib import admin
from django.urls import path
from NewsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
]
