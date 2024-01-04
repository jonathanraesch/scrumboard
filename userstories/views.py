from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from userstories.forms import UserStoryForm
from userstories.models import UserStory


class HttpResponseSeeOther(HttpResponseRedirect):
    status_code = 303


class HttpResponseTemporaryRedirect(HttpResponseRedirect):
    status_code = 307


def index(request):
    new_story_form = UserStoryForm(request.path)
    if request.method == 'POST':
        new_story_form = UserStoryForm(request.path, request.POST)
        if new_story_form.is_valid():
            current_user = request.user
            if current_user.is_anonymous:
                current_user = None
            UserStory.objects.create(
                title=new_story_form.cleaned_data.get('title'),
                story=new_story_form.cleaned_data.get('story'),
                author=current_user
            )
            return HttpResponseSeeOther(new_story_form.cleaned_data.get('next_path'))

    story_list = UserStory.objects.order_by('-pub_date')
    context = {
        'story_list': story_list,
        'new_story_form': new_story_form,
    }
    return render(request, 'userstories/index.html', context=context)


def index_redirect(request):
    return HttpResponseTemporaryRedirect(reverse('userstories:index'))
