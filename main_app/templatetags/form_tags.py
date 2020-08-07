from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, classname):
    existing_classes = field.field.widget.attrs.get('class', None)
    if existing_classes:
        if existingclasses.find(given_class) == -1:
            classes = existing_classes + ' ' + classname
        else:
            classes = existing_classes
    else:
        classes = classname
    return field.as_widget(attrs={'class': classes})


# Got help from this article:
# https://ethanshearer.com/view-post/3/070519/sass-with-django-part2-bulma