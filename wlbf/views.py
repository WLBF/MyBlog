from django.shortcuts import render
from wlbf.models import Category, Blog
from wlbf.forms import CategoryForm, BlogForm


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'wlbf/index.html', context_dict)


def about(request):
    return render(request, 'wlbf/about.html', {})


def category(request, category_name_slug):

    context_dict = {'category_name_slug': category_name_slug}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        blogs = Blog.objects.filter(category=category)

        context_dict['blogs'] = blogs
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'wlbf/category.html', context_dict)


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


def blog(request, id):
    
    try:
        blog = Blog.objects.get(id=str(id))

    except Blog.DoesNotExist:
        raise Http404        
 
    return render(request, 'wlbf/blog.html', {'blog': blog})


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

    context_dict = {'form':form, 'category': cat}

    return render(request, 'wlbf/add_blog.html', context_dict)    
