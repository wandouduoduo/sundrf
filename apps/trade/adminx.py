# -*- coding: utf-8 -*-
# @Time    : 18/8/7 上午11:57
# @Author  : Sun
# @Version : v1.0
# @File    : adminx.py
import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "nums", ]
    model_icon = 'fa fa-shopping-cart'


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]
    model_icon = 'fa fa-list'

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)