from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from analytics.models import Channel, Video, Search
from analytics.serializers import ChannelSerializer, VideoSerializer, SearchSerializer
from django.http import JsonResponse 
from analytics.forms import SearchForm
from analytics.api import YouTubeRestAPI
import json
from django.forms.models import model_to_dict


# Create your views here.
def IndexView(request):
    template = 'index.html'
    form = SearchForm
    return render(request, template, {"form": form})

@api_view(['POST', 'GET'])
def ChannelAPI(request):
    if request.method == 'POST':
        form = SearchForm(request.POST or None)
        if form.is_valid():
            query = form.cleaned_data['search']
            search_obj, channel_obj = YouTubeRestAPI(query).channel_query()
            # serializer returned objects
            search_serializer = model_to_dict(search_obj)
            if channel_obj:
                channel_serializer = model_to_dict(channel_obj)
            else:
                channel_serializer = None
            print(channel_serializer)
            return JsonResponse({'search': search_serializer, 'channel': channel_serializer}, status=200)
    return JsonResponse({'request': 'failed'}, status=200)