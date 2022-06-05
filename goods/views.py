from django.http import JsonResponse
from django.shortcuts import render
from user.logic import UserLogic
import json
from goods.models import Host
from .logic import HostLogic
# Create your views here.


def create_host(req):
    token = req.GET.get("token")
    if not token:
        raise Exception(u"请登录")
    user = UserLogic.get_user_by_token(token=token)
    data = json.loads(req.body)
    name = data.get("name")
    ip = data.get("ip")
    remark = data.get("remark")

    HostLogic.create(user=user, name=name, ip=ip, remark=remark)

    return JsonResponse({"status": True})


def user_fav_host(req):
    token = req.GET.get("token")
    if not token:
        raise Exception(u"请登录")
    user = UserLogic.get_user_by_token(token=token)
    data = json.loads(req.body)
    host_id = data.get("host_id")
    HostLogic.user_fav(user_id=user.id, host_id=host_id)
    return JsonResponse({"status": "收藏成功"})

def user_unfav_host(req):
    token = req.GET.get("token")
    if not token:
        raise Exception(u"请登录")
    user = UserLogic.get_user_by_token(token=token)
    data = json.loads(req.body)
    host_id = data.get("host_id")
    HostLogic.user_unfav(user_id=user.id, host_id=host_id)
    return JsonResponse({"status": "取消收藏成功"})


def get_user_fav_host(req):
    token = req.GET.get("token")
    if not token:
        raise Exception(u"请登录")
    user = UserLogic.get_user_by_token(token=token)
    hosts = HostLogic.get_user_fav_host(user_id=user.id)
    return JsonResponse({"hosts": hosts})


def host_list(req):
    data = req.GET
    ip = data.get("ip")
    queryset = Host.objects.all()
    if ip:
        queryset = queryset.filter(ip__icontains=ip)

    results = [host.to_json() for host in queryset]
    return JsonResponse({"results": results})