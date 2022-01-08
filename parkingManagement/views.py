from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import uuid
from .serializers import CarToBeParkedSerializer, ParkingLotSerializer
from .models import CarToBeParked, ParkingLot


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerParkingLot(request):
    serializer = ParkingLotSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        adminPhone = request.data['adminPhone']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        totalSlots = request.data['totalSlots']
        emptySlots = request.data['emptySlots']
        ParkingLot(user=user,adminPhone=adminPhone,latitude=latitude,longitude=longitude,totalSlots=totalSlots,emptySlots=emptySlots).save()
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def registerCarToBeParked(request):
    serializer = CarToBeParkedSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.filter(username=request.data['parkingLotAdminId']).first()
        parkingLot = ParkingLot.objects.filter(user=user).first()
        startTime = request.data['startTime']
        endTime = request.data['emdTime']
        accessId = str(uuid.uuid4())
        CarToBeParked(parkingLot=parkingLot,startTime=startTime,endTime=endTime,accessId=accessId).save()
    return Response(serializer.data,status=status.HTTP_200_OK)
