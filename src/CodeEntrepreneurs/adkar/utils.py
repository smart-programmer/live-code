from __future__ import unicode_literals

import random
import string

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''


def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "-")
    str = str.replace("؟", "-")
    return str


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return u''.join(random.choice(chars) for _ in range(size))


DONT_USE = ['My_Form']


def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = u"{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = u"{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


# Let's break this down a little (for extra context):
# What does Klass = instance.__class__ mean?

# What this does is set Klass to the actual model class that the instance comes from. That allows you to call things on it.

# Such as a QuerySet like Klass.objects.all().

# Klass could be User, Product, Profile, or many other models you created in your project.

# So the queryset: Klass.objects.filter(slug=slug) is looking up all instances of that particular class that matches your lookup call (slug=slug)

# Finally, adding .exists() returns a boolean value of whether or not the queryset exists.


from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 35)

#from shortener.models import KirrURL


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


def unique_code_generator(instance, code=None):
    if code is not None:
        new_code = code
    else:
        new_code = code_generator()

    klass = instance.__class__
    qs = klass.objects.filter(activation_key__iexact=new_code)
    if qs.exists():
        new_code = code_generator()
        return unique_code_generator(instance, code=new_code)
    return new_code
