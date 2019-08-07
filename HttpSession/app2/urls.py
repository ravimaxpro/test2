from django.conf.urls import url
from .import views
app_name='app2'
urlpatterns=[
    url(r'^$',views.input,name='input'),
    url(r'^add$', views.add, name='add'),
    url(r'^display$', views.display, name='display'),
]