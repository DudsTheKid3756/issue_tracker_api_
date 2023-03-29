from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Heyo, it's the index path or whatever")
