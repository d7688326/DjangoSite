from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.template import RequestContext
from django.contrib.auth.models import User
from article.models import Bookmark,Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def profile(request,username):
    context = RequestContext(request)
    myworks = Article.objects.filter(author = username)
    user = User.objects.filter(username = username)
    uid = user.values()[0]['id']
    profile = UserProfile.objects.filter(user = uid)

    paginator = Paginator(myworks,3)

    page = request.GET.get('page')


    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render_to_response('author_profile.html',{'profile':profile,'articles':articles},context)


@login_required
def user_profile(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,instance= request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/display')

    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('edit_profile.html', args,context )

@login_required
def myprofile(request):
    context = RequestContext(request)
    user = request.user
    profile = user.profile
    ids = []
    collections = Bookmark.objects.filter(user_id = user.id).values('article_id')
    for x in range(0,collections.count()):
        ids.append(int(collections[x]['article_id']))

    article_list = Article.objects.filter(id__in=ids)

    paginator = Paginator(article_list,3)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render_to_response('myprofile.html',{'profile':profile,'articles':articles},context )

@login_required
def myworks(request):
    context = RequestContext(request)
    user = request.user
    profile = user.profile
    username = user.username
    myworks = Article.objects.filter(author = username)

    paginator = Paginator(myworks,3)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render_to_response('myworks.html',{'profile':profile,'articles':articles},context )

