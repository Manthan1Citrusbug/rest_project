from django.shortcuts import render

from app_ser_view.serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


# Single Student data(Model Object)

def student_detail(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    
    # YOU CAN WRITE THIS 2 LINE CODE FOR HTTPRESPONSE OR YOU CAN USE JSONRESPONSE ALSO
    
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    
    # if you have simple dict object you don't need to write safe=False
    # but in this case multiple dict object is inside the list so you have to write safe=False
    return JsonResponse(serializer.data, safe=False)

