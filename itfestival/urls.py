from django.urls import path
from .views import (
    SpeakerListView,
    SponsorsListView,
    PartnerListView
)

urlpatterns = [
    path('sponsor/', SponsorsListView.as_view(), name='sponsor-list-view'),
    path('speakers/', SpeakerListView.as_view(), name='speaker-list-view'),
    path('partner/', PartnerListView.as_view(), name='partner-list-view'),
]