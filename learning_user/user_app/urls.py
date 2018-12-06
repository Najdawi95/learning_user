from django.conf.urls import url
from user_app import views

# TEMPLATE TAGGING
app_name = 'user_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.base, name='base'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^user_login/$', views.user_login, name='user_login'),

]
