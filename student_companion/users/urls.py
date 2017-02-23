from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^me/$', views.CurrentUserView.as_view(), name='current-user-detail')
]
