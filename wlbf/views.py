from django.shortcuts import render
from wlbf.models import Category, Blog
from wlbf.forms import CategoryForm


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'wlbf/index.html', context_dict)


def about(request):
    return render(request, 'wlbf/about.html', {})


def category(request, category_name_slug):

    context_dict = {}

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
