from django.urls import path

# from rest_framework.routers import DefaultRouter

# from profiles_api import views
from .views import ProfileView, ProfileListAPIView

# router = DefaultRouter()
# router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('profile-view/', ProfileView.as_view()),
    path('list-view/', ProfileListAPIView.as_view()),

    # path('', include(router.urls))
]
