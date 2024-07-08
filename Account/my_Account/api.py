from django.shortcuts import render
from django.http import HttpResponse
from .models import Details



def index(request):


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        user_details = Details(first_name=first_name, last_name=last_name, email=email, message=message)
        user_details.save()

    return render(request, "templates/index.html", {})
