from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length  = 100)
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)
    description = models.TextField(max_length = 200, default = "description")
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    image = models.ImageField(upload_to = 'uploads/Product'  ,  default = 0)

    @staticmethod
    def get_products(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
             return Product.objects.filter(category = category_id)
        else:
             return Product.get_all_products();
class Customer(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 15)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email = email)


