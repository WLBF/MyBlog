from django.shortcuts import render
from wlbf.models import Category, Blog
from wlbf.forms import CategoryForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    blog = Blog.objects.all()[0]
    return render(request, 'wlbf/blog.html', {'blog':blog})

def about(request):
    return render(request, 'wlbf/about.html', {})


def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category.slug
        context_dict['category'] = category

        blogs = Blog.objects.filter(category=category).order_by('-post_time')
        paginator = Paginator(blogs, 10)
        page = request.GET.get('page')
        blog_list = []
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage :
            blog_list = paginator.paginator(paginator.num_pages)
        context_dict['blog_list'] = blog_list
    except Category.DoesNotExist:
        pass

    return render(request, 'wlbf/category.html', context_dict)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'wlbf/add_category.html', {'form': form})


def get_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404        
    return render(request, 'wlbf/blog.html', {'blog': blog})


@login_required
def add_blog(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if cat:
                blog = form.save(commit=False)
                blog.category = cat
                blog.views = 0
                blog.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = BlogForm()

    context_dict = {'form':form, 'category': cat, 'category_name_slug': category_name_slug}

    return render(request, 'wlbf/add_blog.html', context_dict)    

@login_required
def del_blog(request, category_name_slug):
    if request.method == 'GET':
        if 'blog_id' in request.GET:
            blog_id = request.GET['blog_id']
            try:
                Blog.objects.get(id=blog_id).delete()

            except Blog.DoesNotExist:
                raise Http404        
    return category(request, category_name_slug)



def track_url(request):
    blog_id = None
    url = '/wlbf/'
    if request.method == 'GET':
        if 'blog_id' in request.GET:
            blog_id = request.GET['blog_id']
            try:
                blog = Blog.objects.get(id=blog_id)
                blog.views = blog.views + 1
                blog.save()
                return get_blog(request, blog_id)
            except:
                pass

    return redirect(url)



def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)
    else:
        cat_list = Category.objects.all()        

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list



def suggest_category(request):
        cat_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']

        cat_list = get_category_list(8, starts_with)
        return render(request, 'wlbf/category_list.html', {'cat_list': cat_list })
