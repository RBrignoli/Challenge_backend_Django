from django.http import HttpResponse

def index(request):
    return HttpResponse("to no polls index.")
