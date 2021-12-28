from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import CourseProductSerializer
from .models import CourseProduct


# Create your views here.

class ShowCourseProduct(APIView):
    def get(self,request):
        query=CourseProduct.objects.all()
        #print(query)
        serializers=CourseProductSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddCourseProduct(APIView):
    def post(self,request):
        serializers=CourseProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

