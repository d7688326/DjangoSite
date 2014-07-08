__author__ = 'franklin'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyregistrationForm
from django.contrib.auth.decorators import login_required
from userprofile.forms import UserProfileForm
from django.template import RequestContext



def login(request):
    context = RequestContext(request)
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c,context )

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    context = RequestContext(request)
    return render_to_response('loggedin.html',
                                {'full_name':request.user.username},context)

def invalid_login(request):
    context = RequestContext(request)
    return render_to_response('invalid_login.html',context )

@login_required()
def logout(request):
    context = RequestContext(request)
    auth.logout(request)
    return render_to_response('logout.html',context )

def register_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = MyregistrationForm(request.POST)
        profile_form=UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # hash password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()


            return HttpResponseRedirect('/accounts/register_success')



    else:
        user_form = MyregistrationForm()
        profile_form = UserProfileForm()


    args={}
    args.update(csrf(request))

    args['user_form'] = user_form
    args['profile_form'] = profile_form

    return render_to_response('register.html',args,context)

def register_success(request):
    context = RequestContext(request)

    return render_to_response('register_success.html',context )

