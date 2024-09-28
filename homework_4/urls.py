"""
URL configuration for homework_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import (
    main_page_view,
    TestView,
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view(), name='test'),
    path('', main_page_view, name='main_page'),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/parsing/', include('parser.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
