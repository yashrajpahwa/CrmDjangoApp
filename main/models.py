from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True,
                            help_text='Enter your name')
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True,
                            help_text='Enter the Tag')

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Both', 'Both'),
    )
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Delivery Pending', 'Delivery Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    status = models.CharField(
        max_length=255, null=True, blank=True, choices=STATUS)
    note = models.CharField(
        max_length=510, null=True, blank=True)

    def __int__(self):
        return self.id
