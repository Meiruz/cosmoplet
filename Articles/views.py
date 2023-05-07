from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.db import IntegrityError 
from .models import Article

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        articles = Article.objects.order_by("-date")

        return render(request, "Articles/home.html", {"title":"Cosmoplet | Главная", "cards":articles})
    return render(request, "Articles/home.html", {"title":"Cosmoplet | Главная", 'nav':True})


def loginuser(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['pass'])

        if user == None:
            return render(request, 'Articles/login.html', {"title":"Вход", "error":"Неверное имя пользователя или пароль."})
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'Articles/login.html', {"title":"Вход"})


def signup(request):
    if request.method == "POST":
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['pass1'])

                user.save()
                return redirect('home')
            except IntegrityError:
                return render(request, 'Articles/signup.html', {"title":"Регистрация", "error":"Такое имя пользователя уже существует. Выберите другое."})     
        else:
            return render(request, 'Articles/signup.html', {"title":"Регистрация", "error":"Пароли не совпадают! Попробуйте еще..."})
    else:
        return render(request, 'Articles/signup.html', {"title":"Регистрация"})
    

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    

def settings(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'Articles/settings.html', {"title":"Настройки профиля", "nav":True})

def view(request, l_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=l_pk)

        if article.slider1 == '':
            n = 0
        elif article.slider2 == '':
            n = 1
        elif article.slider3 == '':
            n = 2
        else:
            n = 3

        liked = request.user.liked.split(';')

        f = False
        for i in liked:
            if i == str(l_pk):
                f = True

        return render(request, 'Articles/view.html', {"title":article.title, "article":article, "nav":True, "n":n, "like":f})

def save(request, l_pk):
    if request.method == "POST":
        liked = request.user.liked.split(';')
        
        try:
            liked.remove(str(l_pk))
        except ValueError:
            liked.append(str(l_pk))

        new = ';'.join(liked)

        request.user.liked = new
        request.user.save()
        return redirect('more', l_pk=l_pk)


def marks(request):
    liked = request.user.liked.split(';')

    cards = []
    u = 0
    for i in liked:
        try:
            cards.append(get_object_or_404(Article, pk=int(i)))
        except:
            u = 1

    cards.reverse()
    return render(request, 'Articles/home.html', {"title":'Cosmoplet | Сохраненное', "cards":cards})
 