import urllib
import json
from .documents import ChannelDocument, SearchDocument
from django.conf import settings
from .models import Channel, Search
from django.utils import timezone
import pytz

api_key = settings.GOOGLE_API_KEY
endpoint = 'https://www.googleapis.com/youtube/v3/'

class YouTubeRestAPI():
    def __init__(self, query):
        self.query = '+'.join(query.lower().split(' '))

    def channel_query(self):
        # search if username in database already
        s = SearchDocument.search().query("match", query=' '.join(self.query.split('+')))
        queryset = s.to_queryset()
        if len(queryset) > 0:
            print(queryset[0])
            # case channel already in database
            if queryset[0].success: 
                return Search.objects.filter(id=queryset[0].id)[0], Channel.objects.get(channel_id=queryset[0].channel_id)
            # return search object and None if no channel found
            return Search.objects.filter(id=queryset[0].id)[0], None

        # else make api request
        else:
            request = endpoint + 'channels?part=snippet,statistics,topicDetails&forUsername={}&key={}'.format(self.query, api_key)
            response = urllib.request.urlopen(request).read()
            data = json.loads(response)

            # case no results found for entered username
            if data['pageInfo']['totalResults'] == 0:
                search_obj = Search(
                        query       = ' '.join(self.query.split('+')),
                        success     = False,
                        channel_id  = None,
                        searched_at = timezone.now()
                )
                search_obj.save()
                return search_obj, None

            # case results found
            else:
                search_obj = Search(
                        query       = ' '.join(self.query.split('+')),
                        success     = True,
                        channel_id  = data['items'][0]['id'],
                        searched_at = timezone.now()
                )
                search_obj.save()

                channel_obj = Channel(
                        channel_id              = data['items'][0]['id'],
                        channel_username        = ' '.join(self.query.split('+')),
                        channel_name            = data['items'][0]['snippet']['title'],
                        channel_photo           = data['items'][0]['snippet']['thumbnails']['default']['url'],
                        subscriber_count        = data['items'][0]['statistics']['subscriberCount'],
                        video_count             = data['items'][0]['statistics']['videoCount'],
                        view_count              = data['items'][0]['statistics']['viewCount'],
                        country                 = data['items'][0]['snippet']['country'],
                        created_at              = data['items'][0]['snippet']['publishedAt']
                )
                channel_obj.save()
                return search_obj, channel_obj
