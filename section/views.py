from rest_framework import generics
from .models import Sections
from .serializers import SectionsListSerializer, SectionsDetailSerializer


class SectionsListView(generics.ListAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsListSerializer
    lookup_field = 'path'


class SectionsDetailView(generics.RetrieveAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsDetailSerializer
    lookup_field = 'path'