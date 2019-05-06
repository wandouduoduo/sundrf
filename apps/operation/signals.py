# -*- coding: utf-8 -*-
# @Time    : 18/8/8 下午3:25
# @Author  : Sun
# @Version : v1.0
# @File    : signal.py
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import UserFav


# post_save:接收信号的方式
# sender: 接收信号的model
@receiver(post_save, sender=UserFav)
def create_UserFav(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserFav)
def delete_UserFav(sender, instance=None, created=False, **kwargs):
        goods = instance.goods
        goods.fav_num -= 1
        goods.save()
