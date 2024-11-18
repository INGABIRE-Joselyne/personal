from http.client import responses

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from propertapp.serializer import Userserializers,TernantSerializer
from propertapp.serializer import Ternant
from propertapp.models import Ternant,User
from  drf_spectacular.utils import extend_schema

@extend_schema(
    methods=['GET', 'POST'],
    request=Userserializers,
    responses=Userserializers,
    description='retrieve all user or create a user'
)

@api_view(['GET','POST'])
def user_info(request):
    if request.method=='GET':
        user=User.objects.all()
        myserializer=Userserializers(user,many=True)
        return Response(myserializer.data)
    elif request.method=='POST':
        serial=Userserializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,201)
        return Response(serial.errors,401)

@api_view(['GET', 'POST'])
def Ternant_info(request):
        if request.method=='GET':
            ternant=Ternant.objects.all()
            myserializer=TernantSerializer(ternant,many=True)
            return Response(myserializer.data)
        elif request.method=='POST':
            serial=TernantSerializer(data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data,201)
                return Response(serial.errors,401)


# Create your views here.
