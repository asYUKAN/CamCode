from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name='upload-index'),
    path('',views.uploaded,name='upload-uploaded'),
    path('execute/',views.Executed,name='upload-executed')
    
]
