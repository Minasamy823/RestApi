from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """serializers are for cjanging the type of an object into binary or any other type to
    be permenantly saved in the database"""

    name = serializers.CharField(max_length=10)
    email = serializers.CharField(max_length=20)


    """models in general for arranging the data in the data base, serializer file is to appear the fields that are 
    necessary to be in the interfase of the user while the file of the viewset is to control what will be the output
     that will comeup to the user, so if we put thefile of the email in the serializers but not in the view file the
      user will see the icon where he can write the emial but when he presses enter there will be any output related
       to the email unless you haven't mention it in the view file"""


class userprofileserializer (serializers.ModelSerializer):
    """ITS FOR OUR PROFILE OBJECTS"""

    class Meta:
        """meta class tells rest framework what classes do we need to take from the models to appear for the user in the screen """
        model = models.UserProfile
        fields = ('id', 'name', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


    def create (self, validated_data):
        """to create and return the users"""
        user = models.UserProfile (
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class profilefeedbackserializers(serializers.ModelSerializer):
    """this serializers is for the model of the feedback we have created and it is responsibile for appering the fields er have
    created in the database , so for evey model we create in the database we need a serializer for it to appear in the iterface of the user"""
    class Meta:

           model = models.profilefeedback
           fields = ('id', 'user_profile', 'status_text', 'created_on')
           extra_kwargs = {'user_profile' : {'read_only' : True}}