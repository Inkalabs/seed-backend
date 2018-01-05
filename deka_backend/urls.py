from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

frontend_modules = {
    'app': {
        'url': '',
        'view': 'index.html',
    }
}

frontend_urls = []
for module_name, module_data in frontend_modules.items():
    frontend_urls.append(path(
        module_data['url'],
        TemplateView.as_view(template_name=module_data['view']),
        name=module_name))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/log_viewer/', include(('log_viewer.urls', "log-viewer"), namespace='log-viewer')),
    # path('api/', include(api_urlpatterns, namespace='api')),
] + frontend_urls
