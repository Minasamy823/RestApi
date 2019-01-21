from rest_framework import permissions

class UpdateownProfile (permissions.BasePermission):
    """allow user to edit their own profile but not the others"""



    def has_object_permission(self, request, view, obj):

       if request.method in permissions.SAFE_METHODS:

            return True

       return obj.id == request.user.id




class postownstatus (permissions.BasePermission):
    """allow user to edit their own status but not the others"""



    def has_object_permission(self, request, view, obj):

       if request.method in permissions.SAFE_METHODS:

            return True

       return obj.user_profile.id == request.user.id
    """here we used the user_profile which we have used tin the models files to be sure that its the profile of that user not the other"""