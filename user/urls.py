from django.urls import path

from .views import (
    login_form,
    recieving_sth_from_browser,
    sending_sth_to_browser,
    saying_hi_to_browser,
)

urlpatterns = [
    path("hi/", saying_hi_to_browser),
    path("get/", sending_sth_to_browser),
    path("post/", recieving_sth_from_browser),
    path("login_form/", login_form),
]
