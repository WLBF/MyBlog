from django import template
from wlbf.models import Category
import markdown
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library() 


@register.filter(is_safe=True)  
@stringfilter  
def custom_markdown(value):
    print 'shit'
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))


@register.inclusion_tag('wlbf/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}
