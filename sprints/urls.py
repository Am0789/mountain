from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Mountains API",
        default_version="v1",
        description="This API provides access to data and services for our project",
        terms_of_service="",  # Здесь может быть ссылка на условия использования (пустая строка в данном случае)
        contact=openapi.Contact(email="contact@example.com"),  # Здесь указывается контактный email
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html'), name='swagger-ui'),
    path('api/', include('mountains.urls')),
]