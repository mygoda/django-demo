from .models import Host, HostUserFavShip


class HostLogic():

    @classmethod
    def create(cls, user, name, ip, remark):
        host = Host(created_by_id=user.id, name=name, ip=ip, remark=remark)
        host.save()
        return host

    @classmethod
    def user_fav(cls, user_id, host_id):
        obj, created = HostUserFavShip.objects.get_or_create(user_id=user_id, host_id=host_id)
        obj.is_valid = True
        obj.save()

    @classmethod
    def user_unfav(cls, user_id, host_id):
        HostUserFavShip.objects.filter(user_id=user_id, host_id=host_id).update(is_valid=False)

    @classmethod
    def get_user_fav_host(cls, user_id):
        objs = HostUserFavShip.objects.filter(user_id=user_id, is_valid=True)
        host_ids = [obj.host_id for obj in objs]
        hosts = Host.objects.filter(id__in=host_ids)
        return [host.to_json() for host in hosts]