from rest_framework import  serializers
from propertapp.models import Ternant,User

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email','password']
        extra_kwargs={
            'id':{'read_only':True},
            'Password':{'write_only':True},

        }
class TernantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ternant
        fields=['id','names','phone','email']
        extra_kwargs={
           'id':{'read_only':True},

        }

