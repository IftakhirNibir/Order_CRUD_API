from django.contrib import admin
from django.urls import path, include
from orders import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Order CRUD API",
        default_version='v1',
        description="API documentation for the Order CRUD application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', views.order_list),
    path('order_detail/<str:product_id>/', views.order_detail),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


