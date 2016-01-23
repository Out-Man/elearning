"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#class based view
from django.views.generic import TemplateView
from rest_framework import routers

from videos.serializers import VideoViewSet

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)



urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^dj/admin/', include(admin.site.urls)),
    url(r'^contact/$', TemplateView.as_view(template_name='company/contact_us.html'), name='contact_us'),
    url(r'^$', 'elearning.views.home', name='home'),

    url(r'^projects/$', 'videos.views.category_list', name='projects'),
    url(r'^projects/(?P<cat_slug>[\w-]+)/$', 'videos.views.category_detail', name='project_detail'),
    url(r'^projects/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', 'videos.views.video_detail', name='video_detail'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]

#auth login/logout
urlpatterns += [
    url(r'^upgrade/$', 'billing.views.upgrade', name='account_upgrade'),
    url(r'^billing/$', 'billing.views.billing_history', name='billing_history'),
    url(r'^billing/cancel/$', 'billing.views.cancel_subscription', name='cancel_subscription'),
]

#auth login/logout
urlpatterns += [
    url(r'^account/$', 'accounts.views.account_home', name='account_home'),
    url(r'^login/$', 'accounts.views.auth_login', name='auth_login'),
    url(r'^logout/$', 'accounts.views.auth_logout', name='auth_logout'), 
    url(r'^register/$', 'accounts.views.auth_register', name='register'), 
]

urlpatterns += [
    url(r'^comment/(?P<id>\d+)$', 'comments.views.comment_thread', name='comment_thread'),
    url(r'^comment/create/$', 'comments.views.comment_create_view', name='comment_create'),
]

#Notifications
urlpatterns += [
    url(r'^notifications/$', 'notifications.views.all', name='notifications_all'),
    url(r'^notifications/ajax/$', 'notifications.views.get_notifications_ajax', name='get_notifications_ajax'),
    url(r'^notifications/(?P<id>\d+)/$', 'notifications.views.read', name='notifications_read'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)