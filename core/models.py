from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


class BaiViet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    baiviet = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
    content = models.TextField()


class YeuCau(models.Model):
    tenyeucau = models.CharField(max_length=255)
    loaiyeucau = models.IntegerField(default=0)


class NhaCungCap(models.Model):
    name = models.CharField(max_length=255)
    diachi = models.TextField()
    trangthai = models.IntegerField(default=0)


class NhaCungCapYeuCau(models.Model):
    yeucau = models.ForeignKey(YeuCau, on_delete=models.CASCADE)
    nhacungcap = models.ForeignKey(NhaCungCap, on_delete=models.CASCADE)
    thoigian = models.DateField(auto_now=True)
 