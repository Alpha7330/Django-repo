from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *
from django.core.mail import send_mail

def validate(value):
    if value<0:
        raise serializers.ValidationError('value should be positive')
    elif value==0:
        raise serializers.ValidationError('value should be greater than zero')


    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = ['id', 'author_name', 'nationality']


class Bookserializer(serializers.ModelSerializer):
    author_id=serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        many=True,
        write_only=True,
        source="authors"
    )
    authors=AuthorSerializer(many=True,read_only=True)
    class Meta:
        model=Books
        fields = ['id', 'book_title', 'book_published_date','author_id','authors']



class UserSerializer(serializers.ModelSerializer):
    books_borrowed=Bookserializer(many=True,read_only=True)
    books_borrowed_ids = serializers.PrimaryKeyRelatedField(
        queryset=Books.objects.all(),
        many=True,
        write_only=True,  
        source='books_borrowed'
    )
    
       

    class Meta:
        model = User
        fields = ['id','user_name','books_borrowed','books_borrowed_ids']
   

class EmailSerializer(serializers.Serializer):        
    email=serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    def send_email(self):
        email=self.validated_data['email']
        subject = self.validated_data['subject']
        message = self.validated_data['message']
        from_email='alpha733060@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        

class Libraryserializer(serializers.ModelSerializer):
    books_in_library=Bookserializer(many=True,read_only=True)
    books_available=serializers.PrimaryKeyRelatedField(
        queryset=Books.objects.all(),
        many=True,
        write_only=True,
        source='books_in_library'
    )
    class Meta:
        model=Library
        fields=['id','library_name','books_in_library','books_available']


class librariansserializer(serializers.ModelSerializer):
    library_con=Libraryserializer(many=True,read_only=True)
    library_id=serializers.PrimaryKeyRelatedField(
        queryset=Library.objects.all(),
        many=True,
        write_only=True,
        source='library_con'
    )
    class Meta:
        model=librarians
        fields=['id','librarians_name','library_con','library_id']



# class AuthorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=Author
#         fields=['id','author_name','nationality']
