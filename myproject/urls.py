
from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('article', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
