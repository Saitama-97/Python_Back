import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_Unicom.models import Department, UserInfo


# Create your views here.
def depart_add(request):
    if request.POST:
        depart_name = request.POST.get("title")
        Department.objects.create(title=depart_name)
        return redirect("/depart/list/")
    else:
        return render(request, "depart_add.html")


def depart_delete(request):
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    if request.POST:
        new_title = request.POST.get("title")
        Department.objects.filter(id=nid).update(title=new_title)
        return redirect("/depart/list/")
    else:
        depart = Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"depart_title": depart.title})


def depart_list(request):
    query_result = Department.objects.all()
    return render(request, "depart_list.html", {"query_result": query_result})


def user_add(request):
    if request.method == "GET":
        context = {
            'gender_choices': UserInfo.gender_choices,
            "depart_list": Department.objects.all()
        }
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库中
    UserInfo.objects.create(name=user, password=pwd, age=age,
                            account=account, create_time=ctime,
                            gender=gender, depart_id=depart_id)

    # 返回到用户列表页面
    return redirect("/user/list/")


def user_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


def user_edit(request, nid):
    context = {
        'gender_choices': UserInfo.gender_choices,
        "depart_list": Department.objects.all()
    }
    if request.POST:
        # 获取用户提交的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        account = request.POST.get('ac')
        ctime = request.POST.get('ctime')
        gender = request.POST.get('gd')
        depart_id = request.POST.get('dp')

        # 添加到数据库中
        UserInfo.objects.filter(id=nid).update(name=user, password=pwd, age=age,
                                               account=account, create_time=ctime,
                                               gender=gender, depart_id=depart_id)
        return redirect("/user/list/")
    else:
        user_info = UserInfo.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {"user_info": user_info, "context": context})


def user_list(request):
    queryset = UserInfo.objects.all()
    return render(request, "user_list.html", {"queryset": queryset})
