# -*- coding: utf-8 -*-
#
import logging

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from wechat.views import CustomWeChatView




class Command(BaseCommand):
    help = 'Automatically synchronize WeChat menu'

    logger = logging.getLogger('syncmenu')

    def handle(self, *args, **options):
        CustomWeChatView.update_menu()


Command.logger.setLevel(logging.DEBUG)
