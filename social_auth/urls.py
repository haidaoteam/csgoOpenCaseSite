from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from social_auth.views import LogoutView

urlpatterns = [
    url(r'^logout', login_required(LogoutView.as_view(), login_url='/'), name='logout')
]
