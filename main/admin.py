from django.contrib import admin

from .models import ClassName, Spec, Spell, Slang, Diminishing


class SpecInline(admin.TabularInline):
    model = Spec
    extra = 0


class SpecAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Spec information', {'fields': ['class_name']}),
    ]
    inlines = [SpecInline]

class SpellInLine(admin.TabularInline):
    model = Spell
    extra = 0


class SpellAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Spell owner', {'fields': ['name']}),
    ]
    inlines = [SpellInLine]


admin.site.register(ClassName, SpecAdmin)
admin.site.register(Spec, SpellAdmin)
admin.site.register(Slang)
admin.site.register(Diminishing)
