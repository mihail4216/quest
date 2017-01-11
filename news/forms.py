from django.forms import ModelForm
from django import forms
from news.models import News, Comments


class NewsAddForm(ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'text',
            'avtor',
        )

    def save(self, user=None, commit=True):
        from_2 = super(NewsAddForm, self).save(commit=True)
        from_2.avtor = user
        from_2.save()
        return from_2


class CommentAddForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('title', 'text',)

