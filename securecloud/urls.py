from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

admin.site.site_header = "Secure Cloud Manager Admin"

admin.site.site_title = "Secure Cloud Manager"

admin.site.index_title = "Welcome Admin"

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('manager.urls')),

]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)