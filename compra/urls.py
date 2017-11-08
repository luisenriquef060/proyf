from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^producto/', views.nuevo, name ="nuevo"),
    url(r'^vendedor/', views.nuevoU, name ="nuevoU"),
    url(r'^$', views.home_view, name='home_view'),
    url(r'^upload$', views.upload_image_view, name='upload_image_view'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': settings.MEDIA_ROOT}),
    ]
