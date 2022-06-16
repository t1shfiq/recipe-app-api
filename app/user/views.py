"""
Views for the user API
"""
from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.APIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer