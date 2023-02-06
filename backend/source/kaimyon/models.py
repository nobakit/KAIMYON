from django.db import models

# Create your models here.
# NOTE: pkを明示的に指定しないとidがpkとして自動で設定されるらしい


class KanjiSingle(models.Model):
    kanji = models.CharField(max_length=1, primary_key=True)

    def __str__(self):
        return self.kanji


class KanjiIdiom(models.Model):
    idiom = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.idiom


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.tag_id}: {self.tag_name}"


class KanjiTagRelation(models.Model):
    kanji = models.ForeignKey(KanjiSingle, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.kanji}, {self.tag}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["kanji", "tag"], name="unique_kanji_tag")
        ]


class IdiomTagRelation(models.Model):
    idiom = models.ForeignKey(KanjiIdiom, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.idiom}, {self.tag}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["idiom", "tag"], name="unique_idiom_tag")
        ]
