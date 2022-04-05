from random import choices
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from numpy import number

# class SampleModel(models.Model):
#     title = models.CharField(max_length=100)
#     number = models.IntegerField()

CATEGORY = (('business', 'ビジネス'), ('life', '生活'),('comic', 'マンガ'), ('other', 'その他'))
# CATEGORY2 = (('test', 'テスト'), ('test2', 'テスト2'),('test3', 'テスト3'), ('test4', 'テスト4'))

class Book(models.Model):
    title     = models.CharField(max_length=100)
    text      = models.TextField()
    category  = models.CharField(
                max_length=100,
                choices = CATEGORY
                )
    # category2 = models.CharField(
    #             max_length=100,
    #             choices = CATEGORY2
    #             )

    def __str__(self):
        return self.title