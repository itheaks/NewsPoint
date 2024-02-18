from django.shortcuts import render

def main(request):
    return render(request, 'news/main.html')

def news1(request):
    return render(request, 'news/news1.html')

def news2(request):
    return render(request, 'news/news2.html')

def link(request):
    return render(request, 'news/link.html')

def prompt(request):
    return render(request, 'news/prompt.html')
