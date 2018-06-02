from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from adkar.utils import unique_slug_generator
from adkar.validators import validate_body
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .utils import code_generator
from django.urls import reverse
import django  # you wont find this import django in "learn django" viedo apperently in this virsion of django i have to make
# the on_delete field my self that's why this import statment is here


# Create your models here.

def upload_location(instance, filename):
    return "{}/{}".format(instance.owner, filename)


USER = settings.AUTH_USER_MODEL


class Adkar(models.Model):
    # this default explenations is at SchoolBlog/main.models, the other default that you provide when making migrations is for making an id for a user
    owner = models.ForeignKey(USER, on_delete=django.db.models.deletion.CASCADE)
    title = models.CharField(max_length=200)
    type_of_content = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(null=True, blank=True, validators=[validate_body])
    time_of_updating = models.DateTimeField(auto_now=True)
    time_of_addition = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True, upload_to=upload_location)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True, unique=True)
    # my_date			  = models.DateTimeField(auto_now=False, auto_now_add=False)

    def activation_method(self):
        print('activate_via_email')


def adkar_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:  # this if statment is basically comunecating with the slug field to make it send True if the instance slug is been made and false if not
        instance.slug = unique_slug_generator(instance)
        # remember you can customize anything that's beeing saved here like forms and models and everthing


# def adkar_post_save_receiver(sender, instance, created, *args, **kwargs):

#	if not instance.slug:                               this is the saving method so you have to save() when your done unlike pre_save() which doesn't care
        # about saving because this is the saving method so if you called save without in if
        # statment it will bee an infinite loop of saving because it will try to save()
        # so it will call the saving method which is the same method 'post_save' then it
        # will try to save again and it will call the saving method post__save
        # and it will go on forever
#		instance.slug = unique_slug_generator(instance)
#		save()


pre_save.connect(adkar_pre_save_receiver, sender=Adkar)
# post_save.connect(adkar_pre_save_receiver, sender=Adkar)


class Activation(models.Model):
    user = models.OneToOneField(USER, on_delete=django.db.models.deletion.CASCADE)
    activation_key = models.CharField(max_length=120, null=True, blank=True)
    activated = models.BooleanField(default=False)

    def activation_method(self):
        print('activate_via_email')
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={'code': self.activation_key})
            subject = 'Activate acount'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your acount here: {path_}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activate your acount here: {path_}</p>'
            print(html_message)
            sent_mail = False
            # sent_mail = send_mail(subject, message, from_email, recipient_list,
            #                       fail_silently=False, html_message=html_message)
            return sent_mail


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        activation = Activation.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender=USER)
