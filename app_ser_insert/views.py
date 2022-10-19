from functools import partial
from django.shortcuts import render
import random
from app_ser_insert.serializers import StudentSerializer
from .models import Student
from django.http import HttpResponse, JsonResponse

# Create your views here.


# Single Student data(Model Object)

def student_insert(request):
    
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


def student_update(request):
    # CREATING DATA FOR UPDATE INTO SERIALIZERS
    data = {
        'id':1,
        'name':'Hemang',
        'roll':'102',
        'city':'Surat'
    }

    instance_data = Student.objects.get(id=data['id'])
    # .save() WILL UPDATE THE EXISTING 'Student' instance 
    serializer = StudentSerializer(instance_data, data=data, partial=True)

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

def student_delete(request):
    # CREATING DATA FOR DELETE INTO SERIALIZERS
    data = { 'id' : 5 }

    try:
        instance_data = Student.objects.get(id=data['id'])
        res = instance_data.delete()
        res = {'status':True, 'msg':'DATA DELETED!!'}
        return JsonResponse(res, safe=False)
    except:
        return JsonResponse({'res':'Something Went Wrong'}, safe=False)