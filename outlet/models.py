from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    userprofile_address = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class CartElement(models.Model):
    cartElement_userprofile = models.ForeignKey(UserProfile)
    cartElement_number = models.IntegerField()


class Cart(models.Model):
    cart_user = models.ForeignKey(UserProfile)
    cart_cartElement = models.ManyToManyField(CartElement)


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_slug = models.SlugField(max_length=255)
    item_description = models.TextField()
    item_category = models.ForeignKey(Category)
    item_tags = models.ManyToManyField(Tag)
    date_post = models.DateTimeField(auto_now_add=True)
    item_price = models.FloatField()
    item_cartElement = models.ManyToManyField(CartElement, blank=True)
    item_weight = models.FloatField(blank=True)
    item_height = models.FloatField(blank=True)
    item_width = models.FloatField(blank=True)
    item_deep = models.FloatField(blank=True)
    item_brand = models.CharField(max_length=255)
    item_article = models.CharField(max_length=255)
    item_picture = models.ImageField(blank=True)
    item_liked = models.ManyToManyField(UserProfile, blank=True)


    def __str__(self):
        return self.item_name


class Order(models.Model):
    order_date = models.DateTimeField()
    order_cart = models.ForeignKey(CartElement)
    No_payment = 'NOP'
    Success_payment = 'SUP'
    Ready_to_ship = 'RTS'
    On_track = 'ONT'
    Achieved = 'ACH'
    Error_order = 'EIP'

    ORDER_STATUSES = (
        (No_payment, 'No payment'),
        (Success_payment, 'Success payment'),
        (Ready_to_ship, 'Ready to ship'),
        (On_track, 'In delivering'),
        (Achieved, 'Achieved'),
        (Error_order, 'Error in process'),
    )
    order_status = models.CharField(max_length=3,choices=ORDER_STATUSES, default=No_payment)