from django.http import HttpResponse

# Create your views here.
def homePageViev(request):
    return HttpResponse('Hello, World!')