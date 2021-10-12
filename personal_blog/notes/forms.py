from django.forms import ModelForm
from .models import Note, Topic, Category
from django import forms


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
        exclude = ('id',)

class NoteForm(ModelForm):
    order = forms.Select()
    class Meta:
        model = Note
        fields = ('title','summary','order','content',)

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('topic',)
        exclude = ('id',)
        