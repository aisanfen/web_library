import datetime

from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from libsys import models as libsys_models
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
            # return redirect(reverse('libsys:login'))
            return redirect(reverse('managersys:login'))
    return warpper


# Create your views here.

def login(request):
    if request.session.get("username"):
        return redirect(reverse('libsys:index'))
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
                    return redirect(reverse('libsys:index'))
                else:
                    return redirect(reverse('libsys:login'))
            except Exception as e:
                return redirect(reverse('libsys:login'))
    return render(request, "libsys/login.html")


def regist(request):
    if request.session.get("username"):
        return redirect(reverse('libsys:index'))
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
                    return redirect(reverse('libsys:index'))
                else:
                    return redirect(reverse('libsys:login'))
            except Exception as e:
                return redirect(reverse('libsys:login'))
    if request.method == "GET":
        return render(request, "libsys/login.html")


def logout(request):
    request.session.clear()
    return redirect(reverse('libsys:index'))


def index(request):
    context = {}
    context['page_name'] = "主页"
    return render(request, "libsys/index.html", context)


def search(request):
    context = {}
    if request.method == "POST":
        context['page_name'] = "检索结果"
        name = request.POST.get("name",default=None)
        author = request.POST.get("author",default=None)
        ISBN = request.POST.get("ISBN",default=None)
        publishdate = request.POST.get("publishdate",default=None)
        result=libsys_models.Book.objects.filter(Q(name__contains=name))
        name=""
        print(name=="",
              author=="",
              ISBN=="",
              publishdate=="")
        books=[]
        for book in result:
            book.image_url='libsys/book_image/'+book.image_url+".jpg"
            books.append(book)
        context['books']=books
        return render(request, "libsys/search_result.html", context)
    context['page_name'] = "高级检索"
    return render(request, "libsys/search.html", context)


def book_info(request, id):
    context = {}
    try:
        book = libsys_models.Book.objects.get(id=id)
        context['page_name'] = "图书信息"
        context['book'] = book
        book.image_url = 'libsys/book_image/' + book.image_url + ".jpg"
        return render(request, "libsys/book_information.html", context)
    except Exception as e:
        print(e)
    return redirect(reverse('libsys:union_search'))




@checkLogin
def borrow(request):
    if request.method == "POST":

        pass
    return redirect(reverse('libsys:404'))


def page_404(request):
    return HttpResponse("404 Not Found")

@checkLogin
def message_board_user(request):
    if request.method=="POST":
        username=request.session.get('username', False)
        user_id=request.session.get('id', False)
        if username:
            content=request.POST.get("content")
            message=libsys_models.Message.objects.create(content=content,name=username,
                                                         user_id=user_id,parent_menu=-1,
                                                         date=datetime.datetime.now()
                                                         )
    return redirect(reverse('libsys:message_board'))

def message_board(request):
    context = {}
    context['page_name'] = "留言板"
    message_list = libsys_models.Message.objects.all()
    context['message_list'] = message_list
    return render(request, "libsys/message_board.html", context)


def book_rank(request, rank=0):
    context = {}
    context['page_name'] = "借阅排行"
    result=libsys_models.Book.objects.all().order_by("class_id")[rank:rank+10]
    books=[]
    for re in range(0,len(result),2):
        books.append(result[re:re+2])
    context['books'] = books
    return render(request, "libsys/books_rank.html", context)


def new_books(request, page=0):
    context = {}
    context['page_name'] = "借阅排行"
    result = libsys_models.Book.objects.all().order_by("class_id")[page:page + 10]
    books = []
    for re in range(0, len(result), 2):
        books.append(result[re:re + 2])
    context['books'] = books
    return render(request, "libsys/new_books.html", context)


def about(request):
    return None
