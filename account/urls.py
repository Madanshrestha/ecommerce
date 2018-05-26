from django.conf.urls import url
from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='user_register'),
    url(r'^login/', LoginView.as_view(), name='user_login'),
    url(r'^logout/', LogoutView.as_view(), name='user_logout'),
]