from django.contrib import admin
from .models import *
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ["title",'id']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','position','id']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone','mail','locate','id']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','key']

class ActivitesAdmin(admin.ModelAdmin):
    list_display = ['title','key']

class ActCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','key']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title','key']

class ServicesCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','key']


class PracticeAdmin(admin.ModelAdmin):
    list_display = ['title','key']

class Prictice_form_Admin(admin.ModelAdmin):
    list_display = ['name','id']

class JoinUs_form_Admin(admin.ModelAdmin):
    list_display = ['name','id']

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title','id']

admin.site.register(Vacancy,VacancyAdmin)
admin.site.register(Joinus_form,JoinUs_form_Admin)
admin.site.register(Practice,PracticeAdmin)
admin.site.register(Practice_form,Prictice_form_Admin)
admin.site.register(ServiceCategory,ServicesCategoryAdmin)
admin.site.register(Service,ServicesAdmin)
admin.site.register(ActCategory,ActCategoryAdmin)
admin.site.register(Act,ActivitesAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Team,TeamAdmin)
