from django.shortcuts import redirect, render,get_object_or_404
from En.models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from index.models import *
# Create your views here.
def en_index(request):
    partniors = Partniors.objects.all()
    lang = "en"
    logos = Logo.objects.all()
    slider = Slider.objects.all()[:4]
    con = Contact.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    practices = Practice.objects.all()
    sosials = Sosials.objects.all()
    about = About.objects.all()
    members = Team.objects.all()
    ymembers = Team.objects.all()[:4]
    image = get_object_or_404(adminadmin,id = 1)
    p = 0
    for i in practices:
        p = p + 1
    s = 0
    for m in members:
        s = s + 1
    v = 0
    vacans = Vacancy.objects.all()
    for i in vacans:
        v = v + 1
    context = {
        "lang":lang,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "practices":practices,
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

def en_about(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    abouts = About.objects.all()[:1]
    teams = Team.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    title1 = "About us"
    title2 = "Mission"
    title3 = "Our Team"
    context = {
        "abouts":abouts,
        "lang":lang,
        "title1":title1,
        "title2":title2,
        "teams":teams,
        "title3":title3,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
        
    }
    return render(request,"about.html",context)

def en_contact(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    contacts = Contact.objects.all()[:1]
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    context = {
        "contacts":contacts,
        "lang":lang,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'contact.html',context)

def en_blog(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    lang = "en"
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    practices = Practice.objects.all()
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
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'blog.html',context)

def en_blog_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    post = get_object_or_404(Blog,key = key)
    selection = Blog.objects.all()[:6]
    practices = Practice.objects.all()
    lang = "en"
    context = {
        "post":post,
        "lang":lang,
        "selection":selection,
        "act_categories":act_categories,
        "services_categories":services_categories,
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'blog-single.html',context)

def en_act_category(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    cat = get_object_or_404(ActCategory,key=key)
    practices = Practice.objects.all()
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
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'act.html',context)

def en_act_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
    services_categories = ServiceCategory.objects.all()
    act_categories = ActCategory.objects.all()
    act_post = get_object_or_404(Act,key = key)
    practices = Practice.objects.all()
    context = {
        "lang":lang,
        "act_categories":act_categories,
        "act_post":act_post,
        "services_categories":services_categories,
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'act-single.html',context)

def en_service_category(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
    act_categories = ActCategory.objects.all()
    practices = Practice.objects.all()
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
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'services.html',context)

def en_service_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
    act_categories = ActCategory.objects.all()
    services_categories = ServiceCategory.objects.all()
    services_post = get_object_or_404(Service,key = key)
    practices = Practice.objects.all()
    context = {
        "lang":lang,
        "services_categories":services_categories,
        "services_post":services_post,
        "act_categories":act_categories,
        "practices":practices,
        "sosials":sosials,
        "con":con,
        "logos":logos,
    }
    return render(request,'services-single.html',context)

def en_practice(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
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

def en_practice_detail(request,key):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
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
        logos = Logo.objects.all()
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        jobs = form.cleaned_data.get("jobs")
        phone =  form.cleaned_data.get("phone")
        mail = form.cleaned_data.get("mail")
        new = Practice_form(practice=practice.title,name=name,surname=surname,jobs=jobs,phone=phone,email=mail)
        new.save()
        return redirect('Eng')
    return render(request,"practice-single.html",context)

def en_members(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
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

def en_joinus(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
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
        return redirect('Eng')
    return render(request,"joinus.html",context)

def en_vacancy(request):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    practices = Practice.objects.all()
    lang = "en"
    sosials = Sosials.objects.all()
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

def en_vacancy_detail(request,target):
    logos = Logo.objects.all()
    con = Contact.objects.all()
    sosials = Sosials.objects.all()
    practices = Practice.objects.all()
    lang = "en"
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