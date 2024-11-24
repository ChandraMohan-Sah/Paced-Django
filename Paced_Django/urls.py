from django.contrib import admin
from django.urls import path, include

# Media File Namespace
from django.conf import settings
from django.conf.urls.static import static
from app8_authentication.app8_api import google_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.api.urls")),
    #social urls
    path('complete/google/', google_auth.google_callback, name='google_callback'),

    path('app1/', include("app1_static_nav.app1_api.urls")),
    path('app2/', include("app2_simple_form.app2_api.urls")),
    path('app3/', include("app3_contact_form.app3_api.urls")),
    path('app4/', include("app4_file_uploads.app4_api.urls")),
    path('app5/', include("app5_crud_operation.app5_api.urls")),
    path('app6/', include("app6_pfso.app6_api.urls")),
    path('app7/', include("app7_sessions.app7_api.urls")),
    path('app8/', include("app8_authentication.app8_api.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


