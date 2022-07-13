
from django.urls import path
from . import views


urlpatterns = [
  
   path('',views.restview),
   path('seri/',views.seriview),
   path('create/',views.create)

]