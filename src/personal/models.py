from django.db import models

# Create your models here.

PRIORITY = [
    ("H","High"),
    ("M", "Medium"),
    ("L", "Low")
]

class Question(model.models):
    title                   = models.charField(max_length=60)
    question                = Models.TextField(max_length=400)
    priority                = models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title