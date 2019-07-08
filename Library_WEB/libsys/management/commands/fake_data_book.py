import datetime
import random
import uuid

from Library_WEB import settings
from libsys import models as libsys_models

def fake_data_book():
    books=libsys_models.Book.objects.all()
    def get_bool():
        boolen = [True, False]
        return boolen[random.randint(0,1)]

    def random_datetime():
        return datetime.datetime(random.randint(2015, 2017),  # year
                                 random.randint(1, 12),  # month
                                 random.randint(1, 28), # day
                                 random.randint(0, 23),  # hour
                                 random.randint(0, 59), # min
                                 random.randint(0, 59),  # sec
                                 random.randint(0, 100), #microsecond
                                 datetime.timezone.utc if settings.USE_TZ else None)

    for book in books:
        book.is_reservation=get_bool()
        book.is_order=get_bool()
        book.location="三楼A区"
        book.publish_name=random.choice(["清华大学出版社","机械工业出版社",
                                         "延边大学出版社","北京大学出版社"])
        book.publish_date=random_datetime()
        book.UUID=str(uuid.uuid4())
        book.save()
    pass