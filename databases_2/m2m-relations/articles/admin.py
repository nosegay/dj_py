
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_main = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                if has_main:
                    raise ValidationError('Указано несколько основных разделов')
                else:
                    has_main = True
        if not has_main:
            raise ValidationError('Требуется указать основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
