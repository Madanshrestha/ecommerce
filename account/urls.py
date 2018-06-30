from django.conf.urls import url
from .views import login_page, register_page, guest_register_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^register/guest/$', guest_register_view, name="guest_register"),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
