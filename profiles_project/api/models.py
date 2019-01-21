from django.db import  models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



from django.contrib.auth.models import BaseUserManager

   # default django user model is not efficient to apply our logic

class UserProfileManager(BaseUserManager):


    def create_user(self, email, name, password=None):
    #Creates  user profile  and save it in data base

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """we can modify here  the authority of admin."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    customized user class gives us more power to control our logic, by inheritance of provided django
    AbstractBaseUser
    """
     # id attributte is the parent class this important note
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


# methods of this class to return user's attributes
    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def get_short_name(self):
        """Django uses this when it needs to get the users appreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email



class profilefeedback (models.Model):
    """creating a table in the database where we can store the status of every profile user"""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    """this one to link every status with its profile and delete the status in case the user deleted his profile account"""
    status_text = models.CharField(max_length=255)
    """this is the status that we are gonna return from this class"""
    created_on = models.DateTimeField(auto_now_add=True)
    """this one to put a time for the status as the time when it is gonna be added"""

    def __str__(self):
        """this for returning the model as a string"""
        return self.status_text