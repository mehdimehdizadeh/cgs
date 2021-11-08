from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class About(models.Model):
    aboutus = RichTextField(verbose_name = "Haqqımızda")
    mission = RichTextField(verbose_name = "Missiya")
    image1 = models.ImageField(verbose_name = "Şəkil 1", blank = True, null = True)
    title = "Haqqımızda"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

class Team(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ad və soyad")
    position = models.CharField(max_length=150, verbose_name="Vəzifə")
    image = models.ImageField(verbose_name = "Şəkil", blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aktiv Üzv"
        verbose_name_plural = "Aktiv Üzvlərimiz"
        ordering = ['-id']

class Contact(models.Model):
    phone = models.CharField(max_length=150,verbose_name="Əlaqə nömrəsi")
    mail = models.CharField(max_length=150,verbose_name="Elektron poçt")
    locate = models.CharField(max_length=150,verbose_name="Ünvan")
    location = models.CharField(max_length=150,verbose_name="Xəritə")

    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqə"

class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name = "Məzmun")
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)
    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ['-id']

class ActCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Fəaliyyətin kateqoriyası"
        verbose_name_plural = "Fəaliyyətin kateqoriyaları"
        ordering = ['-id']

class Act(models.Model):
    act = models.ManyToManyField(ActCategory,verbose_name="Kateqoriya",blank=True)
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name = "Məzmun")
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Fəaliyyət"
        verbose_name_plural = "Fəaliyyətlər"
        ordering = ['-id']

class ServiceCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Xidmətin kateqoriyası"
        verbose_name_plural = "Xidmətin kateqoriyaları"
        ordering = ['-id']

class Service(models.Model):
    serv = models.ManyToManyField(ServiceCategory,verbose_name="Kateqoriya",blank=True)
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name = "Məzmun")
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"
        ordering = ['-id']

class Practice(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name = "Məzmun")
    image = models.ImageField(verbose_name="Şəkil",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Təlim"
        verbose_name_plural = "Təlimlər"
        ordering = ['-id']

class Practice_form(models.Model):
    practice = models.CharField(max_length=150,verbose_name="Təlimin adı",blank=True,null=True)
    name = models.CharField(max_length=150,verbose_name="Ad")
    surname = models.CharField(max_length=150,verbose_name="Soyad")
    jobs = models.CharField(max_length=150,verbose_name="İş yeri")
    phone = models.CharField(max_length=150,verbose_name="Telefon")
    email = models.CharField(max_length=150,verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Təlimin form səhifəsi"
        verbose_name_plural = "Təlimin form səhifəsi"
        ordering = ['-id']

class Joinus_form(models.Model):
    name = models.CharField(max_length=150,verbose_name="Ad")
    surname = models.CharField(max_length=150,verbose_name="Soyad")
    jobs = models.CharField(max_length=150,verbose_name="İş yeri")
    phone = models.CharField(max_length=150,verbose_name="Telefon")
    email = models.CharField(max_length=150,verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bizə qoşul"
        verbose_name_plural = "Bizə qoşul"
        ordering = ['-id']

class Vacancy(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    about = RichTextField(verbose_name = "İş haqqında")
    requirements = RichTextField(verbose_name = "Tələblər")
    email = models.CharField(max_length=150,verbose_name="Email",blank=True)
    target = models.CharField(max_length=150,verbose_name="data-target",blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vakansiya"
        verbose_name_plural = "Vakansiyalar"
        ordering = ['-id']