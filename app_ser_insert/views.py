from django.shortcuts import render
import random, json, io
from app_ser_insert.serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

# Create your views here.


# Single Student data(Model Object)

def student_insert():
    
    name = ['Raj','Rani','Rahul','Hemang','Parth','Kaushik','Keyur']
    city = ['Ahmedabad','Surat','vapi','Mumbai','Rajkot','Vadodara']
    
    # CREATING DATA FOR INSERT INTO SERIALIZERS
    data = {
        'name':random.choice(name),
        'roll':101,
        'city': random.choice(city)
    }
    
    # .save() WILL CREATE A NEW INSTANCE
    serializer = StudentSerializer(data = data)

    # .save() WILL UPDATE THE EXISTING 'Student' instance 
    # serializer = StudentSerializer(Student, data = data)

    if serializer.is_valid():
        print(serializer.validated_data)

        # YOU CAN TRY 
        serializer.save()
        # OR
        # serializer.create(serializer.validated_data)

        res = {'status':True, 'msg':serializer.validated_data}
        return JsonResponse(res, safe=False)
    
    res = {'status':False, 'msg':serializer.errors}
    return JsonResponse(res, safe=False)


def student_update():
    # CREATING DATA FOR INSERT INTO SERIALIZERS
    data = {
        'name':'Hemang',
        'roll':102,
        'city':'Surat'
    }

    # .save() WILL UPDATE THE EXISTING 'Student' instance 
    serializer = StudentSerializer(Student, data=data)

    if serializer.is_valid():
        print(serializer.validated_data)

        # YOU CAN TRY 
        serializer.save()
        # OR
        # serializer.create(serializer.validated_data)

        res = {'status':True, 'msg':serializer.validated_data}
        return JsonResponse(res, safe=False)
    
    res = {'status':False, 'msg':serializer.errors}
    return JsonResponse(res, safe=False)