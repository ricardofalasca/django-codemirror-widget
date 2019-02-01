from django.db import models
from django import forms

from codemirror.widgets import CodeMirrorTextarea


class CodeMirrorField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': CodeMirrorFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class CodeMirrorFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': CodeMirrorTextarea})
        super().__init__(*args, **kwargs)
