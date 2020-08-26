from django.http import HttpResponse

def index(requests):
    return HttpResponse('<h1>Hello Word</h1>')
