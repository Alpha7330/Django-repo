from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from . paginations import StandardResultsSetPagination,OffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.utils.decorators import method_decorator
from .Holiday import HolidayService
from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env('.env')

HOLIDAY_API_KEY=env('HOLIDAY_API_KEY')

# Create your views here.
class UserAPIView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    pagination_class = StandardResultsSetPagination
    # pagination_class=OffsetPagination


    # def get_authenticators(self):
    #     if self.request.method == ['GET','POST']:
    #         return []
    #     return super().get_authenticators()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()


    # @method_decorator(permission_classes([AllowAny]))
    # @method_decorator(authentication_classes([]))

    # @permission_classes([AllowAny])
    # @authentication_classes([])
    def get(self, request, pk=None):
        
        if pk is not None:
           
            try:
                user_objs =CustomUser.objects.get(id=pk)
                refresh = RefreshToken.for_user(user_objs)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                    }
            except CustomUser.DoesNotExist:
                return Response({'status':'fail','message': f'Invaild Id:- {pk}.',}, status=status.HTTP_404_NOT_FOUND)

            serialized_data = CustomUserSerializer(user_objs).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data,'newdata':data}, status=status.HTTP_200_OK)
        else:
            user_objs = CustomUser.objects.all()
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(user_objs, request)
            serialized_data = CustomUserSerializer(page, many=True).data
            return paginator.get_paginated_response({
                'status': 'success',
                'message': 'Data fetched successfully',
                'data': serialized_data
            })
            # serialized_data = CustomUserSerializer(user_objs, many=True).data
            # return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
    
    def post(self,request):

        
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            
            response_data = {
                'status': 'success',
                'message': 'User created successfully',
                'data': serializer.data,
                'tokens': tokens
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):	
        try:
            user_obj=CustomUser.objects.get(id=pk)
            user_obj.delete()
            return Response("successfully deleted")
        
        except CustomUser.DoesNotExist:
            return Response("not successful")
    
    def put(self,request,pk):	
        try:
            user_obj=CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer=CustomUserSerializer(instance=user_obj,data=request.data)	  
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({'message': 'failed to update','status':'failed'})		
        
    def patch(self,request,pk):
        try:
            user_obj=CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(instance=user_obj,data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()
           return Response({'message':'field updated successfully','data':serializer.data})
        else:
            return Response({'message':'field failed to be update'})
    
    
    # def get_tokens_for_user(user):
    #     refresh = RefreshToken.for_user(user)

    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }
class TokenUserView(APIView): 
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication] 
    def get(self,request): 
        user = request.user
         
        try:
            user_objs =CustomUser.objects.get(email=user.email)
            
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_data = CustomUserSerializer(user_objs).data
        return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
        

    def put(self,request):

        user=request.user

        
        try:
                 user_obj=CustomUser.objects.get(email=user.email)
        except CustomUser.DoesNotExist:
                 return Response({'status': 'fail'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer=CustomUserSerializer(instance=user_obj,data=request.data)	  
        if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response({'message': 'failed to update','status':'failed'})	

    def patch(self,request):
        user=request.user
        try:
            user_obj=CustomUser.objects.get(email=user.email)
        except CustomUser.DoesNotExist:
             return Response({'status': 'fail'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(instance=user_obj,data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()
           return Response({'message':'field updated successfully','data':serializer.data})
        else:
            return Response({'message':'field failed to be update'})
        

class HolidayListView(APIView):
    def get(self, request):
        service = HolidayService(api_key=HOLIDAY_API_KEY)
        country = request.GET.get('country')
        year = request.GET.get('year')

        data = service.get_holidays(country=country,year=year)
        # response.raise_for_status()
        response =  data.json()
        print(f'197---{response}')
        if response['status'] == 200:
            return Response(response)
        else:
            return Response('something went wrong while fetching data from api', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CountryListView(APIView):
    def get(self, request):
        service = HolidayService(api_key=HOLIDAY_API_KEY)
        data = service.get_countries()
        return Response(data)