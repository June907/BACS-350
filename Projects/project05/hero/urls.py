from .views import AboutPage, BasePage, HomePage, ProfilePage, HeroDetailView, HeroListView
from django.urls import path
from . import views

urlpatterns = [
    path('hero', HeroListView.as_view(), name='hero'),
    path('<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('profile', ProfilePage.as_view()),
    path('', HomePage.as_view()),

] 


