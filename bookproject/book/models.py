from random import choices
from sre_constants import CATEGORY
from tabnanny import verbose
from unicodedata import category
from django.db import models
from numpy import number

from .consts import MAX_RATE

# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()

CATEGORY = (('business', 'ビジネス'), ('life', '生活'),('comic', 'マンガ'), ('other', 'その他'))
# CATEGORY2 = (('test', 'テスト'), ('test2', 'テスト2'),('test3', 'テスト3'), ('test4', 'テスト4'))

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
  title     = models.CharField(max_length=100)
  text      = models.TextField()
  category  = models.CharField(
              max_length=100,
              choices = CATEGORY
              )
  def __str__(self):
      return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title