"""Musicmp3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Musicmp3 import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(),name="index"),
    path('upload/',views.Upload.as_view(),name="upload"),
    path('view_all/',views.View_all.as_view(),name="view_all"),
    path('albums/',views.Albums.as_view(),name="albums"),
    path('artists/',views.Artists.as_view(),name="artists"),
    path('one_album/',views.One_album.as_view(),name="one_album"),
    path('one_song/',views.One_song.as_view(),name="one_song"),
    path('one_artist/',views.One_artist.as_view(),name="one_artist"),
    path('search/',views.search,name="search"),
    path('o_delete/',views.OpenDelete.as_view(),name="o_delete"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('a_login/',views.AdminLogin.as_view(),name='a_login'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('Logout/',views.Logout,name='Logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
