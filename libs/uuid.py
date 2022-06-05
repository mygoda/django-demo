import uuid
import random
import string


def create_uuid():
    return str(uuid.uuid4().hex)


def random_string(length=6):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def random_code(length=6):
    return ''.join(random.sample(string.digits, length))
