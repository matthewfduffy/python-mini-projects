def html_tag(tag):
    def wrapper(func):
        def inner(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return inner
    return wrapper


@html_tag('div')
def div(inner):
    return inner


@html_tag('i')
def italic(inner):
    return inner

print(div("Python"))        # <div>Python</div>
print(italic("Python"))     # <i>Python</i>


