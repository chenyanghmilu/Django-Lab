from django.shortcuts import render
from django.http import HttpResponse


class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Name1', 'tabby', 'foul little demon', 3),
    Finch('Name2', 'tortoise shell', 'diluted tortoise shell', 0),
    Finch('Name3', 'black tripod', '3 legged cat', 4)
]


def home(request):
    return HttpResponse('<h1>Hello Finches</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })