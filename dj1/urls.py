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
from app_Unicom import views as view2

urlpatterns = [
    path("admin/", admin.site.urls),
    # app_Unicom_depart
    path("depart/add/", view2.depart_add),
    path("depart/delete/", view2.depart_delete),
    path("depart/<int:nid>/edit/", view2.depart_edit),
    path("depart/list/", view2.depart_list),
    # app_Unicom_user
    path("user/add/", view2.user_add),
    path("user/delete/", view2.user_delete),
    path("user/<int:nid>/edit/", view2.user_edit),
    path("user/list/", view2.user_list),
]
