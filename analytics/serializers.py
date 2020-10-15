from rest_framework import serializers
from analytics.models import Channel, Search, Video


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Channel
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search 
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Video
        fields = '__all__'