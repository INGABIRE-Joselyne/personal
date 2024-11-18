from django.urls import  path
from . import  views
from drf_spectacular.views import *

urlpatterns=[
    path('api/user',views.user_info,name='user_info'),
    path('api/Ternant',views.Ternant_info,name='Ternant_info'),
    path('api/schema',SpectacularAPIView.as_view(),name='schema'),
    path('api/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]