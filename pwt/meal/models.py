from django.db import models

# Create your models here.

from meal_plane.models import MealPlan
import uuid

class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal_plan_id = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
