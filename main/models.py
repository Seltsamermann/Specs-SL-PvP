from django.db import models

# Create your models here.


class ClassName(models.Model): #для работы с классами с 3 спеками
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class Spec(models.Model): #спек конкретного класса
    klass = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default="/static/main/images/") #относительная ссылка на картинку

    def __str__(self):
        return self.name

    def class_spec_list(self, class_name):
        class_list = ClassName.objects.in_bulk()
        for i in class_list.keys():
            if class_list[i].class_name == class_name:
                return self.objects.filter(klass=i)


class Spell(models.Model): #общий вид ячейки таблицы
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    kind = models.CharField(max_length=100, default="бурст") #бурст/сейв/контроль/мобил./другое
    image = models.CharField(max_length=100, default="/static/main/images/") #относительная ссылка на картинку
    name = models.CharField(max_length=100) #название спелла
    tier = models.CharField(max_length=100, default="Базовая способность") #можно с Integer: 0, если базовый, 1-7, если талант 1-7 тира, 8, если PvP-талант
    type = models.CharField(max_length=100, default="Инстант") #инстант, каст или пассивка
    cd = models.CharField(max_length=100, blank=True) #КД спелла
    explain = models.CharField(max_length=500, blank=True) #если не нужны выделения
    on_use = models.CharField(max_length=500, blank=True) #При использовании:
    on_duration = models.CharField(max_length=500, blank=True) #На время действия:
    radius = models.CharField(max_length=100, blank=True) #Радиус:
    buff_type = models.CharField(max_length=100, blank=True) #(не)дисп/пурж бафф/дебафф
    note = models.CharField(max_length=500, blank=True) #Примечание:

    def __str__(self):
        return self.name


class Slang(models.Model):
    slang = models.CharField(max_length=100)
    original = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        return self.slang


class Diminishing(models.Model):
    STUN = '1'
    INCAP = '2'
    BLIND = '3'
    ROOT = '4'
    SILENCE = '5'
    TYPE_CHOICES = [
        (STUN, 'Стан'),
        (INCAP, 'Паралич'),
        (BLIND, 'Ослепление'),
        (ROOT, 'Обездвиживание'),
        (SILENCE, 'Немота'),
    ] #цифры здесь нужны для цикла по типам диминишинга; в классах такой необходимости нет
    CLASSES = [
        ('Воин', 'Воин'),
        ('Паладин', 'Паладин'),
        ('Рыцарь смерти', 'Рыцарь смерти'),
        ('Охотник', 'Охотник'),
        ('Шаман', 'Шаман'),
        ('Охотник на демонов', 'Охотник на демонов'),
        ('Друид', 'Друид'),
        ('Разбойник', 'Разбойник'),
        ('Монах', 'Монах'),
        ('Маг', 'Маг'),
        ('Жрец', 'Жрец'),
        ('Чернокнижник', 'Чернокнижник'),
        ('Расовая способность', 'Расовая способность')
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=STUN)
    klass = models.CharField(max_length=100, choices=CLASSES, default='Воин')
    ability = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.ability
