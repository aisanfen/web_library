import datetime
import random
import uuid

from django.contrib.auth.hashers import make_password

from Library_WEB import settings
from libsys import models as libsys_models
from django.contrib.auth import models as auth_models

def fake_data_borrow():
    books=libsys_models.Borrow.objects.all().delete()
    def get_bool():
        boolen = [True, False]
        return boolen[random.randint(0,1)]

    def random_datetime():
        return datetime.datetime(random.randint(2015, 2017),  # year
                                 random.randint(1, 12),  # month
                                 random.randint(1, 28),  # day
                                 random.randint(0, 23),  # hour
                                 random.randint(0, 59),  # min
                                 random.randint(0, 59),  # sec
                                 random.randint(0, 100),  # microsecond
                                 datetime.timezone.utc if settings.USE_TZ else None)

    books=libsys_models.Book.objects.all()
    users=auth_models.User.objects.all()
    for x in range(1000):
        book = random.choice(books)
        user = random.choice(users)
        date_=random_datetime()
        borrow=libsys_models.Borrow.objects.create(book_id=book.id,
                                                   num=1,
                                                   book_name=book.name,
                                                   return_date=date_,
                                                   date=date_+datetime.timedelta(days=30),
                                                   reader_id=user.id
                                                   )
        borrow.save()
    pass