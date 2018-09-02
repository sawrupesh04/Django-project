from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen

def home(request):
    return render(request, 'home.html')

def webscrapping(request):
    url = request.GET['url']
    tag = request.GET['tag']

    on_file = urlopen(url)
    soup = BeautifulSoup(on_file, 'html.parser')
    tags = soup(tag)
    tag_list = []
    for tag in tags:
        tag_list.append(tag)


    return render(request, 'webscrapping.html', {'url':url, 'soup':soup, 'tags': tag_list})
