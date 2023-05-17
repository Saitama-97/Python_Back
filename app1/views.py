from django.shortcuts import render, HttpResponse, redirect
from app1.models import UserInfo, Department


# Create your views here.


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 根据app的注册顺序，在每个app下的templates目录中寻找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, 'user_add.html')


def tpl(request):
    name = "韩超发方法"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "郭智", "salary": 100000, 'role': "CTO"}

    data_list = [
        {"name": "郭智", "salary": 100000, 'role': "CTO"},
        {"name": "卢慧", "salary": 100000, 'role': "CTO"},
        {"name": "赵建先", "salary": 100000, 'role': "CTO"},
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, 'n3': user_info, "n4": data_list})


def news(req):
    import requests
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news")
    data_list = res.json()
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关数据

    # 1.获取请求方式 GET/POST
    print(request.method)

    # 2.在URL上传递值 /something/?n1=123&n2=999
    print(request.GET)

    # 3.在请求体中提交数据
    print(request.POST)

    # 4.【响应】HttpResponse("返回内容")，内容字符串内容返回给请求者。
    # return HttpResponse("返回内容")

    # 5.【响应】读取HTML的内容 + 渲染（替换） -> 字符串，返回给用户浏览器。
    # return render(request, 'something.html', {"title": "来了"})

    # 6.【响应】让浏览器重定向到其他的页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.chinaunicom.com.cn/")

    # return HttpResponse("登录失败")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def orm(request):
    # Department.objects.create(title="后台")
    # Department.objects.create(title="前端")
    # Department.objects.create(title="算法")
    # return HttpResponse("添加成功")
    # Department.objects.filter(id=3).delete()
    # return HttpResponse("删除成功")
    # query_list = Department.objects.all()
    # for item in query_list:
    #     print(item.title)
    # print(query_list)
    # UserInfo.objects.all().delete()
    # UserInfo.objects.create(name="Alan", password="123", age=12)
    # UserInfo.objects.create(name="Bob", password="456", age=23)
    # UserInfo.objects.create(name="Calvin", password="789", age=35)
    result_list1 = UserInfo.objects.all()
    for result in result_list1:
        print(result.name, result.password, result.age)
    print("******")
    UserInfo.objects.filter(name="Alan").update(age=11)
    result_list2 = UserInfo.objects.all()
    for result in result_list2:
        print(result.name, result.password, result.age)
    return HttpResponse("result")


def info_list(request):
    result = UserInfo.objects.all()
    return render(request, "info_list.html", {"user_list": result})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    else:
        name = request.POST.get("name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        UserInfo.objects.create(name=name, password=password, age=age)
        return HttpResponse("添加成功")
