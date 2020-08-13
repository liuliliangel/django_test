"""evaluation_Djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from evaluationTest.views import GetStudent,GetStudentShortUrl,search_post,GetShortUidUrl
from evaluationTest import views
#导入views.py文件中的index函数

urlpatterns = [
    path('admin/',admin.site.urls),
    #path('',GetStudent),
    url(r'^search-Uid$', GetStudentShortUrl),
    url(r'^search-post$', search_post),
    url(r'^search-url$', GetShortUidUrl),

    #在url中凡是以url开头的访问都使用index函数来处理该请求
]

