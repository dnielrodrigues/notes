from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

"""
url config ...
--------------------------------------------------------------------------------
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
]
