from django.http import HttpResponse

def Home(request):
    return HttpResponse("Server Running...")