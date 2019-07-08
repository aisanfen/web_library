from django.contrib import admin
from libsys import models as libsys_models


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_per_page = 10  # 默认为100条
    list_display = ["id", "name", "author", "ISBN"]
    pass

admin.site.register(libsys_models.Book, BookAdmin)

class EBookAdmin(admin.ModelAdmin):
    list_per_page = 10  # 默认为100条
    pass

admin.site.register(libsys_models.EBook, EBookAdmin)

class BorrowAdmin(admin.ModelAdmin):
    list_per_page = 10  # 默认为100条
    pass

admin.site.register(libsys_models.Borrow, BorrowAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_per_page = 10  # 默认为100条
    pass

admin.site.register(libsys_models.Message, MessageAdmin)


