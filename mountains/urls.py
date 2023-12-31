from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CoordinateViewSet, ImageViewSet, UserViewSet, PassViewSet, submitData

router = routers.DefaultRouter()
router.register(r'coordinates', views.CoordinateViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'passes', views.PassViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/submit-data/', views.submitData, name='submit-data'),
    path('api/submit-data/<int:id>/', views.get_pass_by_id, name='get-pass-by-id'),
    path('api/submit-data/<int:id>/edit/', views.editData, name='edit-data'),  # Добавлен префикс "/edit/"
    path('api/submit-data/by-user-email/', views.getPassesByUserEmail, name='get-passes-by-user-email')
]
