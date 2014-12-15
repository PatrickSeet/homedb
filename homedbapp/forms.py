from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from homedbapp.models import Shopper, Property


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}))
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


    class Meta:
        model = Shopper
        fields = ("username", "first_name", "last_name", "phone", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Shopper.objects.get(username=username)
        except Shopper.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class PropertyForm(ModelForm):

    mlsid = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    numofbdrms = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    numofbthrms = forms.FloatField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    numofmaster = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    sqfootage = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    lotsize = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    askingprice = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    offeredpricce = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    soldprice = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    roof = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    kitchen = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    bathrooms = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    frontyard = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    backyard = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    termite = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    foundation = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    neighborhood = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    propertytype = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box'}), required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Property
        exclude = ('xcoordinate', 'ycoordinate',)
