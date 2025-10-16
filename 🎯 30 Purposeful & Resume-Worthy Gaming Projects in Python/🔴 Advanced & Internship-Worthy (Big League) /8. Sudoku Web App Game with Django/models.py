from django.db import models

class Puzzle(models.Model):
    name = models.CharField(max_length=100)
    board = models.TextField()  # store as 81-char string with 0 for blanks
