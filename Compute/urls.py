from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

	url(r'^$', views.computeNthNumber, name='computeNthNumber'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
