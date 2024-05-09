from django.urls import path
from app.home.apps import HomeConfig
from app.home.views import home


app_name = HomeConfig.name


urlpatterns = [
    path('', home, name='home'),
]