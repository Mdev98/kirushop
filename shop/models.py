import uuid
from django.db import models
from django.core.validators import MinValueValidator
from authentication.models import Customer

# Create your models here.

class Size(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.code

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)

    def __str__(self) -> str:
        return self.name


    @property
    def preview(self):
        preview = self.image_set.filter(default=True).get()
        return preview.imageUrl

    

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    default = models.BooleanField(default=False, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.customer.username

    @property
    def total_cart_item(self) -> int:
        return sum([item.quantity  for item in self.cartitem_set.all()])

    @property
    def total_cart_item_price(self):
        return sum([item.total_price for item in self.cartitem_set.all()])


class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f"{self.item} - ({self.quantity})"

    @property
    def total_price(self):
        return self.item.price * self.quantity

class ShippingDetails(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.customer.username

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4)
    cart      = models.OneToOneField(Cart, on_delete=models.DO_NOTHING, null=True, blank=True)
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping  = models.OneToOneField(ShippingDetails, on_delete=models.DO_NOTHING)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self)-> uuid:
        return f'{self.order_id}_{self.customer.username}'



    

