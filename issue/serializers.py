from rest_framework import serializers

from issue.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    reminder_time = serializers.TimeField()
    reminder_date = serializers.DateField()
    reminder_alert = serializers.CharField(max_length=15, allow_null=False)

    class Meta:
        model = Reminder
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    issue_reminder = ReminderSerializer(source="reminder")
    issue_title = serializers.CharField(max_length=28, allow_null=False)
    issue_comment = serializers.CharField(max_length=255, allow_null=False)

