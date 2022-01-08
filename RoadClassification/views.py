from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
import uuid
from .models import RoadComplains
from .serializers import RoadComplainSerializer
from . import DeepLearningModel
from PIL import Image
import os

# Create your views here.

dirpath = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(dirpath,'images')

@api_view(['POST'])
def damageComplain(request):
    serializer = RoadComplainSerializer(data=request.data)
    if serializer.is_valid():
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        image = request.FILES['image']
        image_location = str(uuid.uuid4())+'.jpeg'
        image_location = os.path.join(image_folder,image_location)
        image_np = DeepLearningModel.detect(image_location)
        im = Image.fromarray(image_np)
        location = str(uuid.uuid4())+'.jpeg'
        location = os.path.join(image_folder,location)
        im.save(location)
        RoadComplains(latitude=latitude,longitude=longitude).save()
    return Response(serializer.data,status=status.HTTP_200_OK)