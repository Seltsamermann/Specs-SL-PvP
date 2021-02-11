from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import ClassName, Spec

# Create your views here.

def index(request):
    class_list = ClassName.objects.all()
    return render(request, 'main/index.html', {'class_list': class_list})


def diminishing(request):
    return render(request, 'main/diminishing.html')

def macro(request):
    return render(request, 'main/macro.html')

def slang(request):
    return render(request, 'main/slang.html')

def classes(request):
    return render(request, 'main/classes.html')

def warrior(request):
    return render(request, 'main/classes/warrior.html')

def paladin(request):
    return render(request, 'main/classes/paladin.html')

def hunter(request):
    return render(request, 'main/classes/hunter.html')

def rogue(request):
    return render(request, 'main/classes/rogue.html')

def priest(request):
    return render(request, 'main/classes/priest.html')

def shaman(request):
    return render(request, 'main/classes/shaman.html')

def mage(request):
    return render(request, 'main/classes/mage.html')

def warlock(request):
    return render(request, 'main/classes/warlock.html')

def monk(request):
    return render(request, 'main/classes/monk.html')

def druid(request):
    return render(request, 'main/classes/druid.html')

def demonhunter(request):
    return render(request, 'main/classes/demonhunter.html')

def deathknight(request):
    return render(request, 'main/classes/deathknight.html')

def spec(request, special):
    #pk - уникальный номер каждого спека (не внутри класса, а абсолютно)
    this_spec = Spec.objects.get(pk = special)
    #this_spec - объект класса Spec, который передаётся в переменной spec
    #в файл base_spec.html при помощи рендера (по крайней мере, я в это верю)
    return render(request, 'main/classes/base_spec.html', {'spec': this_spec})
