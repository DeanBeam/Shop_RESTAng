from django.conf.urls import include, url
from django.conf import settings

from .api import UserProfileList, UserProfileDetail
from .api import CategoryList, CategoryDetail
from .api import TagList, TagDetail
from .api import ItemList, ItemDetail
from .api import OrderList, OrderDetail
from .api import CartList, CartDetail



userprofile_urls = [
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserProfileDetail.as_view(), name='user-detail'),
    url(r'^$', UserProfileList.as_view(), name='user-list')
]

category_urls = [
    url(r'^/(?P<slug>[0-9a-zA-Z_-]+)$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^$', CategoryList.as_view(), name='category-list')
]

tag_urls = [
    url(r'^/(?P<slug>[0-9a-zA-Z_-]+)$', TagDetail.as_view(), name='tag-detail'),
    url(r'^$', TagList.as_view(), name='tag-list')
]

item_urls = [
    url(r'^/(?P<slug>[0-9a-zA-Z_-]+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^$', ItemList.as_view(), name='item-list')
]

order_urls = [
    url(r'^/(?P<order_status>[0-9a-zA-Z_-]+)$', OrderDetail.as_view(), name='order-detail'),
    url(r'^$', OrderList.as_view(), name='order-list')
]

cart_urls = [
    url(r'^/(?P<cart_userprofile>[0-9a-zA-Z_-]+)$', CartDetail.as_view(), name='cart-detail'),
    url(r'^$', CartList.as_view(), name='cart-list')
]


urlpatterns = [
    url(r'^userprofile', include(userprofile_urls)),
    url(r'^category', include(category_urls)),
    url(r'^tag', include(tag_urls)),
    url(r'^item', include(item_urls)),
    url(r'^order', include(order_urls)),
    url(r'^cart', include(cart_urls)),
]
