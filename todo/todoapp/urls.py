from django.urls import path
from todoapp import views

urlpatterns = [
    
   
    path('home/',views.home),
    path('contact/',views.contact),
    path('about/',views.about),
    path('add_task/',views.add_task),
    path('dtl',views.dtl),
    path('delete/<rid>',views.delete_task),
    path('edit/<rid>',views.edit_task),
    path('completed/<rid>',views.mark_completed),
    
]
