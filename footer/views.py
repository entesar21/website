from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import FooterSerializer
from .models import Footer


# Create your views here.

class ShowFooter(APIView):
    def get(self,request):
        query=Footer.objects.all()
        #print(query)
        serializers=FooterSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddFooter(APIView):
    def post(self,request):
        serializers=FooterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render

# Create your views here.
