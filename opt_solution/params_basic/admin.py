from django.contrib import admin
from .models import Section, Option, Promotion, Student, TypeFraisAcademique, FraisAcademique, FraisAcademiqueStudent

admin.site.register(Section)
admin.site.register(Option)
admin.site.register(Promotion)
admin.site.register(Student)
admin.site.register(TypeFraisAcademique)
admin.site.register(FraisAcademique)
admin.site.register(FraisAcademiqueStudent)
