from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('homecat/<str:cat>/', views.homecat, name='homecat'),
    path('product/<int:id>/', views.product, name='product'),
    path('addtocard/<int:id>/', views.addtocard, name='addtocard'),
    path('removefromcard/<int:id>/', views.removefromcard, name='removefromcard'),
    path('displaycard/', views.displaycard, name='displaycard'),
    path('displaycardid/<int:id>/', views.displaycardid, name='displaycardid'),
    path('displayallcards/', views.displayallcards, name='displayallcards'),
    path('paiement/', views.paiement, name='paiement'),
    path('essai/', views.essai, name='essai'),
]