from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import  get_template
from django.template import Context,RequestContext
from django.views.generic.base import  TemplateView
from article.models import Article,Procedure,get_avg,Bookmark

from forms import ArticleForm, CommentForm, ProcedureForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def hello(request):
    name="frank"
    html="<p>Hi %s !!</p> "% name
    return HttpResponse(html)

def hello_template(request):
    name= "frank"
    t = get_template('hello.html')
    html= t.render(Context({'name':name}))
    return HttpResponse(html)

def hello_simple(request):
    name= "duan"
    context= RequestContext(request)
    return render_to_response('hello.html',{'name':name},context)

class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Mike'
        return context

def articles(request):
    language ='en-gb'
    session_language= 'en-gb'
    context = RequestContext(request)

    if 'lang' in request.COOKIES:
        language= request.COOKIES['lang']

    if 'lang' in request.session:
        session_language =request.session['lang']

    args = {}
    args.update(csrf(request))
    args['articles']=Article.objects.order_by('likes')[:3]
    args['language']=language
    args['session_language']=session_language


    return render_to_response('articles.html', args,context)

def article(request,article_id=1):
    context = RequestContext(request)
    a= Article.objects.get(id= article_id)
    editable = False
    if request.user.username == a.author:
        editable =True
    #if submit, authenticate and redirect
    if request.POST:
        form= ProcedureForm(request.POST, request.FILES)
        if form.is_valid():
            c= form.save(commit=False)
            c.article= a
            c.save()

            return HttpResponseRedirect('/article/get/%s' % article_id)
    #if no submit, create a form for user input
    else:
        form=ProcedureForm()

    args= {}
    args.update(csrf(request))

    args['form']= form
    args['article']= a
    args['avg_rating']= get_avg(article_id)
    args['editable']= editable

    return render_to_response('article.html',args,context)

@login_required()
def like_article(request):
    article_id = None
    like_count = 0
    if request.method == 'GET':
        article_id = request.GET.get('article_id')

    if article_id:
        a =Article.objects.get(id=article_id)
        count = a.likes
        count +=1
        a.likes=count
        like_count =  count
        a.save()

    return HttpResponse(like_count)


@login_required()
def add_comment(request,article_id):

    context = RequestContext(request)
    a = Article.objects.get(id=article_id)
    #submitted
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            #save but not sending to database, return an object
            c= f.save(commit=False)
            c.pubdate = timezone.now()
            c.name = request.user.username
            c.article= a
            c.save()

            return HttpResponseRedirect('/article/get/%s' % article_id)
    #first time load
    else:
        f= CommentForm()

    args= {}
    args.update(csrf(request))
    args['form']=f
    args['article']=a

    return render_to_response('add_comment.html',args,context)

def language(request,language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang',language)
    request.session['lang']= language
    return response

@login_required()
def create(request):
    #if submit, authenticate and redirect
    context = RequestContext(request)
    if request.POST:
        form= ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            c= form.save(commit=False)
            c.author = request.user.username
            c.save()

            return HttpResponseRedirect('/article/all')
    #if no submit, create a form for user input
    else:
        form= ArticleForm()

    args= {}
    args.update(csrf(request))

    args['form']= form

    return render_to_response('create_article.html',args,context )


def search_titles(request):
    if request.method =="POST":
        if request.POST['search_text'] != '':
            search_text = request.POST['search_text']

    else:
        search_text= None

    articles = Article.objects.filter(title__icontains=search_text)

    return render_to_response('ajax_search.html',{'articles':articles})

def search_pages(request):
    if request.method =="POST":
        if request.POST['search_text'] != '':
            search_text = request.POST.get('search_text')
    else:
        search_text= 'haha'

    articles= Article.objects.filter(title__icontains=search_text)


    args= {}
    args.update(csrf(request))
    args['articles'] = articles


    return render_to_response('result_page.html',args)


@login_required()
def add_bookmark(request):
    context = RequestContext(request)
    article_id = None

    if request.method == 'GET':
        article_id = request.GET.get('article_id')

    if article_id:
        userid = request.user.id
        c = Bookmark.objects.filter(user_id=userid,article_id=article_id)
        if c.count()>0:
            return HttpResponse("alert('already saved !')", mimetype="application/x-javascript")
        else:
            Bookmark.objects.create(user_id=userid,article_id=article_id)


    return HttpResponse("alert('saved !')", mimetype="application/x-javascript")

@login_required()
def delete_procedure(request):
    context = RequestContext(request)
    procedure_id =None

    if request.method == 'GET':
        procedure_id = request.GET.get('procedure_id')

    if procedure_id:
        a= Procedure.objects.get(id = procedure_id)
        a.delete()

    return HttpResponse("alert('deleted !')", mimetype="application/x-javascript")