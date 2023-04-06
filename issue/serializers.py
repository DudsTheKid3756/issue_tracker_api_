from rest_framework import serializers

from .models import Reminder, Issue


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):
    reminder = ReminderSerializer(allow_null=True, required=False)

    class Meta:
        model = Issue
        fields = "__all__"

    def create(self, validated_data):
        reminder_instance = None
        if validated_data.__contains__("reminder"):
            reminder = validated_data.pop("reminder")
            reminder_instance = Reminder.objects.create(**reminder)
        issue = Issue.objects.create(**validated_data)
        issue.reminder = reminder_instance
        issue.save()
        return issue
