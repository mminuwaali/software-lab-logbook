from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls")),
    path("", include("landing.urls")),
    path("student/", include("student.urls")),
    path("staff/", include("staff.urls")),
    path("blog/", include("blog.urls")),
    # path("summary/", include("summary.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
