"""tukiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin, sitemaps
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from homeapp import sitemaps
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
# from django.views.static import serve
sitemaps = {
    'static':sitemaps.StaticViewSitemap,
    'blog_view':sitemaps.blog_view,
    'login':sitemaps.login,
    'logout':sitemaps.logout,
    'register':sitemaps.register


}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('',include('homeapp.urls')),
    path('',include('user.urls')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
