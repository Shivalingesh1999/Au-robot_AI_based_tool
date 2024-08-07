from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
import json
from home.models import *
import pandas as pd

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def generate_random_data():
    #url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
    #r = requests.get(url)
    payload = pd.read_json('/root/04-01-2022/django_elastic_demo-master/home/data.json',lines=True)
    print(payload.get('keywords'))
    #print(df)
    #payload = json.loads(r.text)
    # count = 1
    # for data in payload.get('keywords'):
        # print(count)
        # ElasticDemo.objects.create(
            # Robot_name = data.get('Robot_name'),
            # content = data.get('variables')
        # )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})




class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)
        
  

