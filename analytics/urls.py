from django.urls import path
from analytics.views import IndexView, ChannelAPI

app_name = 'analytics'
urlpatterns = [
    # ex: /results/
    path('', IndexView, name='index'),
    path('channel/api/', ChannelAPI, name="channel_api"),
]
