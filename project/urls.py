"""sdalandingPage_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from apps.search.views import VideoSearchView

admin.site.site_title = 'Sam Dale Academy Administration'
admin.site.site_header = 'Sam Dale Academy LLC'

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
]

urlpatterns += [
    url(r'', include('apps.flatpage.urls', namespace='flatpage')),
    url(r'^videos/', include('apps.upload.urls', namespace='upload')),
    url(r'^search/?$', VideoSearchView.as_view(), name='video_search_view'), #override haystack view, custom url directs to custom view
    url(r'^our-blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^shop/', include('apps.shop.urls', namespace='shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


