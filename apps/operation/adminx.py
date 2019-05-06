# -*- coding: utf-8 -*-
# @Time    : 18/8/7 上午11:59
# @Author  : Sun
# @Version : v1.0
# @File    : adminx.py
import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]
    model_icon = 'fa fa-anchor'


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]
    model_icon = 'fa fa-info'


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]
    model_icon = 'fa fa-android'


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)