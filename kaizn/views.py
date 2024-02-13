
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .authentication import EmailAuthBackend 
from .models import *
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import UsersSerializer,ItemsSerializers,TagsSerializers,TagsBulkCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser



@api_view(['POST'])
def login_page(request):
    
    """
    Used to authenticate the user.

    """

    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
         
        # Check if a user with the provided username exists
        if not Users.objects.filter(kai_email=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return HttpResponse("Invalid Username",status=400)

         
        # Authenticate the user with the provided username and password
        eb = EmailAuthBackend()
        user = eb.authenticate(request=request,username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return HttpResponse("Invalid Password", status=400)

        else:
            # Log in the user and redirect to the home page upon successful login
            return HttpResponse("Login Successful", status=200)
     
 
# Define a view function for the registration page
@api_view(['POST'])
def register_page(request):
    """
    Registers the new user.
    """
    if request.method == 'POST':
        username = request.data.get('kai_email')
        password = request.data.get('kai_password')
        print(username,password) 
        # Check if a user with the provided username already exists
        user = Users.objects.filter(kai_email=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        else:         
    
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data)
            return HttpResponse(serializer.errors, status=400)
     
    # Render the registration page template (GET request)
    #return render(request, 'register.html')
    

@api_view(['POST'])
def add_item(request):
    """
    Adds items to the list
    """
    if request.method == "POST":
        SKU = request.data['kai_SKU']
               
        print(request.data,SKU)

        item = Items.objects.filter(kai_SKU=SKU)
        if item.exists():
            pass
        else:
            serializer = ItemsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            # it = Items(kai_SKU=SKU,kai_Name=Name,kai_Category=Category,kai_instock=In_Stock,kai_available_stock=Av_Stock) 
            # it.save()
            r_tags = request.data['Tags']
            tags = r_tags.split(',')
            print(tags)
            # lst = []

            for i in range(len(tags)):
                tmp = {}
                tmp['kai_SKU'] = SKU
                tmp['kai_tags'] = tags[i]
                t_serializer = TagsSerializers(data=tmp)
                if t_serializer.is_valid():
                    t_serializer.save()

            # # for i in range(len(tags)):
            # #     lst.append({'tag':tags[i],'SKU':SKU})
            
            # tags_serializer = TagsBulkCreateSerializer(data={'tag_data':request.data})
            # if tags_serializer.is_valid():
            #     tags_serializer.save()

        #messages.info(request, "Item created Successfully!")
        # return redirect('/dashboard/')
        return HttpResponse("Item created!")


@api_view(['GET'])
def display_items(request):
    """
    Displays the items present in the database.
    """
    if request.method == "GET":
        itemset = Items.objects.select_related().all()
        # for n in itemset:
        #     print()

        serli = ItemsSerializers(itemset,many=True)
        return JsonResponse(serli.data,safe=False)