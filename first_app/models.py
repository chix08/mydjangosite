from django.db import models


#
# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.topic_name


class Name(models.Model):
    topic_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    topic = models.ForeignKey(to=Topic, on_delete=None)

    def __str__(self):
        return self.topic
