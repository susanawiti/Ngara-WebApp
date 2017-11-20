from .models import Index
from .models import About
from .models import Service
from .models import Contact
from django.contrib.auth.models import User
# from snippets.models import Snippet
from .models import Snippet

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """contains user model serializer fields """
    class Meta:
        model = User
        fields = (
            'first_name',
            'email',
            'password',
            "username"
            )
        write_only_fields = ('password', )
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
        
        

        
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            
            'service_of_choice',
            'hours_choice',
            'rooms',
            'service_summary',
            'full_name',
            'phone_number',
            'email',
            'location_of_choice'
            )

class IndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Index
        fields = ('service','timestamp','picture')
        
        
class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ('service','timestamp')
        

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('service','timestamp')
        
        
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('service','timestamp')
        
       
        
        
        