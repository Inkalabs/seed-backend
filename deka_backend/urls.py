from django.contrib import admin
from django.urls import path, include


frontend_modules = {
    'app': {
        'url': '',
        'view': 'app/index.html',
    }
}

frontend_urls = []
# for module_name, module_data in frontend_modules.items():
#     frontend_urls.append(path(
#         module_data['url'],
#         AngularTemplateView.as_view(template_name=module_data['view']),
#         name=module_name))

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(api_urlpatterns, namespace='api')),
] + frontend_urls
