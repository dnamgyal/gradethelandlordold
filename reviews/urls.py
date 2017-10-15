from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^review$', views.review_list, name='review_list'),
    url(r'^$', views.index, name='index'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    url(r'^landlord$', views.landlord_list, name='landlord_list'),
    url(r'^landlord/(?P<landlord_id>[0-9]+)/$', views.landlord_detail, name='landlord_detail'),
    url(r'^landlord/(?P<landlord_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
]
