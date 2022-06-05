from django.shortcuts import render
from .logic import SmsLogic, UserLogic
import json
from django.http import JsonResponse

# Create your views here.


def login(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise Exception(u"参数不正确")
    result = UserLogic.login(username=username, password=password)
    return JsonResponse(result)


def register(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    phone = data.get("phone")
    code = data.get("code")
    if not username or not password or not phone or not code:
        raise Exception(u"参数不正确")
    result = UserLogic.register(username=username, password=password, phone=phone, code=code)
    return JsonResponse(result)


def send_sms(request):
    data = json.loads(request.body)
    phone = data.get("phone")
    status = SmsLogic.send(phone=phone)
    return JsonResponse({"status": True})


def update_user(req):
    token = req.GET.get("token")
    if not token:
        raise Exception(u"请登录")
    data = json.loads(req.body)
    sex = data.get("sex")
    if sex not in [1, 2]:
        raise Exception(u"sex 参数错误")
    wechat = data.get("wechat")
    user = UserLogic.get_user_by_token(token=token)
    UserLogic.update_user(user=user, sex=sex, wechat=wechat)
    return JsonResponse({"status": True})

