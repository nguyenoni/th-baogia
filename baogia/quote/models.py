from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên danh mục")
    slug = models.SlugField(default="", max_length=500,verbose_name="URL")
    create_at = models.DateField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Ngày cập nhật")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên sản phẩm")
    slug = models.SlugField(max_length=500, default="",verbose_name="URL")
    price = models.FloatField(default=0, verbose_name="Giá")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category")
    quantity = models.IntegerField(default=0, verbose_name="Số lượng")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return self.name

class Service_Costs(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói DV đính kèm")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    price_material = models.FloatField(default=0, verbose_name="Giá nguyên liệu")
    price_pack = models.FloatField(default=0, verbose_name="Giá đóng gói")
    packaging = models.FloatField(default=0, verbose_name="Bao bì")
    box = models.FloatField(default=0, verbose_name="Hộp")
    label_stamp = models.FloatField(default=0, verbose_name="Tem nhãn, phd, hdd")
    time_wait_product = models.TextField(default="", verbose_name="Thời gian chờ hàng")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return self.name

class ListQuotes(models.Model):
    # user, product, service, amount, sum
    product = models.ManyToManyField(Product,)