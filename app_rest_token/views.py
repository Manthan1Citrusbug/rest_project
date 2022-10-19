import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.


# Login Form class
class user_login(View):
    def get(self, request):
        return render(request,'login.html')

# Custom Token Generation class 
# class custom_token(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         # Convert JSON String into python datatype (eg. dict)
#         data = json.loads(request.POST['data'])

#         # create serializer for user model
#         serializer = self.serializer_class(data = data,context={'request': request})

#         # check for serializer data is valid or not
#         if serializer.is_valid():

#             # serializer.validated_data['user'] has user value object 
#             user = serializer.validated_data['user']
            
#             # token take value of token and created take boolean value true or false
#             token, created = Token.objects.get_or_create(user=user)
            
#             # Send token and other data
#             return JsonResponse({
#                 'status':True,
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'user_name': user.username,
#                 'password': user.password
#             })
        
#         # send error massage
#         return JsonResponse({'status':False,'msg': serializer.errors})


class custom_token(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # create serializer for user model
        print(request.data)
        serializer = self.serializer_class(data = request.data,context={'request': request})
        # check for serializer data is valid or not
        if serializer.is_valid():
            # serializer.validated_data['user'] has user value object 
            user = serializer.validated_data['user']
    
            # token take value of token and created take boolean value true or false
            token, created = Token.objects.get_or_create(user=user)
            
            # Send token and other data
            return JsonResponse({
                'status':True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
                'password': user.password
            })
        # send error massage
        return JsonResponse({'status':False,'msg': serializer.errors})