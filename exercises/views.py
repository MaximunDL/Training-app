from django.shortcuts import render, get_object_or_404
from .models import Person, Routine
from datetime import datetime

def person_routines(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    routines = person.routines.all()
    return render(request, 'routines/person_routines.html', {'person': person, 'routines': routines})

def routine_detail(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    exercises = routine.exercises.all()
    return render(request, 'routines/routine_detail.html', {'routine': routine, 'exercises': exercises})

def list_users(request):
    users = Person.objects.all()
    return render(request, 'list_users.html', {'users': users})

def routine_today(request, person_id):
    # Obtener el día de la semana actual
    today = datetime.today().strftime('%A').lower()  # Ejemplo: 'Monday'

    # Obtener al usuario
    person = get_object_or_404(Person, id=person_id)

    # Filtrar la rutina del día actual
    try:
        routine = Routine.objects.get(day=today, person=person)
        exercises = routine.exercises.all()
        print(f"Routine found: {routine.id} for {today}")
    except Routine.DoesNotExist:
        routine = None
        exercises = []
        print(f"No routine found for {today}")

    context = {
        'routine': routine,
        'person': person,
        'exercises': exercises
    }

    return render(request, 'routines/routine_detail.html', context)

