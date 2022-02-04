from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api import views


schema_view = get_schema_view(
   openapi.Info(title="Fastener shop API", default_version='v1'),
   public=True,
   permission_classes=[permissions.AllowAny])

router = DefaultRouter()

router.register('category', views.CategoriesViewSet, basename='category')
router.register('card_details', views.CardDetailViewSet,
                basename='card_details')
router.register('card_products', views.ProductsViewSet,
                basename='card_products')


urlpatterns = [
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
          name='schema-swagger-ui'),
     path('', include(router.urls)),
]
