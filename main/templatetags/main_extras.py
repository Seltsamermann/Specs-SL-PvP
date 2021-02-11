from django import template

from main.models import ClassName, Spec, Spell

register = template.Library()

@register.simple_tag
def filter_burst():
    max = len(Spell.objects.filter(kind="бурст").in_bulk())
    massive = [i+1 for i in range(max)]
    return massive

@register.simple_tag
def filter_save():
    max = len(Spell.objects.filter(kind="сейв").in_bulk())
    massive = [i+1 for i in range(max)]
    return massive

@register.simple_tag
def filter_cc():
    max = len(Spell.objects.filter(kind="контроль").in_bulk())
    massive = [i+1 for i in range(max)]
    return massive

@register.simple_tag
def filter_mobile():
    max = len(Spell.objects.filter(kind="мобильность").in_bulk())
    massive = [i+1 for i in range(max)]
    return massive

@register.simple_tag
def filter_utility():
    max = len(Spell.objects.filter(kind="утилити").in_bulk())
    massive = [i+1 for i in range(max)]
    return massive

@register.simple_tag
def class_spec_list(class_name):
    class_list = ClassName.objects.in_bulk()
    for i in class_list.keys():
        if class_list[i].class_name == class_name:
            return Spec.objects.filter(klass=i)

@register.simple_tag
def class_spec_count(class_name):
    spec_list = class_spec_list(class_name)
    return spec_list.count()


@register.simple_tag
def num_key(spell_list, num):
    num = int(num)
    return list(spell_list.keys())[num]

@register.simple_tag
def filter_spec_burst(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="бурст").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]


@register.simple_tag
def filter_spec_save(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="сейв").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]

@register.simple_tag
def filter_spec_cc(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="контроль").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]

@register.simple_tag
def filter_spec_mobile(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="мобильность").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]

@register.simple_tag
def filter_spec_utility(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="утилити").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]

@register.simple_tag
def filter_spec_coven(spek, num):
    num = int(num)
    spec_list = Spec.objects.in_bulk()
    for i in spec_list.keys():
        if spec_list[i].name == spek:
            main_list = Spell.objects.filter(spec=i).filter(kind="ковенант").in_bulk()
            try:
                key = list(main_list.keys())[num-1]
            except IndexError:
                return None
            else:
                return main_list[key]


@register.simple_tag
def max_class_abilities(name, type): #name - имя класса, type - бурст/сейв/..
    class_list = ClassName.objects.in_bulk()
    for i in class_list.keys():
        if class_list[i].class_name == name:
            main_list = Spec.objects.filter(klass=i) #это мы получили все спеки класса
            spell_count = 0
            for spec in main_list:
                spec_id = spec.id
                spell_count = max(spell_count, Spell.objects.filter(spec=spec_id).filter(kind=type).count())
            massive = [i+1 for i in range(spell_count)]
            return massive

@register.simple_tag
def spec_abilities(spec_id, type):
    spell_count = Spell.objects.filter(spec=spec_id).filter(kind=type).count()
    massive = [i+1 for i in range(spell_count)]
    return massive

@register.simple_tag
def class_translation(spec_id):
    if spec_id == 1 or spec_id == 2 or spec_id == 3:
        this_class = "paladin"
    elif spec_id == 4 or spec_id == 5 or spec_id == 6:
        this_class = "deathknight"
    elif spec_id == 7 or spec_id == 8:
        this_class = "demonhunter"
    elif spec_id == 9 or spec_id == 10 or spec_id == 11 or spec_id == 12:
        this_class = "druid"
    elif spec_id == 13 or spec_id == 14 or spec_id == 15:
        this_class = "monk"
    elif spec_id == 16 or spec_id == 17 or spec_id == 18:
        this_class = "warlock"
    elif spec_id == 19 or spec_id == 20 or spec_id == 21:
        this_class = "mage"
    elif spec_id == 22 or spec_id == 23 or spec_id == 24:
        this_class = "shaman"
    elif spec_id == 25 or spec_id == 26 or spec_id == 27:
        this_class = "priest"
    elif spec_id == 28 or spec_id == 29 or spec_id == 30:
        this_class = "rogue"
    elif spec_id == 31 or spec_id == 32 or spec_id == 33:
        this_class = "hunter"
    else:
        this_class = "warrior"
    return this_class
