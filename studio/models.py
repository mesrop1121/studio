from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    
    title = models.CharField(max_length=512,verbose_name="վերնագիր")
    img = models.ImageField(verbose_name='նկար')
    text = RichTextUploadingField(verbose_name="տեքստ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "արտադրանք"
        verbose_name_plural = "արտադրանքներ"

class Subscribe_email(models.Model):

    email = models.EmailField(max_length=256,verbose_name="Էլ․ փոստ")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Էլ․ փոստի բաժանորդագրություն"
        verbose_name_plural = "Էլ․ փոստի բաժանորդագրություններ"
