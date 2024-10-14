from django.db import models
import uuid
# Create your models here.


class ExerciseLibrary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50)  # e.g., strength, cardio
    muscle_groups = models.CharField(max_length=255)  # e.g., chest, triceps
    equipment = models.CharField(max_length=255)  # e.g., dumbbell, none
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
