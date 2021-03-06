from django.shortcuts import render
from rest_framework import viewsets
from. import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models
from . import Permissions1
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated



class HelloApiView(APIView):
    """test the API view """

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """return a list with APIview features """

        an_apiview = [
            'use hhtp mthods a these functions (get, post, delete, patch)'
            'its similar to the django view'
            'it helps you to make the logic'
            'its mapped manually to urls'
         ]

        return Response ({'message':'Hello', 'an_apiview':an_apiview})



    def post (self, request):
        """create a message to the user a hello message with the name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            message = 'Hello{0}'.format(name)
            return Response({'message': message, 'email':email})

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """this for updating any object as the email as an example"""
        return Response({'method':'put'})


    def patch (Self, request, pk=None):
         """its for updating any object provided in the request"""
         return Response({"method" : 'patch'})

    def delete(self, request,pk=None):
        """deleting any object"""

        return Response({"method":'delete'})

class Helloviewset(viewsets.ViewSet):
    """for making or creating an object too just like the APIVIEW"""

    serializer_class = serializers.HelloSerializer

    def list (self,request):
        """return hello message in a different way not like we have done before"""

        a_viewset = [
            "uses actions {list, create, update, partial update, retrieve"
            "maps to urls using Routers"
            "provide more functionality with less code"
            "it does the same like Apiview we have used to post, delete, put or patch but in different way"
              ]
        return Response({"message" : 'Hello', "a_viewset" : a_viewset})

    def create (self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            message = 'Hello{0}'.format(name)
            return Response({'mwssage':message, 'email':email})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """RETRIEVE ANY OBJECT"""
        serializer = serializers.HelloSerializer(data=request.data)

        return Response({"http_method":'GET'})

    def update (self, request, pk=None):
        """UPDATE ANY OBJECT COMPLETELY"""
        return Response ({'http_method': "PUT"})



    def partial_update (self, request, pk=None):
        """UPDATE ANY OBJECT PARTIALLY"""
        return Response({'http_method':"PATCH"})

    def destroy (self, request, pk=None):
        """REMOVING AN OBJECT"""
        return Response({'http_method':"delete"})


class userprofileViewset(viewsets.ModelViewSet):

     """handles creating, creating and updating the profiles"""
     serializer_class = serializers.userprofileserializer
     queryset = models.UserProfile.objects.all()
     authentication_classes = (TokenAuthentication,)
     permission_classes = (Permissions1.UpdateownProfile,)
     filter_backends = (filters.SearchFilter,)
     """Its for adding filters like by name and so on"""
     search_fields =('name', 'email')
     """here we defined exactly what fileds the user can search by and use in the filters search"""

class Loginviewset (viewsets.ViewSet):
    """checks email and pass and return the response"""
    serializer_class = AuthTokenSerializer
    def create (self, request):
        """use the obtainauthtoken apiview to validate and create a token """
        return ObtainAuthToken().post(request)


class profilefeedbackviewset(viewsets.ModelViewSet):
    """handles, creating, reading, updating the status"""

    authentication_classes = (TokenAuthentication,)
    queryset = models.profilefeedback.objects.all()
    serializer_class = serializers.profilefeedbackserializers
    permission_classes = (Permissions1.postownstatus, IsAuthenticated)

    def perform_create (self, serializer):
        """this is for handling when the user writes the status just in his profile not in any others profiles"""
        """so we will inherite from the models this class 'user_profile' from the class of feedback in the modls just to keep the foriegn key
         and to be sure that the user is making a status in his own account and we will add to that in the permissions file"""

        serializer.save(user_profile=self.request.user)


