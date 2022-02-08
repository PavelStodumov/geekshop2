from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    # path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('', include('social_django.urls', namespace='social')),
    path('order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
