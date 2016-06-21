from django.conf.urls import url, include
from . import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.register),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/auth/$', auth_views.auth_view),
    url(r'^accounts/logout/$', auth_views.logout),
    url(r'^accounts/loggedin/$', auth_views.loggedin),
    url(r'^accounts/invalid/$', auth_views.invalid_login),
    url(r'^accounts/register/$', auth_views.register),
    url(r'^accounts/register_success/$', auth_views.register_success),

]
