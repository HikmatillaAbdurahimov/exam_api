
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views
from django.urls import path,include


schema_view=get_schema_view(
    openapi.Info(
        title='spotify API docs',
        default_version='v1',
        description='API documentation',
        terms_of_service='https://www.gogle.com/policie/terms/',
        contact=openapi.Contact(email='contact@yourapi.local'),
        license=openapi.License(name='BSD license')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
