from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme.html', views.aboutme, name="aboutme"),
    path('your_crypto.html', views.your_crypto, name="your_crypto"),
    path('delete/<crypto_id>', views.delete, name="delete")
]