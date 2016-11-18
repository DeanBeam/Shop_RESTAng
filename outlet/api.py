__author__ = 'Kona'
from rest_framework import generics

from .serializers import CategorySerializer, TagSerializer, ItemSerializer, UserProfileSerializer, OrderSerializer, \
    CartSerializer
from .models import Category, Tag, Item, UserProfile, Order, Cart


class UserProfileMixin(object):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileList(UserProfileMixin, generics.ListAPIView):
    pass


class UserProfileDetail(UserProfileMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'


class CategoryMixin(object):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(CategoryMixin, generics.ListAPIView):
    pass


class CategoryDetail(CategoryMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'


class TagMixin(object):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagList(TagMixin, generics.ListAPIView):
    pass


class TagDetail(TagMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'


class ItemMixin(object):
    model = Item
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemList(ItemMixin, generics.ListAPIView):
    pass


class ItemDetail(ItemMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'


class OrderMixin(object):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderList(OrderMixin, generics.ListAPIView):
    pass


class OrderDetail(OrderMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'order_status'


class CartMixin(object):
    model = Cart
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartList(CartMixin, generics.ListAPIView):
    pass


class CartDetail(CartMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'cart_userprofile'