from django.conf.urls import url, include
from . import views as post_views

urlpatterns = [

    url(r'^$', post_views.calculate_view),
    url(r'^form/$', post_views.form_view),

]
