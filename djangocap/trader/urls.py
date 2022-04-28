from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme.html', views.aboutme, name="aboutme"),
    path('your_crypto.html', views.your_crypto, name="your_crypto"),
    path('delete/<pk>', views.delete, name="delete"),

]