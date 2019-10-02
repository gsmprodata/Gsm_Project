
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home.urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include(home.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
