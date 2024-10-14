from django.db import models


import uuid
from user.models import User


class Progress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Storing weight with up to 2 decimal places
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage with up to 2 decimal places
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2)  # Muscle mass in kg
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Progress for {self.user.username} on {self.date}"
    
