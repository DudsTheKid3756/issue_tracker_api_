from django.db import models


class Reminder(models.Model):
    time = models.TimeField(null=False)
    date = models.DateField(null=False)
    alert = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f"rmndr{self.time}_{self.date}_{self.alert}"


class Issue(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE)
    title = models.CharField(max_length=28, null=False)
    comment = models.TextField(max_length=255, null=False)
    color = models.CharField(max_length=7, default="#000000")
    created_by = models.CharField(max_length=15, null=False)
    created = models.DateTimeField(null=False)
    has_reminder = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
