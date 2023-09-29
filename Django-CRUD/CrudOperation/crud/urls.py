from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('modifier/<int:myId>',views.modifier,name = 'modifier'),
    path('supprimer/<int:myId>',views.supprimer,name = 'supprimer'),
]