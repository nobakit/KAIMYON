from django.db import models

# Create your models here.
# NOTE: pkを明示的に指定しないとidがpkとして自動で設定されるらしい

class KanjiSingle(models.Model):
    kanji = models.CharField(max_length=5, unique=True)
    # tag_1 = models.SmallIntegerField(max_length=4)
    # tag_2 = models.SmallIntegerField(max_length=4)
    # tag_3 = models.SmallIntegerField(max_length=4)

class KanjiIdiom(models.Model):
    idiom = models.CharField(max_length=10, unique=True)
    # tag_1 = models.SmallIntegerField(max_length=4)
    # tag_2 = models.SmallIntegerField(max_length=4)
    # tag_3 = models.SmallIntegerField(max_length=4)

class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)