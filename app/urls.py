from app import views
from django.urls import path,include
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API for managing projects",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('projects',views.handleprojects, name="handleprojects"),
    path('projects/create', views.createProject, name='createProject'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
    path('projects/<int:id>/delete', views.delete_project, name='delete_project'),
     path('project/edit/<int:project_id>/', views.edit_project, name='edit_project'),
]
