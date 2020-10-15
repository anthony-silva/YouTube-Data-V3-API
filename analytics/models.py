from django.db import models

# Table for storing search information
class Search(models.Model):
    id          = models.AutoField(primary_key=True)
    query       = models.CharField(max_length=120, blank=False)
    success     = models.BooleanField(default=None)
    channel_id  = models.CharField(max_length=120, default=None, null=True)
    searched_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "searches"

    def __str__(self):
        return str(self.query)



# Table for storing channel info
class Channel(models.Model):
    id                      = models.AutoField(primary_key=True)
    channel_id              = models.CharField(max_length=120, null=True)
    channel_username        = models.CharField(max_length=120, null=True)
    channel_name            = models.CharField(max_length=120, null=True)
    channel_photo           = models.CharField(max_length=200, null=True)
    subscriber_count        = models.BigIntegerField(null=True)
    video_count             = models.BigIntegerField(null=True)
    view_count              = models.BigIntegerField(null=True)
    country                 = models.CharField(max_length=20)
    created_at              = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.channel_name)


# Table for storing  video info
class Video(models.Model):
    id              = models.AutoField(primary_key=True)
    channel_id      = models.ForeignKey('Channel', on_delete=models.CASCADE)
    video_id        = models.CharField(max_length=120, null=True, blank=False)
    video_title     = models.CharField(max_length=200, null=True, blank=False)
    view_count      = models.BigIntegerField(null=True)
    likes           = models.BigIntegerField(null=True)
    dislikes        = models.BigIntegerField(null=True)
    genre           = models.CharField(max_length=50, null=True)
    created_at      = models.DateField()

    def __str__(self):
        return str(self.video_title)
