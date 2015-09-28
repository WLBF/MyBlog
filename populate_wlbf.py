import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyBlog.settings')

import django
django.setup()

from wlbf.models import Category, Blog


def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_blog(cat=python_cat,
             title='How to learn Python',
             text='code code code code code code code code code code')

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Blog.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_blog(cat, title, text, views=0):
    p = Blog.objects.get_or_create(category=cat, title=title)[0]
    p.content = text
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting WLBF population script..."
    populate()
