from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters


from .models import UserProfile
from .serializers import ProfileSerializer


class ProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'login_count': ['gt', 'lte']
    }
