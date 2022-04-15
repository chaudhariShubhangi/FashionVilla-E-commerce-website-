
from django.urls import path

from app1.views import homepage,testing


urlpatterns = [
    path('homepage/', homepage),
    path('base/', testing)
]
