from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('diminishing/', views.diminishing, name='diminishing'),
    path('macro/', views.macro, name='macro'),
    path('slang/', views.slang, name='slang'),
    path('classes/', views.classes, name='classes'),
    path('classes/warrior/', views.warrior, name='warrior'),
    path('classes/paladin/', views.paladin, name='paladin'),
    path('classes/hunter/', views.hunter, name='hunter'),
    path('classes/rogue/', views.rogue, name='rogue'),
    path('classes/priest/', views.priest, name='priest'),
    path('classes/shaman/', views.shaman, name='shaman'),
    path('classes/mage/', views.mage, name='mage'),
    path('classes/warlock/', views.warlock, name='warlock'),
    path('classes/monk/', views.monk, name='monk'),
    path('classes/druid/', views.druid, name='druid'),
    path('classes/demonhunter/', views.demonhunter, name='demonhunter'),
    path('classes/deathknight/', views.deathknight, name='deathknight'),
    path('classes/<int:special>/', views.spec, name="specialization")
]
