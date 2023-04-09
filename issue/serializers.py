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

    def update(self, instance, validated_data):
        reminder = None
        if validated_data.__contains__("reminder"):
            reminder = validated_data.pop("reminder")
        instance.reminder = Reminder()
        instance.reminder.save()
        reminder_instance = instance.reminder

        instance.title = validated_data.get("title", instance.title)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.color = validated_data.get("color", instance.color)
        instance.create_by = validated_data.get("created_by", instance.created_by)
        instance.has_reminder = validated_data.get("has_reminder", instance.has_reminder)
        instance.is_completed = validated_data.get("is_completed", instance.is_completed)
        instance.save()

        if reminder is not None:
            reminder_instance.time = reminder.get("time", reminder_instance.time)
            reminder_instance.date = reminder.get("date", reminder_instance.date)
            reminder_instance.alert = reminder.get("alert", reminder_instance.alert)

        reminder_instance.save()

        if instance.has_reminder is False:
            instance.reminder = None

        instance.save()

        return instance
