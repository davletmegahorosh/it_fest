from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Members
from .serializers import MembersSerializer, MembersActivationSerializer
from members.email import send_activation_email

class MembersRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MembersSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            send_activation_email(member.email, member.confirmation_code)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembersActivationAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = MembersActivationSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.validated_data['member']
            member.accepted = True
            member.save()
            return Response({"detail": "Account activated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        email = request.GET.get('email')

        user = get_object_or_404(Members, email=email, confirmation_code=code)

        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({"detail": "Account activated successfully."}, status=status.HTTP_200_OK)
