from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^blog/admin/', admin.site.urls),
    url(r'^blog/accounts/', include('django.contrib.auth.urls')),
    url(r'', include('blog.urls')),
]