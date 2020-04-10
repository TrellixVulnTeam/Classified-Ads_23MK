from django.conf.urls import url
from . import views
app_name = 'ads'


urlpatterns = [
     url(r'^$',views.all_ads, name='all_ads') ,
     url(r'^(?P<id>\d+)$', views.ads_detail , name='ads_detail'),
     url(r'^creat$', views.creat_ads , name='creat_ads'),
     url('ajax/load-cities/', views.load_sub, name='load_sub'),  # <-- this one here



    # url(r'^$',views.all_post, name='all_post' ) ,
    # url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),
    # url(r'^del/(?P<id>\d+)$', views.del_post, name='del_post'),
    # url(r'^test$', views.test, name='test'),

]
