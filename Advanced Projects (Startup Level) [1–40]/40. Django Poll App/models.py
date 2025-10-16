from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
