from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from random import choice
from .models import url_map
# Create your views here.


def create_short_url():
    qset=url_map.objects.all()
    short_urls=[x.short_url for x in qset]
    chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    short_url=''
    for i in range(6):
        short_url+=choice(chars)
    while short_url in short_urls:
        short_url=''
        for i in range(6):
            short_url+=choice(chars)
    return short_url


def createShorturl(request):
    short_url=''
    if request.method=='POST':
        data=request.POST
        long_url=data.get('longurl')
        print(str(long_url))
        lst=url_map.objects.filter(long_url=long_url)
        if lst.exists():
            short_url=lst[0].short_url
            return render(request,'show_url.html',context={'short_url':short_url})
        else:
            short_url=create_short_url()
            new_map = url_map(short_url=short_url, long_url=long_url)
            new_map.save()
            print(short_url)
            return render(request,'show_url.html',context={'short_url':short_url})
    return render(request,'home.html',context={'short_url':short_url})

def search(request,short_url):
    map_obj=url_map.objects.filter(short_url=short_url)
    if map_obj.exists():
        long_url=map_obj[0].long_url
        return redirect(long_url)
    else:
        return HttpResponseNotFound("Page not found", status=404)
    
def list(request):
    qset = url_map.objects.all()
    url_list=[]
    for q in qset:
        url_list.append({'short_url':q.short_url,'long_url':q.long_url})
    return render(request, "list.html", context={'url_list':url_list})