# -*- coding: utf-8 -*-
# @Time    : 18/8/7 上午11:54
# @Author  : Sun
# @Version : v1.0
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.views import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Goods, GoodsCategory, Banner, HotSearchWords
from .serializers import GoodsSerializer, CategorySerializer, BannerSerializer, IndexCategorySerializer, HotWordsSerializer
from .filters import GoodsFilter
# Create your views here.


class GoodsPagination(PageNumberPagination):
    """
        商品列表自定义分页
    """
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表页, 分页， 搜索， 过滤， 排序
    retrieve:
        获取商品详情
    """
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('-id')
    # 序列化
    serializer_class = GoodsSerializer
    # 分页
    pagination_class = GoodsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤
    filter_class = GoodsFilter
    # 搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')
    # 限速
    throttle_classes = (UserRateThrottle, AnonRateThrottle)

    # 商品点击数 + 1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    # 获取is_tab=True（导航栏）里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer
