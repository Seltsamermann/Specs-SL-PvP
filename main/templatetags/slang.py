from django import template

from main.models import Slang, Diminishing

register = template.Library()


@register.simple_tag
def counter():
    count = Slang.objects.count()
    massive = [i+1 for i in range(count)]
    return massive

@register.simple_tag
def get_slang(num):
    return Slang.objects.get(pk = num)

@register.simple_tag
def type_counter():
    massive = [i+1 for i in range(5)]
    return massive

@register.simple_tag
def inner_counter(num): #эта штука должна вывести кол-во абилок типа num
    num = str(num)
    model = Diminishing.objects.filter(type=num)
    amount = model.count()
    massive = [i+1 for i in range(amount)]
    return massive

@register.simple_tag
def get_diminishing(num_type, num_order):
    type_list = [t+1 for t in range(5)]
    for i in type_list:
        if type_list[i-1] == num_type:
            main_list = Diminishing.objects.filter(type=str(i)).in_bulk()
            try:
                key = list(main_list.keys())[num_order-1]
            except IndexError:
                return None
            else:
                return main_list[key]

@register.simple_tag
def get_dim_name(num):
    if num == 1:
        return "Оглушение"
    elif num == 2:
        return "Паралич"
    elif num == 3:
        return "Дезориентация"
    elif num == 4:
        return "Обездвиживание"
    elif num == 5:
        return "Немота"
