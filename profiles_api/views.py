from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q


from .models import UserProfile
from .serializers import ProfileSerializer

class ProfileView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ProfileSerializer(profiles, many=True)
        return Response({"profile": serializer.data})

class ProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    filter_fields = {
        'id': ['gte', 'lte']
    }

    # def get_queryset(self):
        # return UserProfile.objects.filter(login_count__gt=0)
        # return UserProfile.objects.filter(login_count__lte=0)
