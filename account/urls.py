from django.conf.urls import url
from .views import login_page, register_page
from django.contrib.auth.views import LogoutView


urlpatterns = [
    url(r'^register/', register_page, name='user_register'),
    url(r'^login/', login_page, name='user_login'),
    url(r'^logout/', LogoutView.as_view(), name='user_logout'),
]
