"""cgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Az.views import *
from En.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('en/',en_index, name = "Eng"),
    path('',az_index,name="Az-first"),
    path('az/',az_index,name="Aze"),
    path('azabout/',az_about,name="azabout"),
    path('enabout/',en_about,name="enabout"),
    path('azcontact/',az_contact,name="azcontact"),
    path('encontact/',en_contact,name="encontact"),
    path('azblog/',az_blog,name="azblog"),
    path('azdetail/<str:key>',az_blog_detail,name="azdetail"),
    path('enblog/',en_blog,name="enblog"),
    path('endetail/<str:key>',en_blog_detail,name="endetail"),
    path('enactcategory/<str:key>',en_act_category,name="enactcategory"),
    path('enactdetail/<str:key>',en_act_detail,name="enactdetail"),
    path('azactcategory/<str:key>',az_act_category,name="azactcategory"),
    path('azactdetail/<str:key>',az_act_detail,name="azactdetail"),
    path('enservicecategory/<str:key>',en_service_category,name="enservicecategory"),
    path('enservicedetail/<str:key>',en_service_detail,name="enservicedetail"),
    path('azservicecategory/<str:key>',az_service_category,name="azservicecategory"),
    path('azservicedetail/<str:key>',az_service_detail,name="azservicedetail"),
    path('azpractice/',az_practice,name="azpractice"),
    path('azpracticedetail/<str:key>',az_practice_detail,name="azpracticedetail"),
    path('enpractice/',en_practice,name="enpractice"),
    path('enpracticedetail/<str:key>',en_practice_detail,name="enpracticedetail"),
    path('enmembers/',en_members,name="enmembers"),
    path('azmembers/',az_members,name="azmembers"),
    path('enjoinus/',en_joinus,name="enjoinus"),
    path('azjoinus/',az_joinus,name="azjoinus"),
    path('envacancies/',en_vacancy,name="envacancies"),
    path('azvacancies/',az_vacancy,name="azvacancies"),
    path('envacanciesdetail/<str:target>',en_vacancy_detail,name="envacanciesdetail"),
    path('azvacanciesdetail/<str:target>',az_vacancy_detail,name="azvacanciesdetail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

