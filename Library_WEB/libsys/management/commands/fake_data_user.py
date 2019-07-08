import datetime
import random
import uuid

from django.contrib.auth.hashers import make_password

from Library_WEB import settings
from libsys import models as libsys_models
from django.contrib.auth import models as auth_models


def fake_data_user():
    user = auth_models.User.objects.filter(is_superuser=0).delete()
    def get_username():
        name_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return "".join([random.choice(name_list) for x in range(30)])
    def random_datetime():
        return datetime.datetime(random.randint(2015, 2017),  # year
                                 random.randint(1, 12),  # month
                                 random.randint(1, 28),  # day
                                 random.randint(0, 23),  # hour
                                 random.randint(0, 59),  # min
                                 random.randint(0, 59),  # sec
                                 random.randint(0, 100),  # microsecond
                                 datetime.timezone.utc if settings.USE_TZ else None)
    for x in range(500):
        username=get_username()
        print("user %s:" % x,username)
        user = auth_models.User.objects.create(password=make_password("admin"),
                                               is_superuser=0,
                                               is_staff=0,
                                               is_active=1,
                                               date_joined=random_datetime(),
                                               username=username)
        user.save()
