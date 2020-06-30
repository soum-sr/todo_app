from django.db import models

PRIORITY_CHOICES = (
    ('High', 'HIGH'),
    ('Mid', 'MIDIUM'),
    ('Low', 'LOW')
)
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default='Low')

    def __str__(self):
        return self.title