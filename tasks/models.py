from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Task of user"""
    NEW = 'New'
    PLANNED = 'Planned'
    INHAND = 'In hand'
    COMPLETED = 'Completed'
    STATUS = [
        ('New', 'New'),
        ('Planned', 'Planned'),
        ('In hand', 'In hand'),
        ('Completed', 'Completed'),
    ]
    name = models.CharField(max_length=200)
    stat = models.CharField(max_length=10, choices=STATUS, default=NEW)
    date_added = models.DateTimeField(auto_now_add=True)
    date_planned = models.DateTimeField('Planned finish time (YYYY-MM-DD HH-MM-SS):', auto_now_add=False, null=True)
    text = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return string model"""
        return '%s %s %s %s' % (self.name, self.stat, self.text, self.date_planned)
