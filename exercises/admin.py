from django.contrib import admin
from .models import Person, Routine, Exercise

admin.site.register(Person)
admin.site.register(Routine)
admin.site.register(Exercise)
