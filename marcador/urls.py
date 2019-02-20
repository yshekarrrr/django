from django.conf.urls import url
from .views import bookmark_user,bookmark_list

urlpatterns = [
    url(r'^user/(?<username>[-\w]+)/$', 'marcador.views.bookmark_user', name='marcador_bookmark_user'),
    url(r'^$', 'marcador.views.bookmark_list',name='marcador_bookmark_list'),
]