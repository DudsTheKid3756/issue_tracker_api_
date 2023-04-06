from django.urls import path

from .views import IssueView

urlpatterns = [
    path('', IssueView.as_view()),
    path('<int:pk>', IssueView.as_view())
]
