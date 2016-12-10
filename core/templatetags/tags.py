from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def edit_list(obj):
    url = reverse(
        'admin:{meta.app_label}_{meta.model_name}_change'.format(
            meta=obj._meta
        ), args=[obj.id]
    )
    html = u'<a href="{}" target="_blank">{}</a>'.format(
        url, obj.__unicode__()
    )
    return mark_safe(html)
