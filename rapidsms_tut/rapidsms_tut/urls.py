from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rapidsms.backends.kannel.views import KannelBackendView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # RapidSMS core URLs
    url(r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    # RapidSMS contrib app URLs
    url(r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    url(r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    url(r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    url(r'^registration/', include('rapidsms.contrib.registration.urls')),
    # Added for Borehole project 
    url(r'^borehole/', include('borehole.urls')),
    url(r'^webSMS/', include('webSMS.urls')), 
    url(r'^backend/kannel-fake-smsc/$',KannelBackendView.as_view(backend_name='kannel-fake-smsc')),
    url(r'^backend/kannel-usb0-smsc/$', KannelBackendView.as_view(backend_name='kannel-usb0-smsc')),
    url(r'^kannel/', include('rapidsms.backends.kannel.urls')),
    url(r"^account/", include("account.urls")), 
    # Third party URLs
    url(r'^selectable/', include('selectable.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
