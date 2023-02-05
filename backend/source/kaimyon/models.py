from django.db import models

# Create your models here.

class KanjiSingle(models.Model):
    kanji = models.CharField(max_length=5, primary_key=True)
    # tag_1 = models.SmallIntegerField(max_length=4)
    # tag_2 = models.SmallIntegerField(max_length=4)
    # tag_3 = models.SmallIntegerField(max_length=4)

class KanjiIdiom(models.Model):
    idiom = models.CharField(max_length=10, primary_key=True)
    # tag_1 = models.SmallIntegerField(max_length=4)
    # tag_2 = models.SmallIntegerField(max_length=4)
    # tag_3 = models.SmallIntegerField(max_length=4)

class Tag(models.Model):
    # NOTE: pkを明示的に指定しないとidがpkとして自動で設定されるらしい
    tag_name = models.CharField(max_length=30)