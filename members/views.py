from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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