from .models import SmsCode, User, UserToken
import random
import time
from libs.sms import SmsLibs
from django.conf import settings


class UserLogic(object):

    @classmethod
    def update_user(cls, user, sex, wechat):
        user.sex = sex
        user.wechat = wechat
        user.save()

    @classmethod
    def get_user_by_token(cls, token):
        now = time.time()
        tokens = UserToken.objects.filter(token=token, expire_time__gte=now)
        if tokens.exists():
            user = tokens.first().user
            return user
        else:
            raise Exception("请登录")

    @classmethod
    def create_token(cls, user: User):
        now = time.time()
        expire_time = now + 7 * 24 * 3600
        token_obj = UserToken(user_id=user.id, expire_time=expire_time)
        token_obj.save()
        return token_obj.token

    @classmethod
    def register(cls, username, password, phone, code):
        if SmsLogic.check(phone=phone, code=code):
            if User.objects.filter(username=username).exists():
                raise Exception("该用户已存在")
            user = User(username=username, password=password, phone=phone)
            user.save()
            token = cls.create_token(user=user)
            return {
                "token": token
            }
        else:
            raise Exception("注册失败, 请重新注册")

    @classmethod
    def login(cls, username, password):
        users = User.objects.filter(username=username)
        if users.first():
            user = users.first()
            if user.password == password:
                token = cls.create_token(user=user)
                return {
                    "token": token
                }
            else:
                raise Exception("密码错误")
        else:
            raise Exception("该用户不存在")


class SmsLogic(object):

    @classmethod
    def send(cls, phone):
        """
            发送
        """
        code = random.randrange(100000, 999999)
        expire = int(time.time()) + settings.MAX_EXPIRE_TIME
        sms_code = SmsCode(code=code, expire_time=expire, phone=phone)
        sms_code.save()
        SmsLibs.send_yidong(phone, code)
        return sms_code

    @classmethod
    def check(cls, phone, code):
        n = time.time()
        is_valid = SmsCode.objects.filter(code=code, phone=phone, expire_time__gte=n, status=0).exists()
        if is_valid:
            SmsCode.objects.filter(code=code, phone=phone, expire_time__gte=n).update(status=1)
            return True
        else:
            return False