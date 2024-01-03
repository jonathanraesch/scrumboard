from django import forms

from userstories.models import UserStory


class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ['title', 'story']

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'new-story-title'})
        self.fields['story'].widget.attrs.update({'class': 'new-story-body'})
