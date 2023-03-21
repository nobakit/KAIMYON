import random
import re

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *

# Create your views here.


def index(response):
    return HttpResponse("Hello, world! You're at the KAIMYON index.")


class TestBackendView(TemplateView):
    def get_kanji_single(self, tags=None):
        if tags is None:
            kanji_list = list(KanjiSingle.objects.all())
        else:
            kanjis = (
                KanjiTagRelation.objects.all()
                .select_related()
                .filter(tag__tag_name__in=tags)
            )
            kanji_list = list(kanjis.values_list("kanji_id", flat=True))
        return kanji_list

    def get_kanji_idiom(self, tags=None):
        if tags is None or tags == "普通":
            idiom_list = list(KanjiIdiom.objects.all())
        else:
            idioms = (
                IdiomTagRelation.objects.all()
                .select_related()
                .filter(tag__tag_name__in=tags)
            )
            idiom_list = list(idioms.values_list("idiom_id", flat=True))
        return idiom_list

    def generate_kaimyou(self, input_name, tags) -> str:
        # 戒名の出力文字数
        len_kaimyou = 8
        kaimyou = []

        kanji_from_name = random.choice(re.split("(.)", input_name)[1::2])
        kaimyou.append(kanji_from_name)

        # 熟語をランダムで取得
        num_idom = 2
        idioms = self.get_kanji_idiom(tags)
        if len(idioms) == 0:
            # DBにタグに関連する熟語が存在しなければ代わりに単漢字を取得
            kanji = random.choice(self.get_kanji_single(tags))
            kaimyou.append(random.choice(kanji))
        else:
            for i in range(num_idom):
                kaimyou.append(random.choice(idioms))

        num_single_kanji = len_kaimyou - len("".join(kaimyou))

        # 単漢字をランダムで取得
        for i in range(num_single_kanji):
            kanji = random.choice(self.get_kanji_single())
            kaimyou.append(str(kanji))

        # 文字列シャッフル
        random.shuffle(kaimyou)

        return "".join(kaimyou)

    def get(self, request, *args, **kwargs):
        # http://localhost:8000/kaimyon/test_db_ope?name=山田太郎&tag=強そう&tag=キラキラ
        name = request.GET.get("name")
        tag = request.GET.getlist("tag")
        # nameは空白削除の処理をかける
        name = name.replace(" ", "").replace("　", "")
        kaimyou = self.generate_kaimyou(name, tag)
        return HttpResponse(f"Your KAIMYOU: {kaimyou}")


test_db_ope = TestBackendView.as_view()
