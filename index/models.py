from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Sosials(models.Model):
    title = models.CharField(max_length=150,verbose_name="Sosial şəbəkənin adının bi kodu")
    link = models.CharField(max_length=150,verbose_name="Sosial şəbəkənin linki")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Sosial şəbəkə"
        verbose_name_plural = "Sosial şəbəkələr"
        ordering = ['-id']
        
class adminadmin(models.Model):
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    title = "admin sekil"

    def __str__(self):
        return self.title
    
class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name="Slaydın başlığı")
    content = models.CharField(max_length=150,verbose_name="Slaydın mətni")
    link = models.CharField(max_length=150,verbose_name="Slaydın gedəcəyi ünvan")
    title_en = models.CharField(max_length=150,verbose_name="Slaydın başlığı - en",blank=True,null=True)
    content_en = models.CharField(max_length=150,verbose_name="Slaydın mətni - en",blank=True,null=True)
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    item = models.CharField(max_length=150,verbose_name="Item",blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Slayd"
        verbose_name_plural = "Slaydlar"
        ordering = ['-id']

class Logo(models.Model):
    image = models.ImageField(verbose_name="Logo",blank = True, null = True)
    title = models.CharField(max_length=150,verbose_name="Logonun adı")
    link = models.CharField(max_length=150,verbose_name="Link",blank = True, null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logolar"

class Partniors(models.Model):
    image = models.ImageField(verbose_name="Logo")
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    item = models.CharField(max_length=150,verbose_name="Item",blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Partnior"
        verbose_name_plural = "Partniorlar"
