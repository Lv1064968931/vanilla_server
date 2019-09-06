"""vanilla_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from login_app import views
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'login/',views.login,name='login'),
    url(r'register/',views.register,name='register'),
    url(r'verify/',views.get_phone_code,name='verify'),
    url(r'fetch/',views.fetch_random_word,name='fetch'),
    url(r'fetchsent/',views.fetch_random_sentence,name='fetchsent'),
    url(r'upload/',views.upload_userdata,name='upload'),
    url(r'download/',views.download_userdata,name='download'),
    url(r'uploadstrangeword/',views.upload_strangeword,name='uploadstrangeword'),
    url(r'downloadstrangeword/',views.download_strangeword,name='downloadstrangeword'),
    url(r'uploadclockingdata/',views.upload_clockingdata,name='uploadclockingdata'),
    url(r'downloadclockingdata/',views.download_clockingdata,name='downloadclockingdata'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url('^', include('login_app.urls')),
    url(r'', include('login_app.urls', namespace='login1')),
]
