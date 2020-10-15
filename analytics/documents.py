from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Search, Channel


@registry.register_document
class ChannelDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'channels'
        # See Elasticsearch Indices API reference for available settings
        settings = {}

    class Django:
        model = Channel # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'channel_id',
            'channel_username',
        ]


@registry.register_document
class SearchDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'searches'
        # See Elasticsearch Indices API reference for available settings
        settings = {}

    class Django:
        model = Search # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'query',
            'success',
            'channel_id',
            'searched_at',
        ]