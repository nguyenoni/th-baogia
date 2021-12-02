from django.db import models
from django.db.models.fields.files import ImageField
from .libs import generate_uid, get_upload_to_folder
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên danh mục")
    slug = models.SlugField(unique=True, blank=True, max_length=500,verbose_name="URL")
    create_at = models.DateField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    @staticmethod
    def custom_slugs(slug):
        if slug is not None:
            obj_slug = Category.objects.filter(slug=slug).first()
            if obj_slug:
                return slug + '-' + str(obj_slug.id)
        return slug

    def save(self, *arg, **kwarg):
        self.slug = self.custom_slugs(slugify(self.name))
        super(Category, self).save(*arg, **kwarg)

    class Meta:
        verbose_name = "Danh mục sản phẩm"
        verbose_name_plural = "Danh mục sản phẩm"
        ordering = ['name']


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên sản phẩm")
    unique_product = models.CharField(max_length=20, unique=True, blank=True, verbose_name="UID sản phẩm")
    cover_image = models.ImageField(upload_to=get_upload_to_folder("products"), max_length=512, blank=True, verbose_name="Image")
    slug = models.SlugField(max_length=500, unique=True, blank=True,verbose_name="URL")
    price = models.FloatField(default=0, verbose_name="Giá")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category")
    quantity = models.IntegerField(default=0, verbose_name="Số lượng")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    @staticmethod
    def custom_slugs(slug):
        if slug is not None:
            obj_slug = Category.objects.filter(slug=slug).first()
            if obj_slug:
                return slug + '-' + str(obj_slug.id)
        return slug

    def save(self, *arg, **kwarg):
        self.unique_product = generate_uid("Product")
        self.slug = self.custom_slugs(slugify(self.name))
        super(Product, self).save(*arg, **kwarg)

    class Meta:
        verbose_name = "Sản Phẩm"
        verbose_name_plural = "Sản Phẩm"
        ordering = ['name']

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.price,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status
        }
# Dung tích
class Volume(models.Model):
    name = models.CharField(max_length=50, default= "", verbose_name="Tên dung tích")
    unique_volume = models.CharField(max_length=20, unique=True, blank=True, verbose_name="UID Dung tích")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="volume_product")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def save(self, *arg, **kwarg):
        self.unique_volume = generate_uid("Volume")
        super(Volume, self).save(*arg, **kwarg)
    
    class Meta:
        verbose_name = "Dung tích sản phẩm"
        verbose_name_plural = "Dung tích sản phẩm"
        ordering = ['name']

    def to_dict(self):
        return {
            "name": self.name,
            "unique_volume": self.unique_volume,
            "is_activate": self.status,
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
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "status": self.status,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    class Meta:
        verbose_name = "Nguyên liệu"
        verbose_name_plural = "Nguyên liệu"
        ordering = ['name']    

    def __str__(self):
        return self.name

# Bao bì cấp 1
class PackagingLevel1(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên bao bì cấp 1")
    type_packaging = models.CharField(max_length=50, default="", verbose_name="Loại bao bì")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name="packaging_level_1_product")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Dung tích", related_name="packagin_level1_volume")
    image = models.ImageField(upload_to=get_upload_to_folder("images"), max_length=512, blank=True, verbose_name="Image")
    type_material = models.CharField(max_length=255, default="", verbose_name="Chất liệu")
    quantity_provider_sell = models.IntegerField(default=0, verbose_name="Chất liệu NCC có thể bán")
    min_order = models.IntegerField(default=0, verbose_name="Min order")
    provider = models.CharField(max_length=255, default="", verbose_name="Nhà cung cấp")
    price = models.FloatField(default=0, verbose_name="Giá")
    quantity_can_order_with_price = models.IntegerField(default=0, verbose_name="Số lượng đặt hàng tương ứng với giá")
    time_to_send = models.TextField(default="", verbose_name="Thời gian giao hàng")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Bao bì cấp 1"
        verbose_name_plural = "Bao bì cấp 1"
        ordering = ['name']

    def to_dict(self):
        return {
            "name": self.name,
            "type_packaging": self.type_packaging,
            "image": self.image,
            "type_material": self.type_material,
            "quantity_provider_sell": self.quantity_provider_sell,
            "min_order": self.min_order,
            "provider": self.provider,
            "price": self.price,
            "quantity_can_order_with_price": self.quantity_can_order_with_price,
            "time_to_send": self.time_to_send,
            "note": self.note,
            "create_at": self.create_at,
            "update_at": self.update_at,
            "status": self.status
        }

    def __str__(self):
        return self.name

# Bao bì cấp 2
class PackagingLevel2(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên bao bì cấp 2")
    price = models.FloatField(default=0, verbose_name="Giá bao bì")
    type_packaging = models.CharField(max_length=50, default="", verbose_name="Loại bao bì")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="packaging_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="packaging_volume", verbose_name="Dung tích")
    note = models.TextField(default="", verbose_name="Ghi chú")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    class Meta:
        verbose_name = "Bao bì cấp 2"
        verbose_name_plural = "Bao bì cấp 2"
        ordering = ['name']

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "status": self.status,
            "create_at": self.create_at,
            "update_at": self.update_at
        }

    def __str__(self):
        return self.name

# Tem nhãn
class Stamp(models.Model):
    name = models.CharField(max_length=255, default="",verbose_name="Tên tem nhãn")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="stamp_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="stamp_volume", verbose_name="Dung tích")
    type_stamp = models.CharField(max_length=255, default="", verbose_name="Loại tem nhãn")
    price = models.FloatField(default=0, verbose_name="Giá")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Tem nhãn"
        verbose_name_plural = "Tem nhãn"
        ordering = ['name']

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "type_stamp": self.type_stamp,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update_at": self.create_at,
            "status": self.status
        }

# Nhân công đóng gói
class PackingWorker(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói chi phí công nhân đóng gói")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="packing_worker_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="packing_worker_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Nhân công đóng gói"
        verbose_name_plural = "Nhân công đóng gói"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }

# Công bố kiểm nghiệm
class Announced(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói công bố kiểm nghiệm")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="annonced_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="annonced_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Công bố kiểm nghiệm"
        verbose_name_plural = "Công bố kiểm nghiệm"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }
#Phí vận chuyển
class FeeShipping(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói phí vận chuyển")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="fee_shipping_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="fee_shipping_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    note = models.TextField(default="", verbose_name="Ghi chú")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Vận chuyển"
        verbose_name_plural = "Vận chuyển"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }

    
# Hộp đựng sản phẩm
# class Box_Product(models.Model):
#     name = models.CharField(max_length=255, default="", verbose_name="Tên hộp đựng sản phẩm")
#     price = models.FloatField(default=0, verbose_name="Giá hộp đựng sản phẩm")
#     product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="box_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
#     volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="box_volume", verbose_name="Dung tích")
#     is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
#     create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
#     update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "price": self.price,
#             "is_activate": self.is_activate,
#             "create_at": self.create_at,
#             "update_at": self.update_at
#         }
#     def __str__(self):
#         return self.name

# Thùng caton
# class Carton_Box(models.Model):
#     name = models.CharField(max_length=255, default="", verbose_name="Tên thùng caton")
#     price = models.FloatField(default=0, verbose_name="Giá thùng caton")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carton_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
#     volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="carton_volume", verbose_name="Dung tích")
#     is_activate = models.BooleanField(default=True, verbose_name="Trạng thái")
#     create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
#     update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "price": self.price,
#             "is_activate": self.is_activate,
#             "create_at": self.create_at,
#             "update_at": self.update_at 
#         }
#     def __str__(self):
#         return self.name