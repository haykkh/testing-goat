from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse(
        '<html>\n<title>To-Do</title>\n</html>'
        )