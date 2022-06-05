from django.db import models
from user.models import User
# Create your models here.


class Host(models.Model):

    name = models.CharField(u"name", max_length=128)
    ip = models.CharField(u"ip", max_length=32)
    remark = models.CharField(u"remark", max_length=120)
    created_by = models.ForeignKey(User, verbose_name="创建用户", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "ip": self.ip,
            "remark": self.remark,
            "created_by": self.created_by.username
        }


class HostUserFavShip(models.Model):

    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    host = models.ForeignKey(Host, verbose_name="用户", on_delete=models.DO_NOTHING)
    is_valid = models.BooleanField("valid", default=True)

    def __str__(self):
        return self.user.username