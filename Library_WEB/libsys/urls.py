from django.contrib import admin
from django.urls import path
from libsys import views as libsys_views

app_name = 'libsys'

urlpatterns = [
    path('', libsys_views.index, name='index'),
    path('about/', libsys_views.about, name='about'),
    path('search/', libsys_views.search, name='union_search'),
    path('bookrank/', libsys_views.book_rank, name='default_book_rank'),
    path('bookrank/<int:rank>', libsys_views.book_rank, name='book_rank'),
    path('messageboard/', libsys_views.message_board, name='message_board'),
    path('messageboarduser/', libsys_views.message_board_user, name='message_board_user'),
    path('newbooks/', libsys_views.new_books, name='default_new_books'),
    path('newbooks/<int:page>', libsys_views.new_books, name='new_books'),
    path('bookinfo/<int:id>', libsys_views.book_info, name='book_info'),
    path('login/', libsys_views.login, name='login'),
    path('404', libsys_views.page_404, name='404'),
]
