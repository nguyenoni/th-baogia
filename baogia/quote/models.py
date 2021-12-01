from django.db import models
from .libs import generate_uid

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
    unique_product = models.CharField(max_length=20, default="", verbose_name="UID sản phẩm")
    slug = models.SlugField(max_length=500, default="",verbose_name="URL")
    price = models.FloatField(default=0, verbose_name="Giá")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category")
    quantity = models.IntegerField(default=0, verbose_name="Số lượng")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")

    def save(self, *arg, **kwarg):
        self.unique_product = generate_uid("Product")
        super(Product, self).save(*arg, **kwarg)

    def __str__(self):
        return self.name
    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.price,
            "price": self.price,
            "quantity": self.quantity
        }
# Dung tích
class Volume(models.Model):
    name = models.CharField(max_length=50, default= "", verbose_name="Tên dung tích")
    unique_volume = models.CharField(max_length=20, default="", verbose_name="UID Dung tích")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="volume_product")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def save(self, *arg, **kwarg):
        self.unique_volume = generate_uid("Volume")
        super(Volume, self).save(*arg, **kwarg)
    def to_dict(self):
        return {
            "name": self.name,
            "unique_volume": self.unique_volume,
            "is_activate": self.is_activate,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    def __str__(self):
        return self.name

# Nguyên liệu
class Material(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên nguyên liệu")
    price = models.FloatField(default=0, verbose_name="Giá nguyên liệu")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="material_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="material_volume", verbose_name="Dung tích")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "is_activate": self.is_activate,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    def __str__(self):
        return self.name

# Bao bì
class Packaging(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên bao bì")
    price = models.FloatField(default=0, verbose_name="Giá bao bì")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="packaging_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="packaging_volume", verbose_name="Dung tích")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "is_activate": self.is_activate,
            "create_at": self.create_at,
            "update_at": self.update_at
        }

    def __str__(self):
        return self.name
# Hộp đựng sản phẩm
class Box_Product(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên hộp đựng sản phẩm")
    price = models.FloatField(default=0, verbose_name="Giá hộp đựng sản phẩm")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="box_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="box_volume", verbose_name="Dung tích")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "is_activate": self.is_activate,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    def __str__(self):
        return self.name

# Thùng caton
class Carton_Box(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên thùng caton")
    price = models.FloatField(default=0, verbose_name="Giá thùng caton")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carton_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="carton_volume", verbose_name="Dung tích")
    is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "is_activate": self.is_activate,
            "create_at": self.create_at,
            "update_at": self.update_at 
        }
    def __str__(self):
        return self.name