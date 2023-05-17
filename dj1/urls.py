"""
URL configuration for dj1 project.

The `urlpatterns` list routes URLs to view1. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function view1
    1. Add an import:  from my_app import view1
    2. Add a URL to urlpatterns:  path('', view1.home, name='home')
Class-based view1
    1. Add an import:  from other_app.view1 import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as view1
from app_Unicom import views as view2

urlpatterns = [
    path("admin/", admin.site.urls),
    # app1
    path("index/", view1.index),
    path("user/list", view1.user_list),
    path("user/add", view1.user_add),
    path("tpl/", view1.tpl),
    path("news/", view1.news),
    path("something/", view1.something),
    path("login/", view1.login),
    path("orm/", view1.orm),
    path("info/list/", view1.info_list),
    path("info/add/", view1.info_add),
    path('info/delete', view1.info_delete),
    # app_Unicom
    path("depart/list/", view2.depart_list),
    path("depart/delete/", view2.depart_delete),
]
