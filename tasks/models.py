from django.db import models


class Task(models.Model):
    """Task of client"""
    NEW = 'NW'
    PLANNED = 'PL'
    INHAND = 'IH'
    COMPLETED = 'CL'
    STATUS = [
        ('NW', 'New'),
        ('PL', 'Planned'),
        ('IH', 'In hand'),
        ('CL', 'Completed'),
    ]
    name = models.CharField(max_length=200)
    stat = models.CharField(max_length=2, choices=STATUS, default=NEW,)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)

    def __str__(self):
        """Return string model"""
        return '%s %s %s' % (self.name, self.stat, self.text)


class Entry(models.Model):
    """Info about task"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string model"""
        return self.text
