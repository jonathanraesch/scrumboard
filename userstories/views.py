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
    new_story_form = UserStoryForm()
    if request.method == 'POST':
        new_story_form = UserStoryForm(request.POST)
        if new_story_form.is_valid():
            current_user = request.user
            if current_user.is_anonymous:
                current_user = None
            UserStory.objects.create(
                title=new_story_form.cleaned_data.get('title'),
                story=new_story_form.cleaned_data.get('story'),
                author=current_user
            )
            return HttpResponseSeeOther(reverse('userstories:index'))

    elif request.method == 'GET':
        theme_param = request.GET.get('theme')
        if theme_param == 'dark':
            request.session['theme'] = 'dark'
        elif theme_param == 'light':
            request.session['theme'] = 'light'
        elif theme_param == 'toggle':
            current_theme = request.session.get('theme')
            if current_theme == 'light':
                request.session['theme'] = 'dark'
            else:
                request.session['theme'] = 'light'

    if not request.session.get('theme'):
        request.session['theme'] = 'dark'
    story_list = UserStory.objects.order_by('-pub_date')
    context = {
        'story_list': story_list,
        'new_story_form': new_story_form,
        'theme': request.session['theme'],
    }
    return render(request, 'userstories/index.html', context=context)


def index_redirect(request):
    return HttpResponseTemporaryRedirect(reverse('userstories:index'))
