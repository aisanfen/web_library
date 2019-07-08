import json
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import models as auth_models
from libsys import models as libsys_models

# Create your views here.
from managersys.forms import LoginForms


def checkLogin(func):
    """
    查看session值用来判断用户是否已经登录
    :param func:
    :return:
    """

    def warpper(request, *args, **kwargs):
        if request.session.get('username', False):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('managersys:login'))

    return warpper


@checkLogin
def index(request):
    content = {}
    print(request.session.items())
    content['page_name'] = "数据面板"
    content['reader_num'] = auth_models.User.objects.filter(is_superuser=0).count()
    content['book_num'] = libsys_models.Book.objects.count()
    content['borrowed'] = libsys_models.Book.objects.extra(where=['is_reservation=1']).count()
    content['fine'] = 0
    return render(request, "managersys/index.html", content)


def login(request):
    if request.session.get("username"):
        return redirect(reverse('managersys:index'))
    if request.method == "POST":
        login_froms = LoginForms(request.POST)
        if login_froms.is_valid():
            try:
                username = login_froms.cleaned_data['account']
                password = login_froms.cleaned_data['password']
                user = auth_models.User.objects.get(username=username)
                is_valid_password = check_password(password, user.password)
                if is_valid_password:
                    request.session['username'] = user.username
                    request.session['id'] = user.id
                    return redirect(reverse('managersys:index'))
                else:
                    return redirect(reverse('managersys:login'))
            except Exception as e:
                return redirect(reverse('managersys:login'))

    if request.method == "GET":
        return render(request, "managersys/login.html")


def logout(request):
    request.session.clear()
    response = HttpResponse(json.dumps({"status": 0}))
    response.delete_cookie('username')
    return redirect(reverse('managersys:index'))
    # return response


@checkLogin
def view_books(request, page=1):
    book_list = libsys_models.Book.objects.all().order_by("id")
    paginator = Paginator(book_list, 2000)
    books = paginator.page(page)
    content = {}
    content['page_name'] = "图书管理"
    content['books'] = books
    return render(request, "managersys/book_tables.html", content)


def view_message(request, page=1):
    content = {}
    message_list = libsys_models.Message.objects.all()
    paginator = Paginator(message_list, 2000)
    message_list = paginator.page(page)
    content['page_name'] = "留言列表"
    content['message_list'] = message_list
    return render(request, "managersys/message_tables.html", content)


@checkLogin
def delete_message(request, id=None):
    try:
        message = libsys_models.Message.objects.get(id=id)
        message.delete()
    except Exception as e:
        pass
    return redirect(reverse('managersys:view_message'))


@checkLogin
def edit_book(request, id):
    if request.method == "POST":
        book = libsys_models.Book.objects.get(id=id)
        book.name = request.POST.get("name")
        book.ISBN = request.POST.get("name")
        book.author = request.POST.get("author")
        # image_url = ""
        book.publish_name = request.POST.get("publish_name")
        book.location = request.POST.get("location")
        book.save()
        content = {}
        content['page_name'] = "图书编辑"
        book.publish_date = str(book.publish_date)
        book.image_url = "libsys/book_image/" + book.image_url + ".jpg"
        content['book'] = book
        return render(request, "managersys/edit_book.html", content)
    book = libsys_models.Book.objects.get(id=id)
    content = {}
    content['page_name'] = "图书编辑"
    book.publish_date = str(book.publish_date)
    book.image_url = "libsys/book_image/" + book.image_url + ".jpg"
    content['book'] = book
    return render(request, "managersys/edit_book.html", content)



@checkLogin
def delete_book(request, id):
    try:
        books = libsys_models.Book.objects.get(id=id)
        books.delete()
    except Exception as e:
        pass
    return redirect(reverse('managersys:default_viewbooks'))


@checkLogin
def add_book(request):
    content = {}
    content['page_name'] = "添加图书"
    if request.method == "GET":
        return render(request, "managersys/add_book.html", content)

    if request.method == "POST":
        return render(request, "managersys/add_book.html", content)


@checkLogin
def reader_manage(request, page=0):
    content = {}
    content['page_name'] = "读者管理"
    try:
        user_list = auth_models.User.objects.filter(is_superuser=0).all()
    except:
        user_list = None
    content['user_list'] = user_list
    return render(request, "managersys/user_tables.html", content)


@checkLogin
def user_profile(request):
    content = {}
    content['page_name'] = "个人信息"
    content['user_name'] = request.session.get("username")
    return render(request, "managersys/user-profile.html", content)


@checkLogin
def borrow(request):
    response = HttpResponse(json.dumps({"status": 0}))
    response.delete_cookie('username')
    return response
