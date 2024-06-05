from django.db import models
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"

class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, related_name='routines', on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # e.g., 'monday', 'tuesday', etc.

    def __str__(self):
        return f"Routine for {self.person.name} on {self.day}"

class Exercise(models.Model):
    routine = models.ForeignKey(Routine, related_name='exercises', on_delete=models.CASCADE)
    index = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.URLField()
    youtube = models.URLField()
    repetitions = models.IntegerField()
    series = models.IntegerField()
    weight = models.FloatField()
    unit = models.CharField(max_length=10)
    previous_weight = models.FloatField()

    def __str__(self):
        return f"Exercise {self.index} - {self.name} in routine {self.routine.day}"
