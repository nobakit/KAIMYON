from django.contrib import admin
from .models import KanjiSingle, KanjiIdiom, Tag, KanjiTagRelation, IdiomTagRelation

# Register your models here.

admin.site.register(KanjiSingle)
admin.site.register(KanjiIdiom)
admin.site.register(Tag)

admin.site.register(KanjiTagRelation)
admin.site.register(IdiomTagRelation)