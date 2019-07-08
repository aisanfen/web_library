from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(default='', null=False, max_length=255)
    ISBN = models.CharField(default='', null=False, max_length=255)
    author = models.CharField(default='', null=False, max_length=255)
    class_id = models.IntegerField(default=0)#图书种类
    publish_date = models.DateField(null=True)
    image_url = models.CharField(null=True,max_length=1024)#图书封面
    publish_name = models.CharField(null=True,max_length=1024)#出版社
    is_order = models.BooleanField(default=False, null=False)
    location = models.CharField(default="", null=True, max_length=255)
    UUID = models.CharField(default="", null=True, max_length=255)
    e_book_id = models.IntegerField(null=True)
    is_reservation = models.BooleanField(default=False, null=False)


# 借阅表
class Borrow(models.Model):
    book_id = models.IntegerField(default=0, null=False)
    reader_id = models.IntegerField(default=0, null=False)
    num = models.IntegerField(default='', null=False)
    book_name = models.CharField(default='', null=False, max_length=255)
    date = models.DateField(null=False)
    is_overdue = models.BooleanField(default=False, null=False)
    return_date = models.DateField(null=False)


# 读者等级
class ReaderLevel(models.Model):
    level = models.IntegerField(default=0, null=False)
    name = models.CharField(default='', null=False, max_length=255)


# 留言库
class Message(models.Model):
    name = models.CharField(default='', null=False, max_length=255)
    date = models.DateField(null=False)
    user_id = models.IntegerField(default=0, null=False)
    content = models.CharField(default='', null=False, max_length=255)
    parent_menu = models.CharField(default='', null=False, max_length=255)
    is_reading = models.BooleanField(default=False, null=False)


# 读者表
class Reader(models.Model):
    name = models.CharField(default='', null=False, max_length=255)
    book_num = models.IntegerField(default=0, null=False)
    max_num = models.IntegerField(default=0, null=False)
    account = models.CharField(default='', null=False, max_length=255)
    password = models.CharField(default='', null=False, max_length=255)
    level = models.IntegerField(default=0, null=False)
    overdue_time = models.IntegerField(default=0, null=False)


# 预定表
class Reserve(models.Model):
    book_id = models.IntegerField(default=0, null=False)
    reader_id = models.IntegerField(default=0, null=False)
    num = models.IntegerField(default=0, null=False)
    book_name = models.CharField(default='', null=False, max_length=255)
    data = models.DateField(null=False)
    is_overdue = models.BooleanField(default=False, null=False)


# 电子书表
class EBook(models.Model):
    name = models.CharField(default='', null=False, max_length=255)
    auther = models.CharField(default='', null=False, max_length=255)
    ISBN = models.CharField(default='', null=False, max_length=255)
    class_id = models.IntegerField(default=0, null=False)
    publish_data = models.DateField(null=False)
    is_order = models.BooleanField(default=False, null=False)
    location = models.CharField(default='', null=False, max_length=255)
    UUID = models.CharField(default='', null=False, max_length=255)
    lib_name = models.CharField(default='', null=False, max_length=255)
    is_open = models.BooleanField(default=False, null=False)


# 图书分类表

class BookClass(models.Model):
    class_name = models.CharField(default='', null=True, max_length=255)
