from django.contrib import admin
from django.urls import path, include
from Twit_app.urls import urlpatterns as Twitt_app_urls
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Twitter API',
        default_version='v1',
        description='Twitter clone',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('Twit_app.urls')),
    path(
        "docs/", schema_view.with_ui("swagger", cache_timeout=0), name="docs"
    ),
    path(
        "docs2/", schema_view.with_ui("redoc", cache_timeout=0), name="docs2"
    ),
    path('admin/', admin.site.urls),
]
