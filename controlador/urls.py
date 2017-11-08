from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('compra.urls')),
    #url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),

]
