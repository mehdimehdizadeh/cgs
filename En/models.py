from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class About(models.Model):
    aboutus = RichTextField(verbose_name = "About")
    mission = RichTextField(verbose_name = "Mission")
    image1 = models.ImageField(verbose_name = "Image 1", blank = True, null = True)
    title = "About us"

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"

class Team(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name and surname")
    position = models.CharField(max_length=150, verbose_name="Position")
    image = models.ImageField(verbose_name = "Image", blank = True, null = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Active Member"
        verbose_name_plural = "Active Members"
        ordering = ['-id']

class Contact(models.Model):
    phone = models.CharField(max_length=150,verbose_name="Phone")
    mail = models.CharField(max_length=150,verbose_name="Email")
    locate = models.CharField(max_length=150,verbose_name="Address")
    location = models.CharField(max_length=150,verbose_name="Location")
    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    content = RichTextField(verbose_name = "Content")
    image = models.ImageField(verbose_name="Image",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-id']

class ActCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category of Action"
        verbose_name_plural = "Categories of Activites"
        ordering = ['-id']

class Act(models.Model):
    act = models.ManyToManyField(ActCategory,verbose_name="Category",blank=True)
    title = models.CharField(max_length=150,verbose_name="Title")
    content = RichTextField(verbose_name = "Content")
    image = models.ImageField(verbose_name="İmage",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Activites"
        ordering = ['-id']

class ServiceCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service category"
        verbose_name_plural = "Services Categories"
        ordering = ['-id']

class Service(models.Model):
    serv = models.ManyToManyField(ServiceCategory,verbose_name="Category",blank=True)
    title = models.CharField(max_length=150,verbose_name="Title")
    content = RichTextField(verbose_name = "Content")
    image = models.ImageField(verbose_name="İmage",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-id']

class Practice(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    content = RichTextField(verbose_name = "Content")
    image = models.ImageField(verbose_name="İmage",blank = True, null = True)
    key = models.CharField(max_length=150,verbose_name="keywords",blank=True,unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Practice"
        verbose_name_plural = "Practices"
        ordering = ['-id']

class Practice_form(models.Model):
    practice = models.CharField(max_length=150,verbose_name="Practice title",blank=True, null=True)
    name = models.CharField(max_length=150,verbose_name="Name")
    surname = models.CharField(max_length=150,verbose_name="Surname")
    jobs = models.CharField(max_length=150,verbose_name="Jobs")
    phone = models.CharField(max_length=150,verbose_name="Phone")
    email = models.CharField(max_length=150,verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Practice form page"
        verbose_name_plural = "Practice form page"
        ordering = ['-id']

class Joinus_form(models.Model):
    name = models.CharField(max_length=150,verbose_name="Name")
    surname = models.CharField(max_length=150,verbose_name="Surname")
    jobs = models.CharField(max_length=150,verbose_name="Jobs")
    phone = models.CharField(max_length=150,verbose_name="Phone")
    email = models.CharField(max_length=150,verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Join us"
        verbose_name_plural = "Join us"
        ordering = ['-id']

class Vacancy(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    about = RichTextField(verbose_name = "About work")
    requirements = RichTextField(verbose_name = "Requirements")
    email = models.CharField(max_length=150,verbose_name="Email",blank=True)
    target = models.CharField(max_length=150,verbose_name="data-target",blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        ordering = ['-id']