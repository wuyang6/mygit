"""DjangoDev URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from projects.views import index
"""
全局路径的配置信息
1.urlpatterns 为固定名称
2.列表中的一个元素，代表一条路由信息
3.从上到下匹配，如果能匹配上Django会自动调用path函数的第二个参数指定的视图（函数视图或者类）
4.如果匹配不上，会自动抛出一个404异常
5.一旦成功，不会继续匹配
"""





urlpatterns = {
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
}
