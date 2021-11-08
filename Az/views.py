from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Az.models import *
from .forms import *
from index.models import *
# Create your views here.
def az_index(request):
    partniors = Partniors.objects.all()
    logos = Logo.objects.all()
    slider = Slider.objects.all()[:4]
    con = Contact.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    members = Team.objects.all()
    ymembers = Team.objects.all()[:4] 
    practices = Practice.objects.all()
    sosials = Sosials.objects.all()
    image = get_object_or_404(adminadmin,id = 1)
    p = 0
    for i in practices:
        p = p + 1
    s = 0
    for m in members:
        s = s + 1
    vacans = Vacancy.objects.all()
    v = 0
    for i in vacans:
        v = v + 1
    lang = "az"
    about = About.objects.all()
    context = {
        "lang":lang,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "about":about,
        "s":s,
        "v":v,
        "p":p,
        "sosials":sosials,
        "image":image,
        "con":con,
        "slider":slider,
        "logos":logos,
        "partniors":partniors,
        "members":ymembers,
        "practices":practices,
    }
    return render(request,"index.html",context)

def az_about(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    abouts = About.objects.all()[:1]
    teams = Team.objects.all()
    lang = "az"
    title1 = "Haqqımızda"
    title2 = "Misiya"
    title3 = "Komandamız"
    context = {
        "abouts":abouts,
        "lang":lang,
        "title1":title1,
        "title2":title2,
        "title3":title3,
        "teams":teams,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,"about.html",context)

def az_contact(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    contacts = Contact.objects.all()[:1]
    lang = "az"
    context = {
        "contacts":contacts,
        "lang":lang,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'contact.html',context)

def az_blog(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    lang = "az"
    post_lists = Blog.objects.all()
    paginator = Paginator(post_lists,9)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
        "lang":lang,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'blog.html',context)

def az_blog_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    post = get_object_or_404(Blog,key = key)
    selection = Blog.objects.all()[:6]
    lang = "az"
    context = {
        "post":post,
        "lang":lang,
        "selection":selection,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'blog-single.html',context)

def az_act_category(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    lang = "az"
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    cat = get_object_or_404(ActCategory,key=key)
    act_posts_list = Act.objects.filter(act = cat)
    paginator = Paginator(act_posts_list,9)
    page = request.GET.get('page')
    try:
        act_posts = paginator.page(page)
    except PageNotAnInteger:
        act_posts = paginator.page(1)
    except EmptyPage:
        act_posts = paginator.page(paginator.num_pages)
    context = {
        "lang":lang,
        "act_categories":act_categories,
        "act_posts":act_posts,
        "services_categories":services_categories,
        "cat":cat,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'act.html',context)

def az_act_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    lang = "az"
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    act_post = get_object_or_404(Act,key = key)
    context = {
        "lang":lang,
        "act_categories":act_categories,
        "act_post":act_post,
        "services_categories":services_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'act-single.html',context)

def az_service_category(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    lang = "az"
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    cat = get_object_or_404(ServiceCategory,key=key)
    services_posts_list = Service.objects.filter(serv = cat)
    paginator = Paginator(services_posts_list,9)
    page = request.GET.get('page')
    try:
        services_posts = paginator.page(page)
    except PageNotAnInteger:
        services_posts = paginator.page(1)
    except EmptyPage:
        services_posts = paginator.page(paginator.num_pages)
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "services_posts":services_posts,
        "act_categories":act_categories,
        "cat":cat,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'services.html',context)

def az_service_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    lang = "az"
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    services_post = get_object_or_404(Service,key = key)
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "services_post":services_post,
        "act_categories":act_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'services-single.html',context)

def az_practice(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,"practice.html",context)

def az_practice_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    practice = get_object_or_404(Practice,key = key)
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    form = PracticeForm(request.POST or None)
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "practice":practice,
        "form":form,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    if form.is_valid():
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        jobs = form.cleaned_data.get("jobs")
        phone =  form.cleaned_data.get("phone")
        mail = form.cleaned_data.get("mail")
        new = Practice_form(practice=practice.title,name=name,surname=surname,jobs=jobs,phone=phone,email=mail)
        new.save()
        return redirect('Aze')
    return render(request,"practice-single.html",context)

def az_members(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    members = Team.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "members":members,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,"team.html",context)

def az_joinus(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    form = JoinusForm(request.POST or None)
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "form":form,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    if form.is_valid():
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        jobs = form.cleaned_data.get("jobs")
        phone =  form.cleaned_data.get("phone")
        mail = form.cleaned_data.get("mail")
        new = Joinus_form(name=name,surname=surname,jobs=jobs,phone=phone,email=mail)
        new.save()
        return redirect('Aze')
    return render(request,"joinus.html",context)

def az_vacancy(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    vacancies = Vacancy.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "vacancies":vacancies,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,"career.html",context)

def az_vacancy_detail(request,target):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "az"
    vacancy = get_object_or_404(Vacancy,target = target)
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "practices":practices,
        "act_categories":act_categories,
        "vacancy":vacancy,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,"career-single.html",context)