from django.contrib import admin

# Register your models here.
from .models import *

class SosialsAdmin(admin.ModelAdmin):
    list_display = ['title','link','id']

class adminadminAdmin(admin.ModelAdmin):
    list_display = ['title']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','content','link']

class LogoAdmin(admin.ModelAdmin):
    list_display = ['title']

class PartniorAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Partniors,PartniorAdmin)
admin.site.register(Logo,LogoAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Sosials,SosialsAdmin)
admin.site.register(adminadmin,adminadminAdmin)