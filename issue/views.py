import datetime

from rest_framework import status
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Issue
from .serializers import IssueSerializer


class IssueView(APIView):
    @staticmethod
    def get(request, pk=None):
        issue: Issue
        if pk:
            try:
                issue = Issue.objects.get(pk=pk)
            except Exception:
                raise NotFound(f"Issue with id: {pk} does not exist", status.HTTP_404_NOT_FOUND)
            serializer = IssueSerializer(issue)
            return Response(serializer.data, status=status.HTTP_200_OK)

        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        request.data["created"] = datetime.datetime.now().isoformat()
        issue_serializer = IssueSerializer(data=request.data)
        if issue_serializer.is_valid():
            issue_serializer.save()
            return Response({"status": "success", "data": issue_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": issue_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def patch(request, pk=None):
        issue = Issue.objects.get(pk=pk)

        serializer = IssueSerializer(issue, data=request.data, partial=True)

        if serializer.initial_data.get("has_reminder"):
            if serializer.initial_data.get("reminder") is None:
                raise NotAcceptable("Reminder field is required if 'has_reminder' field is True")

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    @staticmethod
    def delete(request, pk):
        issue: Issue
        try:
            issue = Issue.objects.get(pk=pk)
        except Exception:
            raise NotFound(f"Issue with id: {pk} does not exist")

        issue.delete()
        return Response({
            "status": "success",
            "message": f"Issue with id: {pk} deleted"
        }, status=status.HTTP_204_NO_CONTENT)
