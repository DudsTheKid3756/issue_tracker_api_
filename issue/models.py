from django.db import models


class Reminder(models.Model):
    time = models.TimeField()
    date = models.DateField()
    alert = models.CharField(max_length=15)

    def __str__(self):
        return f"rmndr{self.time}_{self.date}_{self.alert}"


class Issue(models.Model):
    reminder = models.ForeignKey(Reminder, models.CASCADE, null=True)
    title = models.CharField(max_length=28)
    comment = models.TextField(max_length=255)
    color = models.CharField(max_length=7, default="#000000")
    created_by = models.CharField(max_length=15)
    created = models.DateTimeField()
    has_reminder = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
