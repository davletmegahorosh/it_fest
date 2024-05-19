from django.urls import path
from .views import SectionsListView, SectionsDetailView

urlpatterns = [
    path('', SectionsListView.as_view(), name='sections-list-view'),
    path('<str:path>/', SectionsDetailView.as_view(), name='sections-detail-view'),  # Детальное представление секций
]
