from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^find/', views.computeNthNumber, name='computeNthNumber'),
]
