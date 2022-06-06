from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("sadmin/", admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("staff.urls")),
    path("", include("manager.urls")),
    path("admin/facilities/", include("map.urls")),
    path('admin/', include('django.contrib.auth.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "RHPN MAPPING SYSTEM"
admin.site.site_title = "RHPN MAPPING SYSTEM"
admin.site.index_title = ""