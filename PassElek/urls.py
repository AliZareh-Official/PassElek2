from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
]
urlpatterns += i18n_patterns( path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('hakimizda/', aboutus, name='about_us'),
    path('iletsim/', iletsim, name='iletsim'),
    path('hizmetler/', hizmetler, name='hizmetler'),
    path('urunler/', include('products.urls')),
                              )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
