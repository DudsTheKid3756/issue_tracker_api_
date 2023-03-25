from django.db import models

NONE = "NO_ALERT"
ON_TIME = "ON_TIME"
HALF = "HALF_HOUR"
ONE_HOUR = "ONE_HOUR"
TWO_HOURS = "TWO_HOURS"
ONE_DAY = "ONE_DAY"

ALERT_CHOICES = (
    (NONE, "No alert"),
    (ON_TIME, "On time"),
    (HALF, "Half hour"),
    (ONE_HOUR, "1 hour"),
    (TWO_HOURS, "2 hours"),
    (ONE_DAY, "1 day")
)


class Reminder(models.Model):
    time = models.TimeField()
    date = models.DateField()
    alert = models.CharField(
        max_length=10,
        choices=ALERT_CHOICES,
        default="No alert"
    )


class Issue(models.Model):
    title = models.CharField(max_length=28, null=False)
    comment = models.TextField(max_length=255, null=False)
    color = models.CharField(max_length=7, default="#000000")
    created_by = models.CharField(max_length=15, null=False)
    created = models.DateTimeField(null=False)
    has_reminder = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE)
