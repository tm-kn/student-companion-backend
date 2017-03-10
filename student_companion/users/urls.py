from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register/$', views.RegisterUserView.as_view(), name='register'),
    url(r'^me/$', views.CurrentUserView.as_view(), name='current-user-detail')
]
