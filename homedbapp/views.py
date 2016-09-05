from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.conf import settings
from homedb.settings import GOOGLE_API_KEY
from homedbapp.forms import EmailUserCreationForm, PropertyForm
from homedbapp.models import Property, Shopper
from geolocation.google_maps import GoogleMaps
from json import encoder
import json

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div><div>Signed up on {}'.format(
                user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("/properties/")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {'form': form})


def faq(request):

    return render(request, 'faq.html')


def index(request):

    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

@login_required
def profile(request):

    return render(request, 'registration/profile.html')


@login_required()
def properties(request):

    #retrieving Lat Lng info from db, format to pass to javascript for display markers
    json.encoder.FLOAT_REPR = lambda o: format(o, '.6f')
    properties = Property.objects.all()
    cords_list = []

    for i in properties:
        cords_list.append(i.xcoordinate)
        cords_list.append(i.ycoordinate)

    cords_json = json.dumps(cords_list)

    data = {"properties": properties, "cords_json": cords_json}

    return render(request, "properties/properties.html", data)


@login_required()
def new_property(request):

    s3_url = "https://homedbbucket.s3.amazonaws.com/"
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = PropertyForm(request.POST, request.FILES)
        # Django will check the form's validity
        if form.is_valid():

            # Saving the form will create a new Property object
            if form.save():
                data = form.cleaned_data
                #using property address to lat and lng info from google map, then update table
                property_address = data['address']
                google_maps = GoogleMaps(api_key=GOOGLE_API_KEY)
                location_info = google_maps.query(location=property_address)
                location_info = location_info.first()
                Property.objects.filter(address=property_address).update(xcoordinate=location_info.lat)
                Property.objects.filter(address=property_address).update(ycoordinate=location_info.lng)

                # After saving, redirect the user to add propertynotes
                return redirect("/properties/")
            else:
                print "not saved"
        else:
            print "form not valid"

    # Else if the user is looking at the form page
    else:
        form = PropertyForm()
        print "post failed"

    data = {'form': form, 's3_url': s3_url}

    return render(request, "properties/add_property.html", data)


@login_required()
def view_property(request, property_id):

    s3_url = "https://homedbbucket.s3.amazonaws.com/"
    property = Property.objects.get(id=property_id)
    percentage_over = round((float(property.soldprice - property.askingprice) / float(property.askingprice)) * 100)
    beat_by = property.soldprice - property.offeredpricce
    x = property.xcoordinate
    y = property.ycoordinate

    data = {"property": property, "percentage_over": percentage_over, "beat_by": beat_by,
            "x": x, "y": y, 's3_url': s3_url}

    return render(request, "properties/view_property.html", data)


@login_required()
def edit_property(request, property_id):

    s3_url = "https://homedbbucket.s3.amazonaws.com/"
    # Similar to the the detail view, we have to find the existing genre we are editing
    property = Property.objects.get(id=property_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            if form.save():
                return redirect("/property/{}".format(property_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = PropertyForm(instance=property)
    data = {"property": property, "form": form, 's3_url': s3_url}
    return render(request, "properties/edit_property.html", data)

@login_required()
def delete_property(request, property_id):

    property = Property.objects.get(id=property_id)
    property.delete()

    return redirect("/properties/")