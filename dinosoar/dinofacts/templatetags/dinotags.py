from django import template

register = template.Library()

@register.filter   #need register & load #here we register the tag using decorator.
def first_letters(iterable):
    res = ""
    for item in iterable:
        res += item[0]
    
    return res  

@register.filter(name="nth_letters", is_safe=True) #the name is instedOf the name of the function
def other_letter(iterable, num):
    res = ""
    
    for item in iterable:
        if len(item)< num  or not item[num-1].isalpha():
            res+="*"
        else:
            res += item[num-1]
    return res


from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, mark_safe


@register.filter(needs_autoescape=True)
@stringfilter
def letter_count(value, letter, autoescape=True):
    if autoescape:
        value = conditional_escape(value) #escapping for input(make input as plain text )
        
    result = (
        f"<i>{value}</i> has <b>{value.count(letter)}</b> "
        f"instance(s) of the letter <b>{letter}</b>"
    )
    return mark_safe(result) #escaping for output(apply html)



@register.simple_tag
def mute(*args):
    return ""



from django.utils.html import escape, mark_safe
@register.simple_tag
def make_ul(iterable):
    content = ["<ul>"]
    
    for item in iterable:
        content.append(f"<li>{escape(item)}</li>")
        
    content.append("</ul>")
    content = "".join(content)
    return mark_safe(content)


@register.simple_tag(takes_context=True)
def dino_list(context, title):
    output = [f"<h2>{title}</h2><ul>"]
    
    for dino in context["dinosaurs"]:
        output.append(f"<li>{escape(dino)}</li>")
        
    output.append("</ul>")
    output = "".join(output)
    
    context["weight"] = "20 tons"
    
    return mark_safe(output)

