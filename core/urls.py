from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
urlpatterns = [
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("__debug__/", include("debug_toolbar.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    path("admin/", admin.site.urls),
    path("auth/", include('authentication.urls', namespace='auth')),
    path("profile/", include('account.urls', namespace='profile')),
    path("basketball/", include('basketball.urls', namespace='basketball')),
    path("settings/", include('setting.urls', namespace='settings')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
