from .models import *
from django.contrib.auth.backends import BaseBackend

class EmailAuthBackend(BaseBackend):
    """
    Custom authentication backend.

    Allows users to log in using their email address.
    """

    def authenticate(self,request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        
        user = Users.objects.get(kai_email=username,kai_password=password)
        if user:
            return user
        else:
            return None
        

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None