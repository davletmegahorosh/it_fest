from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/section/', include('section.urls')),
    path('api/info/', include('itfestival.urls')),

]
