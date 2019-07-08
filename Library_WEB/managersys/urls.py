from django.contrib import admin
from django.urls import path
from managersys import views as managersys_views

app_name = 'managersys'

urlpatterns = [
    path('', managersys_views.index, name='index'),
    path('viewbooks/<int:page>', managersys_views.view_books, name='viewbooks'),
    path('viewbooks/', managersys_views.view_books, name='default_viewbooks'),

    path('editbook/<int:id>', managersys_views.edit_book, name='editbook'),
    path('addbook/', managersys_views.add_book, name='addbook'),
    path('deletemessage/<int:id>', managersys_views.delete_message, name='delete_message'),
    path('deletebook/<int:id>', managersys_views.delete_book, name='delete_book'),

    path('userprofile/', managersys_views.user_profile, name='user_profile'),

    path('readermanage/<int:page>', managersys_views.reader_manage, name='reader_manage'),
    path('readermanage/', managersys_views.reader_manage, name='default_reader_manage'),

    path('viewmessage/', managersys_views.view_message, name='view_message'),

    path('borrow/', managersys_views.borrow, name='borrow'),
    path('logout/', managersys_views.logout, name='logout'),
    path('login/', managersys_views.login, name='login'),
]
