from django.db import models
from libs.uuid import create_uuid
# Create your models here.


class User(models.Model):
    """
        用户
    """

    SEX = (
        (1, "男"),
        (2, "女")
    )


    username = models.CharField(u"用户名", max_length=32, default="")
    password = models.CharField(u"密码", max_length=36, default="")
    phone = models.CharField(u"手机号", max_length=18, default="")

    wechat = models.CharField(u"微信号", max_length=18, default="")
    sex = models.IntegerField(u"性别", choices=SEX, default=1)

    is_valid = models.BooleanField(u"是否有效", default=True)

    def __str__(self):
        return self.username


class UserToken(models.Model):
    """
        token
    """

    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    token = models.CharField(u"token", max_length=36, default=create_uuid)
    expire_time = models.IntegerField(u"时间戳", default=0)

    def __str__(self):
        return self.token


class SmsCode(models.Model):
    """
        短信验证码
    """

    phone = models.CharField(u"手机号", max_length=16, default="")
    code = models.CharField(u"code", max_length=16, default="")
    status = models.BooleanField(u"是否使用", default=0)
    expire_time = models.IntegerField(u"时间戳", default=0)

    def __str__(self):
        return self.phone