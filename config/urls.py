from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.home.urls'), name='home'),
    path('mailings/', include('app.mailings.urls'), name='mailings'),
]
