__author__ = 'Kona'
from rest_framework import serializers
from .models import Category, Tag, Item, UserProfile, Order, Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name','slug')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_name', 'item_slug', 'item_brand')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('cart_user', 'cart_element')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'userprofile_like')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_date', 'order_cart','order_status')