from django.urls import path
from . import views

urlpatterns = [
    path("htmll",views.htmll,name="htmll"),
    path("Home",views.Home,name="Home"),
    path("Add",views.Add,name="Add"),
    path("pagetest",views.pagetest,name="pagetest"),
    path("AssestADD",views.AssestADD,name="AssestADD"),
    path('showFull/<int:pk>/', views.showFull, name='showFull'),
    path('update_device/<int:pk>/', views.update_device, name='update_device'),
    path('Assestupdate', views.Assestupdate, name='Assestupdate'),
    path('add_device/<int:pk>/', views.add_device, name='add_device'),
    path('my_devices', views.my_devices, name='my_devices'),



    
]