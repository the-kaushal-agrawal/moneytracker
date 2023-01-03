from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *



@api_view(['GET'])
def apiurls(request):
    api_urls = {
        'Users List' : '/users-list',
        'Transcation List' : '/trans-list',
         'Transcation Create': '/trans-create',
        'Transcation Detail': '/trans-detail/<str:pk>',
        'Transcation Update' : '/trans-update/<str:pk>',
        'Transcation Delete': '/trans-delete/<str:pk>',
       
    }

    return Response(api_urls)
@api_view(['GET'])
def members(request):
    user = User.objects.all()
    serialise = UserSerializer(user,many = True)
    return Response(serialise.data)

@api_view(['GET'])
def listtrans(request):

    data = TranscationsData.objects.all()
    serialise = TransSerializer(data,many = True)
    return Response(serialise.data)

@api_view(['POST'])
def createtrans(request):
    serialiser = TransSerializer(data = request.data,many = False)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['GET'])
def detailtrans(request,pk):
    trans = TranscationsData.objects.get(id = pk)
    serialiser = TransSerializer(trans,many = False)
    return Response(serialiser.data)

@api_view(['DELETE'])
def deletetrans(request,pk):
    trans = TranscationsData.objects.get(id = pk)
    trans.delete()
    return Response("transcation deleted successfully")


@api_view(['POST'])
def updatetrans(request,pk):
    trans = TranscationsData.objects.get(id = pk)
    serialiser = TransSerializer(instance = trans,data = request.data,many = False)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)


