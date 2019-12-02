from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import ProfileSerializer

class ProfileView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"profile": serializer.data})
        
