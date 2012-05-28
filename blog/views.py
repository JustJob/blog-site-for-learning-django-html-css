# Create your views here.
# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.forms import ModelForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    print request.GET
    paginator = Paginator(Blog.objects.all(), 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page if page is not None else 1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        print "the number of pages is: " + str(paginator.num_pages)
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': posts
    })

def view_post(request, slug):   
    print request.GET
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    print request.GET
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
    
def add_blog(request):
    class BlogForm(ModelForm):
        class Meta:
            model = Blog
            exclude = ('slug')
            
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            newBlog = form.save(commit=False)
            newBlog.set_slug()
            print 'the slug is : ' + newBlog.slug
            newBlog.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = BlogForm()
    return render_to_response('add.html', { 'form' : form }, context_instance = RequestContext(request))