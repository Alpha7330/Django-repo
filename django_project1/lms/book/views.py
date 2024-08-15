from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env('.env')
# Create your views here.

###########------Author---------###########
class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class author_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field='id'        
# #read
# @api_view([ 'GET'])
# def home(request):
#     auth_obj=Author.objects.all()
#     serializer=AuthorSerializer(auth_obj,many=True)
#     return Response({'status':200,'message':'this api is working properly','payload':serializer.data})

# #create
# @api_view(['POST'])
# def cre_op(request):
#     serializer=AuthorSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)    
#     else:
#         return Response(serializer.errors)
    
# #update
# @api_view(['POST'])
# def up_op(request,id):
#     auth_obj=Author.objects.get(id=id)  
#     serializer=AuthorSerializer(instance=auth_obj,data=request.data)  
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
# #delete
# @api_view(['DELETE'])  
# def del_op(request,id):
#     auth_obj=Author.objects.get(id=id)
#     auth_obj.delete()
#     return Response("author is deleted successfully")  

##################---------Books----------#################

class BookListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = Bookserializer
    lookup_field = 'id'
    
######################-----USER-------generic api and mixins------##########################

class Userlist_create(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
       
    
class Userdis_up_del(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def  delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)

####################################  EMAIL #################################
class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_email()
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
################################  library ################################
class LibraryView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = Libraryserializer

class detail_libary_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = Libraryserializer
    lookup_field='id'

################################  librarians #############################

class libraians_view(generics.ListCreateAPIView):
    queryset = librarians.objects.all()
    serializer_class = librariansserializer

class detail_libraians_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = librarians.objects.all()
    serializer_class = librariansserializer        
    lookup_field='id'
###################################### APIVIEW ######################
class AuthorAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            # author_objs = get_object_or_404(Author, pk=pk)
            try:
                author_objs = Author.objects.get(id=pk)
                print(f'127-------{author_objs}')
            except Author.DoesNotExist:
                return Response({'status':'fail','message': f'Invaild Id:- {pk}.',}, status=status.HTTP_404_NOT_FOUND)

            serialized_data = AuthorSerializer(author_objs).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
        else:
            author_objs = Author.objects.all()
            print(f'135-------{author_objs}')
            serialized_data = AuthorSerializer(author_objs, many=True).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):	
        try:
            auth_obj=Author.objects.get(id=pk)
            auth_obj.delete()
            return Response("successfully deleted")
        
        except Author.DoesNotExist:
            return Response("not successful")
    
    def put(self,request,pk):	
        try:
            auth_obj=Author.objects.get(id=pk)
        except Author.DoesNotExist:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer=AuthorSerializer(instance=auth_obj,data=request.data)	  
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({'message': 'failed to update','status':'failed'})		
        
    def patch(self,request,pk):
        try:
            auth_obj=Author.objects.get(id=pk)
        except Author.DoesNot:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        nationality=request.data.get('nationality')

        if nationality == None:
            return Response({'status': 'fail', 'message': 'field does not exist'})

        serializer = AuthorSerializer(instance=auth_obj, data={'nationality': nationality}, partial=True)

        if serializer.is_valid():
           serializer.save()
           return Response({'message':'field updated successfully'})
        else:
            return Response({'message':'field failed to be update'})
        



class BookAPIView(APIView):
    def get(self, request, pk=None):

        if pk==None:
            try:
               book_objs = Books.objects.all()
            except Books.DoesNotExist:
                return Response({'message': 'Book not found'})   
            
            serializer=Bookserializer(book_objs,many=True)
            return Response({'books':serializer.data,'message':'books fetched successfully'})
        else:
            try:
               book_objs=Books.objects.get(id=pk)
            except:
                return Response({'message':'failed'})   
            serializer=Bookserializer(book_objs)
            return Response({'books':serializer.data,'message':'successful'})

    def post(self,request):
        serializer=Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        else:
            return Response(serializer.errors)
    
    def delete(self, request,pk):
        try:
            book_obj=Books.objects.get(id=pk)
            book_obj.delete()
            return Response("successfully deleted")
        
        except Books.DoesNotExist:
            return Response("not successful")
        
    def put(self,request,pk):    
        try:
            book_obj=Books.objects.get(id=pk)
        except Books.DoesNotExist:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer=Bookserializer(instance=book_obj,data=request.data)	  
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            # return Response({'message': 'failed to update','status':'failed'})		
            return Response(serializer.errors)
        
    def patch(self,request,pk):
        try:
            book_obj=Books.objects.get(id=pk)
        except Books.DoesNot:
             return Response({'status': 'fail', 'message': f'Invalid Id: {pk}'}, status=status.HTTP_404_NOT_FOUND)
        
        book_title=request.data.get('book_title')
        if book_title == None:
            return Response({'status': 'fail', 'message': 'field does not exist'})
        
        serializer=Bookserializer(instance=book_obj,data={'book_title': book_title},partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response({'message':'field updated successfully'},serializer.data)
        else:
            return Response({'message':'field failed to be update'})
