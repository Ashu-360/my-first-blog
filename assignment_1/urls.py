from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^assign/$',views.form_handle,name = 'first_assign'),

]
