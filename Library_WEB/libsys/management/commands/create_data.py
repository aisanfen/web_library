from django.core.management.base import BaseCommand

from libsys.management.commands.fake_data_book import fake_data_book
from libsys.management.commands.fake_data_borrow import fake_data_borrow
from libsys.management.commands.fake_data_user import fake_data_user


class Command(BaseCommand):
    help = 'Import init data for test'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('初始化模拟数据'))
        self.stdout.write(self.style.SUCCESS('载入图书数据'))
        try:
            fake_data_book()
        except Exception as e:
            print(e)
        self.stdout.write(self.style.SUCCESS('载入用户数据'))
        # try:
        #     fake_data_user()
        # except Exception as e:
        #     print(e)
        self.stdout.write(self.style.SUCCESS('载入借阅数据'))
        # try:
        #     fake_data_borrow()
        # except Exception as e:
        #     print(e)
        self.stdout.write(self.style.SUCCESS('结束载入'))