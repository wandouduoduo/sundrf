"""sunbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
import xadmin
from sunbackend.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')

# 配置codes的url
router.register(r'codes', SmsCodeViewset, base_name="codes")

# 配置用户注册的url
router.register(r'users', UserViewset, base_name="users")

# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 配置收货地址
router.register(r'address',AddressViewset , base_name="address")

# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 配置订单的url
router.register(r'orders', OrderViewset, base_name="orders")

# 配置首页轮播图的url
router.register(r'banners', BannerViewset, base_name="banners")

# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # rest_framework api 视图
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # api 文档视图
    url(r'docs/', include_docs_urls(title="豌豆多多")),

    url(r'^', include(router.urls)),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的token认证接口
    url('login/', obtain_jwt_token),
    # 支付宝
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    # 首页
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
]
