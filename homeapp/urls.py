from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('post/',views.create_post,name='post_page'),
    path('blog_view/',views.blog_view,name='blog_view'),
    
    
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)