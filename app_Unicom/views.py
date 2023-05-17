from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_Unicom.models import Department, UserInfo


# Create your views here.
def depart_list(request):
    query_result = Department.objects.all()
    return render(request, "depart_list.html", {"query_result": query_result})


def depart_delete(request):
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_test(request):
    return HttpResponse("Git Test123")
