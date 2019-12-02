from django.urls import path

from .views import ProfileListAPIView


urlpatterns = [
    # path('profile-view/', ProfileView.as_view()),
    path('list-view/', ProfileListAPIView.as_view()),
]
