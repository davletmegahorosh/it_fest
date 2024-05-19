from rest_framework import generics
from .models import Speaker, Sponsor, Partner
from .serializers import SpeakerSerializer, SponsorsSerializer, PartnerSerializer


class SpeakerListView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class SponsorsListView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorsSerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

