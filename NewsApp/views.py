from django.shortcuts import render
import requests

# Create your views here.
API_KEY = 'd0b69496c18e463f888a273cb521ea9f'



def index(request):
    url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']
    context={
        'articles':articles
    }
    return render(request,'index.html',context)