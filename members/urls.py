from django.urls import path
from .views import MembersRegistrationAPIView, MembersActivationAPIView

urlpatterns = [
    path('register/', MembersRegistrationAPIView.as_view(), name='member-registration'),
    path('activate/', MembersActivationAPIView.as_view(), name='member-activation'),
]