from django.db import models

class KanjiSingle(models.Model):
    # NOTE: pkを明示的に指定しないとidがpkとして自動で設定されるらしい
    kanji = models.CharField(max_length=5)

class KanjiIdiom(models.Model):
    idiom = models.CharField(max_length=10)
