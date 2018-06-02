from django import forms
from adkar.models import Adkar
from django.db.models.signals import pre_save, post_save
from adkar.validators import validate_title
from django.contrib.auth import get_user_model
# Note: to validate a field: name the validation function validate or clean depending on where is the
# validation function is,  then put an _  then the name of the field you wanna validate
# if your usung clean but if you're using validate then name the field what ever you like
# beacuse if your using validate insted of clean then you have a way of telling
# django which field you wanna validate simply by puting this in the field you
# wanna validate: validators=[a list of the validation functions you want on this field]
# otherwise you have to put clean then the name of the field for django to know it.
# Also if you're using validate it's ValidationError() not forms.ValidationError()
User = get_user_model()


class CreateAdkarForm(forms.Form):
    title = forms.CharField(label="العنوان")
    body = forms.CharField(required=False, label="النص")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "ammar":
            raise forms.ValidationError("لا تكتب زي كذا")
        return title


# this form is basically inhariting from the mode that's been givin to it which is Adkar so if
# you wanna modify it like normal Form(clean_data)
# then just modify the model it's inhariting from
class CreateAdkarModelForm(forms.ModelForm):
    title = forms.CharField(required=True, validators=[validate_title])
    # i can also make this in validators then add the validation list in adkaar.models if i don't want to override this title field field

    class Meta:
        model = Adkar
        fields = [
            "title",
            "body",
            'image'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "ammar":
            raise forms.ValidationError("لا تكتب زي كذا")
        return title

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if "حمار" in body:
            raise forms.ValidationError("انت الحمار")
        return body

# in the recievers the first name doesn't have to bee the same as the class name but this is just to remember which class this pre save is for
# the reason why we don't have to mention the class we want to take the instance from is because when we connect the pre save we mention that


def CreateAdkarModelForm_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.title = instance.title + "hi"


pre_save.connect(CreateAdkarModelForm_pre_save_receiver, sender=CreateAdkarModelForm)
# looks like this doesn't work you can still modify this in the adkar_pre_save_receiver by typing this same code


# Note: if you write only clean without the field name than you will validate every field go see documentation
# Note: if you wanna get really into validators you can actually make your own fields just like null and blank.


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='conform password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     qs = User.objects.filter(email__iexact=email)
    #     if qs.exists():
    #         raise forms.ValidationError('this user alredy exists')
    #     return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False

        if commit:
            user.save()
            user.activation.activation_method()
        return user
